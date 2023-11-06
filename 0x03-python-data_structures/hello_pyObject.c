#include "Python.h"

void print_hello_world(void)
{
	PyObject *pObj = NULL;

	pObj = PyBytes_FromString("Hello world\n");
	PyObject_Print(pLast, stdout, 0);
	Py_DECREF(pObj);
}
