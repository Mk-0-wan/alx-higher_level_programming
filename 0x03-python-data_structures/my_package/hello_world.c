#include <stdio.h>
#include <C:\Users\Administrator\AppData\Local\Programs\Python\Python311\include\Python.h>

/**
 * STATIC PYOBJECT FILE WRITTEN IN C
 * STATIC CHAR FUNCTION WHICH DEFINES THE FUNCTION
 * STATIC PYMETHODEF WHICH DEFINES THE CFUNCTION
 * 
*/

static PyObject* hello_world()
{
    puts("Hello world, with <3 from c");
    Py_RETURN_NONE; /*PyObject macro for None */
}

static char HelloWorldFunctionDocs[] =
    "prints 'Hello, world' to the screen, from C";

static PyMethodDef MethodTable[] = {
    {
        "hello_world", /*CHAR POINTER TO THE NAME OF THE FUNCTION*/
        (PyCFunction)hello_world, /*(PyCFunction) parsed method written in c*/
        METH_NOARGS,/*CALLING CONVECTION OF THE FUNCTION*/
        HelloWorldFunctionDocs/*CHAR POINTER TO THE DOCS OF THE FUNCTION*/
    },
    {NULL, }
};

static char HelloWorldModuleDocs[] = 
    "Module documentation for 'Hello World'";

static struct PyModuleDef HelloWorld = {
    PyModuleDef_HEAD_INIT,
    "hello_world",
    HelloWorldModuleDocs,
    -1,
    MethodTable
};

PyMODINIT_FUNC PyInit_hello_world()
{
    return PyModule_Create(&HelloWorld);
}