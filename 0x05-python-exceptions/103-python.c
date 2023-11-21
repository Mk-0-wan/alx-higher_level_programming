#include "Python.h"

/**
 * print_python_bytes - Prints python Bytes objects
 * information
 * @p: A python object
 * Return: void
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
	printf("  trying string: %s\n", pyByte->ob_sval);

	if (PyBytes_Size(p) >= 10)
		printf("  first 10 bytes:");
	else
		printf("  first %zu bytes:", PyBytes_Size(p) + 1);
	while (i < 10 && i <= PyBytes_Size(p))
	{
		printf(" %02x", (unsigned char)(pyByte->ob_sval[i] & 0xff));
		i++;
	}
	printf("\n");
}

/**
 * print_python_float - Prints python float objects
 * information
 * @p: A python object
 * Return: void
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *pyFloat = NULL;

	pyFloat = (PyFloatObject *)p;
	printf("[.] float object info\n");
	if (PyFloat_Check(p) != 1)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	/* check on how to get the value from it */
	if (PyFloat_Check(p) && pyFloat)
	{
		printf("  value: %s\n",
			PyOS_double_to_string(pyFloat->ob_fval, 'g', 16,
				Py_DTSF_ADD_DOT_0, NULL));
		fflush(stdout);
	}
}

/**
 * print_python_list - Prints python list object
 * information
 * @p: A python Object
 * Return: void
 */
void print_python_list(PyObject *p)
{
	PyListObject *py_list = NULL;
	ssize_t list_len = 0;
	ssize_t i = 0;
	const char *element_type = NULL;

	py_list = (PyListObject *)p;
	list_len = py_list->ob_base.ob_size;

	printf("[*] Python list info\n");
	if (PyList_Check(p) != 1)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", list_len);
	printf("[*] Allocated = %ld\n", (signed long)(py_list->allocated));
	while (i < list_len)
	{
		element_type = py_list->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, element_type);
		if (!strcmp(element_type, "bytes"))
			print_python_bytes((PyObject *)py_list->ob_item[i]);
		else if (!strcmp(element_type, "float"))
			print_python_float((PyObject *)py_list->ob_item[i]);
		i++;
	}
}

