#include "Python.h"

/**
* print_python_bytes - print information about the python byte object
 * written in python
 *
 * @p: pointer to a python Object
 *
 * Return: Always void
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *pyByte = NULL;
	ssize_t i = 0;

	pyByte = (PyBytesObject *)p;
	printf("[.] bytes object info\n");
	if (PyBytes_Check(p) != 1)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", PyBytes_Size(p));
	printf("  type string: %s\n", pyByte->ob_sval);
	/* represent only the first 10 bytes on a string */
	if (PyBytes_Size(p) >= 10)
		printf("  first 10 bytes: ");
	else
		printf("  first %zu bytes: ", PyBytes_Size(p) + 1);
	while (i <= 10 && i <= PyBytes_Size(p))
	{
		printf("%02x ", (unsigned char)pyByte->ob_sval[i]);
		i++;
	}
	printf("\n");
}
/**
 * print_python_list - print information about the python list object
 * written in python
 * @p: pointer to a python Object
 * Return: Always void
 */
void print_python_list(PyObject *p)
{
	PyListObject *py_list = NULL;
	ssize_t list_len = 0;
	ssize_t i = 0;
	const char *element_type = NULL;

	list_len = PyList_Size(p);
	py_list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", list_len);
	printf("[*] Allocated = %ld\n", (signed long)(py_list->allocated));
	while (i < list_len)
	{
		element_type = py_list->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, element_type);
		if (!strcmp(element_type, "bytes"))
			print_python_bytes((PyObject *)py_list->ob_item[i]);
		i++;
	}
}
