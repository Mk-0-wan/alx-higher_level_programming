#include <stdlib.h>
#include "Python.h"

/**
 * print_python_list_info - prints information about a python list object
 * @p: pointer to the PyObject
 *
 * Return: always void.
 */

void print_python_list_info(PyObject *p)
{
	PyListObject *py_list = NULL;
	ssize_t list_len = 0;
	ssize_t i = 0;
	const char *element_type = NULL;

	list_len = PyList_Size(p);
	py_list = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", list_len);
	printf("[*] Allocated = %ld\n", (signed long)(py_list->allocated));
	while (i < list_len)
	{
		element_type = Py_TYPE(py_list->ob_item[i])->tp_name;
		printf("Element %ld: %s\n", i, element_type);
		i++;
	}
}
