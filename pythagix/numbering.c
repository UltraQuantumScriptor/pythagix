#include <Python.h>
#include <stdlib.h>
#include <time.h>

/* ---------- Helper: GCD ---------- */
static PyObject* py_gcd(PyObject* a, PyObject* b){
    PyObject* zero = PyLong_FromLong(0);
    PyObject *x=Py_NewRef(a),*y=Py_NewRef(b),*tmp,*mod;
    while(PyObject_RichCompareBool(y, zero, Py_NE)){
        mod = PyNumber_Remainder(x,y);
        Py_DECREF(tmp=x);
        x=y; y=mod;
    }
    Py_DECREF(y);
    Py_DECREF(zero);
    return x;
}

/* ---------- Helper: modular exponentiation ---------- */
static PyObject* py_modpow(PyObject* base, PyObject* exp, PyObject* mod){
    PyObject* result = PyLong_FromLong(1);
    PyObject* b = Py_NewRef(base);
    PyObject* e = Py_NewRef(exp);
    PyObject* one = PyLong_FromLong(1);
    PyObject* two = PyLong_FromLong(2);

    while(PyObject_RichCompareBool(e, PyLong_FromLong(0), Py_GT)){
        PyObject* rem = PyNumber_Remainder(e, two);
        if(PyObject_RichCompareBool(rem, one, Py_EQ)){
            PyObject* tmp = PyNumber_Multiply(result, b);
            Py_DECREF(result);
            result = PyNumber_Remainder(tmp, mod);
            Py_DECREF(tmp);
        }
        Py_DECREF(rem);
        PyObject* tmp_b = PyNumber_Multiply(b,b);
        PyObject* tmp_b2 = PyNumber_Remainder(tmp_b, mod);
        Py_DECREF(tmp_b); Py_DECREF(b); b=tmp_b2;

        PyObject* tmp_e = PyNumber_FloorDivide(e, two);
        Py_DECREF(e); e=tmp_e;
    }
    Py_DECREF(b); Py_DECREF(e); Py_DECREF(one); Py_DECREF(two);
    return result;
}

/* ---------- Miller-Rabin primality test ---------- */
static int is_prime(PyObject* n, int k){
    PyObject* two = PyLong_FromLong(2);
    PyObject* one = PyLong_FromLong(1);
    PyObject* n_minus_one = PyNumber_Subtract(n, one);

    if(PyObject_RichCompareBool(n, two, Py_LT)){ Py_DECREF(two); Py_DECREF(one); Py_DECREF(n_minus_one); return 0; }

    long small_primes[] = {2,3,5,7,11,13,17,19,23,29};
    for(int i=0;i<sizeof(small_primes)/sizeof(long);i++){
        PyObject* sp = PyLong_FromLong(small_primes[i]);
        if(PyObject_RichCompareBool(n, sp, Py_EQ)){ Py_DECREF(sp); goto prime_true; }
        PyObject* rem = PyNumber_Remainder(n, sp);
        if(PyObject_RichCompareBool(rem, PyLong_FromLong(0), Py_EQ)){ Py_DECREF(rem); Py_DECREF(sp); goto prime_false; }
        Py_DECREF(rem); Py_DECREF(sp);
    }

    PyObject* d = PyNumber_Subtract(n, one);
    int r=0;
    while(1){
        PyObject* rem = PyNumber_Remainder(d, two);
        int is_even = PyObject_RichCompareBool(rem, PyLong_FromLong(0), Py_EQ);
        Py_DECREF(rem);
        if(!is_even) break;
        PyObject* tmp = PyNumber_FloorDivide(d, two);
        Py_DECREF(d);
        d=tmp;
        r++;
    }

    srand((unsigned)time(NULL));
    for(int i=0;i<k;i++){
        unsigned long a_val = 2 + rand()%1000000;
        PyObject* a = PyLong_FromUnsignedLong(a_val);
        PyObject* x = py_modpow(a,d,n);
        if(PyObject_RichCompareBool(x, one, Py_EQ) || PyObject_RichCompareBool(x, n_minus_one, Py_EQ)){Py_DECREF(x); Py_DECREF(a); continue;}
        int found=0;
        for(int j=0;j<r-1;j++){
            PyObject* tmp = py_modpow(x, two, n);
            Py_DECREF(x); x=tmp;
            if(PyObject_RichCompareBool(x, n_minus_one, Py_EQ)){found=1; break;}
        }
        Py_DECREF(x); Py_DECREF(a);
        if(!found) goto prime_false;
    }

prime_true:
    Py_DECREF(two); Py_DECREF(one); Py_DECREF(n_minus_one); Py_DECREF(d);
    return 1;
prime_false:
    Py_DECREF(two); Py_DECREF(one); Py_DECREF(n_minus_one); Py_DECREF(d);
    return 0;
}

/* ---------- Pollard Rho ---------- */
static PyObject* pollard_rho(PyObject* n){
    if(is_prime(n, 8)) return Py_NewRef(n);

    PyObject* x = PyLong_FromLong(rand()%100 + 2);
    PyObject* y = Py_NewRef(x);
    PyObject* one = PyLong_FromLong(1);
    PyObject* c = PyLong_FromLong(rand()%10 + 1);
    PyObject* factor = PyLong_FromLong(1);

    while(PyObject_RichCompareBool(factor, one, Py_EQ)){
        PyObject* tmp1 = PyNumber_Add(PyNumber_Multiply(x,x), c);
        PyObject* tmp2 = PyNumber_Remainder(tmp1, n); Py_DECREF(tmp1); Py_DECREF(x); x=tmp2;

        PyObject* tmpy = PyNumber_Add(PyNumber_Multiply(y,y), c);
        PyObject* tmpy2 = PyNumber_Remainder(tmpy, n); Py_DECREF(tmpy); Py_DECREF(y); y=tmpy2;
        tmpy = PyNumber_Add(PyNumber_Multiply(y,y), c);
        tmpy2 = PyNumber_Remainder(tmpy, n); Py_DECREF(tmpy); Py_DECREF(y); y=tmpy2;

        PyObject* diff = PyNumber_Subtract(x,y);
        factor = py_gcd(diff, n);
        Py_DECREF(diff);
    }
    Py_DECREF(x); Py_DECREF(y); Py_DECREF(one); Py_DECREF(c);
    return factor;
}

/* ---------- Recursive factorization ---------- */
static void factor_recursive(PyObject* n, PyObject* list){
    if(PyObject_RichCompareBool(n, PyLong_FromLong(1), Py_EQ)) return;
    if(is_prime(n,8)){ PyList_Append(list,n); return; }

    PyObject* f = pollard_rho(n);
    PyObject* div = PyNumber_FloorDivide(n,f);
    factor_recursive(f,list);
    factor_recursive(div,list);
    Py_DECREF(f); Py_DECREF(div);
}

/* ---------- Python wrapper: get_factors ---------- */
static PyObject* py_get_factors(PyObject* self, PyObject* args){
    PyObject* n;
    if(!PyArg_ParseTuple(args,"O",&n)) return NULL;

    PyObject* factors = PyList_New(0);
    factor_recursive(n,factors);
    return factors;
}

int compress_0_c(const int* values, int len, int* out){
    if(len<=0) return 0;
    int j=0; out[j++]=values[0];
    for(int i=1;i<len;i++){
        if(values[i]==0 && out[j-1]==0) continue;
        out[j++] = values[i];
    }
    return j;
}

static PyObject* py_compress_0(PyObject* self, PyObject* args){
    PyObject* input_list;
    if(!PyArg_ParseTuple(args,"O!",&PyList_Type,&input_list)) return NULL;

    Py_ssize_t len = PyList_Size(input_list);
    if(len==0) return PyList_New(0);

    int* values = malloc(sizeof(int)*len);
    int* out = malloc(sizeof(int)*len);

    for(Py_ssize_t i=0;i<len;i++) values[i]=(int)PyLong_AsLong(PyList_GetItem(input_list,i));
    int new_len = compress_0_c(values,(int)len,out);

    PyObject* result = PyList_New(new_len);
    for(int i=0;i<new_len;i++) PyList_SetItem(result,i,PyLong_FromLong(out[i]));

    free(values); free(out);
    return result;
}

static PyObject* py_nCr(PyObject* self, PyObject* args){
    PyObject *n_obj, *k_obj;
    if(!PyArg_ParseTuple(args,"OO",&n_obj,&k_obj)) return NULL;

    PyObject* zero = PyLong_FromLong(0);
    PyObject* one = PyLong_FromLong(1);

    if(PyObject_RichCompareBool(k_obj, PyNumber_Subtract(n_obj,k_obj), Py_GT))
        k_obj = PyNumber_Subtract(n_obj,k_obj);

    PyObject* result = PyLong_FromLong(1);
    PyObject* i = PyLong_FromLong(1);

    while(PyObject_RichCompareBool(i, PyNumber_Add(k_obj,one), Py_LT)){
        PyObject* tmp1 = PyNumber_Subtract(n_obj, PyNumber_Subtract(k_obj,i));
        PyObject* tmp2 = PyNumber_Multiply(result, tmp1);
        Py_DECREF(tmp1); Py_DECREF(result);
        result = PyNumber_FloorDivide(tmp2,i);
        Py_DECREF(tmp2);

        PyObject* tmp_i = PyNumber_Add(i,one);
        Py_DECREF(i);
        i=tmp_i;
    }

    Py_DECREF(i); Py_DECREF(zero); Py_DECREF(one);
    return result;
}

static PyMethodDef NumberingMethods[] = {
    {"get_factors", py_get_factors, METH_VARARGS, "Return prime factors using Pollard Rho + Miller-Rabin."},
    {"compress_0", py_compress_0, METH_VARARGS, "Compress consecutive zeros."},
    {"nCr", py_nCr, METH_VARARGS, "Compute binomial coefficient (n choose k)."},
    {NULL,NULL,0,NULL}
};

static struct PyModuleDef numberingmodule = {
    PyModuleDef_HEAD_INIT,
    "numbering",
    NULL,
    -1,
    NumberingMethods
};

PyMODINIT_FUNC PyInit_numbering(void){ return PyModule_Create(&numberingmodule); }
