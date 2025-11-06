#include <Python.h>
#include <stdbool.h>
#include <stdlib.h>

static PyObject* py_filter_primes(PyObject* self, PyObject* args){

    PyObject* input_list;
    int k = 5;
    if (!PyArg_ParseTuple(args,"O!|i",&PyList_Type,&input_list,&k)) return NULL;

    Py_ssize_t size = PyList_Size(input_list);
    PyObject* result = PyList_New(0);

    // Import your Python module pprime
    PyObject* py_module = PyImport_ImportModule("pprime");
    if (!py_module) return NULL;

    PyObject* py_is_prime = PyObject_GetAttrString(py_module, "is_prime");
    if (!py_is_prime) { Py_DECREF(py_module); return NULL; }

    for (Py_ssize_t i=0; i<size; i++){
        PyObject* item = PyList_GetItem(input_list,i);
        PyObject* args_tuple = Py_BuildValue("Oi", item, k);
        PyObject* res = PyObject_CallObject(py_is_prime, args_tuple);
        Py_DECREF(args_tuple);

        if (res == Py_True) {
            PyList_Append(result, item);
        }
        Py_XDECREF(res);
    }

    Py_DECREF(py_is_prime);
    Py_DECREF(py_module);
    return result;
}

static PyMethodDef PrimeMethods[] = {
    {"filter_primes", py_filter_primes, METH_VARARGS,"Filter primes from a list."},
    {NULL,NULL,0,NULL}
};

static struct PyModuleDef primemodule = {
    PyModuleDef_HEAD_INIT,
    "prime",
    NULL,
    -1,
    PrimeMethods,
};

PyMODINIT_FUNC PyInit_prime(void){
    return PyModule_Create(&primemodule);
}
