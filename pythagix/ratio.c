#include <Python.h>

static PyObject* py_gcd(PyObject* a, PyObject* b){
    PyObject* zero = PyLong_FromLong(0);
    PyObject *tmp_a=Py_NewRef(a),*tmp_b=Py_NewRef(b),*t;
    while(PyObject_RichCompareBool(tmp_b, zero, Py_NE)){
        t = tmp_b; Py_INCREF(t);
        PyObject* mod = PyNumber_Remainder(tmp_a,tmp_b);
        Py_DECREF(tmp_a); tmp_a=tmp_b; tmp_b=mod;
        Py_DECREF(t);
    }
    Py_DECREF(tmp_b); Py_DECREF(zero);
    return tmp_a;
}

static PyObject* py_simplify_ratio(PyObject* self, PyObject* args){
    PyObject *a,*b;
    if(!PyArg_ParseTuple(args,"OO",&a,&b)) return NULL;

    if(PyObject_RichCompareBool(b, PyLong_FromLong(0), Py_EQ)){
        PyErr_SetString(PyExc_ZeroDivisionError,"Denominator must not be zero");
        return NULL;
    }
    if(PyObject_RichCompareBool(a, PyLong_FromLong(0), Py_EQ))
        return Py_BuildValue("OO", PyLong_FromLong(0), PyLong_FromLong(1));

    PyObject* g = py_gcd(a,b);
    PyObject* new_a = PyNumber_FloorDivide(a,g);
    PyObject* new_b = PyNumber_FloorDivide(b,g);
    Py_DECREF(g);

    if(PyObject_RichCompareBool(new_b, PyLong_FromLong(0), Py_LT)){
        PyObject* tmp = PyNumber_Negative(new_a); Py_DECREF(new_a); new_a=tmp;
        tmp = PyNumber_Negative(new_b); Py_DECREF(new_b); new_b=tmp;
    }
    return Py_BuildValue("OO", new_a,new_b);
}

static PyObject* py_is_equivalent(PyObject* self, PyObject* args){
    PyObject* tuple_of_ratios;
    if(!PyArg_ParseTuple(args,"O",&tuple_of_ratios)) return NULL;
    if(!PyTuple_Check(tuple_of_ratios)){PyErr_SetString(PyExc_TypeError,"Expected a tuple of ratios"); return NULL;}
    Py_ssize_t n = PyTuple_Size(tuple_of_ratios);
    if(n==0) Py_RETURN_TRUE;

    PyObject* first = PyTuple_GetItem(tuple_of_ratios,0);
    PyObject *base_a,*base_b;
    if(!PyArg_ParseTuple(first,"OO",&base_a,&base_b)) return NULL;
    PyObject* g = py_gcd(base_a,base_b);
    PyObject* a = PyNumber_FloorDivide(base_a,g);
    PyObject* b = PyNumber_FloorDivide(base_b,g);
    Py_DECREF(g);
    if(PyObject_RichCompareBool(b, PyLong_FromLong(0), Py_LT)){
        PyObject* tmp_a=PyNumber_Negative(a); Py_DECREF(a); a=tmp_a;
        PyObject* tmp_b=PyNumber_Negative(b); Py_DECREF(b); b=tmp_b;
    }

    for(Py_ssize_t i=1;i<n;i++){
        PyObject* ratio = PyTuple_GetItem(tuple_of_ratios,i);
        PyObject *cur_a,*cur_b;
        if(!PyArg_ParseTuple(ratio,"OO",&cur_a,&cur_b)) return NULL;

        g = py_gcd(cur_a,cur_b);
        PyObject* norm_a = PyNumber_FloorDivide(cur_a,g);
        PyObject* norm_b = PyNumber_FloorDivide(cur_b,g);
        Py_DECREF(g);
        if(PyObject_RichCompareBool(norm_b, PyLong_FromLong(0), Py_LT)){
            PyObject* tmp_a = PyNumber_Negative(norm_a); Py_DECREF(norm_a); norm_a=tmp_a;
            PyObject* tmp_b = PyNumber_Negative(norm_b); Py_DECREF(norm_b); norm_b=tmp_b;
        }

        if(!PyObject_RichCompareBool(a,norm_a,Py_EQ) || !PyObject_RichCompareBool(b,norm_b,Py_EQ)){Py_DECREF(norm_a); Py_DECREF(norm_b); Py_RETURN_FALSE;}
        Py_DECREF(norm_a); Py_DECREF(norm_b);
    }
    Py_RETURN_TRUE;
}

static PyMethodDef RatioMethods[] = {
    {"simplify_ratio", py_simplify_ratio, METH_VARARGS,"Simplify a ratio."},
    {"is_equivalent", py_is_equivalent, METH_VARARGS,"Check if all ratios in a tuple are equivalent."},
    {NULL,NULL,0,NULL}
};

static struct PyModuleDef ratiomodule = {
    PyModuleDef_HEAD_INIT,
    "ratio",
    NULL,
    -1,
    RatioMethods
};

PyMODINIT_FUNC PyInit_ratio(void){ return PyModule_Create(&ratiomodule); }
