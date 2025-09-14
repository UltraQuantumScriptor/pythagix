#include <Python.h>

static PyObject* py_product(PyObject* self, PyObject* args) {
    PyObject* input_list;

    if (!PyArg_ParseTuple(args, "O!", &PyList_Type, &input_list)) {
        return NULL;
    }

    Py_ssize_t size = PyList_Size(input_list);
    if (size == 0) {
        return PyLong_FromLong(1);
    }

    PyObject* result = PyList_GetItem(input_list, 0);
    Py_INCREF(result);

    for (Py_ssize_t i = 1; i < size; i++) {
        PyObject* item = PyList_GetItem(input_list, i);
        PyObject* temp = PyNumber_Multiply(result, item);
        Py_DECREF(result);
        result = temp;

        if (!result) {
            return NULL;
        }
    }

    return result;
}

static PyMethodDef StatMethods[] = {
    {"product", py_product, METH_VARARGS, "Multiply all numbers in a list. Returns 1 if empty."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef statmodule = {
    PyModuleDef_HEAD_INIT,
    "stat",   
    NULL,
    -1,          
    StatMethods
};

// Module init function
PyMODINIT_FUNC PyInit_stat(void) {
    return PyModule_Create(&statmodule);
}
