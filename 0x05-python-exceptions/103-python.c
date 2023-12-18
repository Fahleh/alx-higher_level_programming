#include <Python.h>
#include <stdio.h>

/**
 * print_python_float - Provides the data of a PyFloatObject.
 * @pyt: PyObject
 */

void print_python_float(PyObject *pyt)
{
	double value = 0;
	char *string = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(pyt))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	value = ((PyFloatObject *)pyt)->ob_fval;
	string = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", string);
}


/**
 * print_python_bytes - Provides the data of a PyBytesObject
 * @pyt: PyObject
 */

void print_python_bytes(PyObject *pyt)
{
	Py_ssize_t size = 0, i = 0;
	char *string = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(pyt))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(pyt);
	printf("  size: %zd\n", size);
	string = (assert(PyBytes_Check(pyt)), (((PyBytesObject *)(pyt))->ob_sval));
	printf("  trying string: %s\n", string);
	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
	while (i < size + 1 && i < 10)
	{
		printf(" %02hhx", string[i]);
		i++;
	}
	printf("\n");
}

/**
 * print_python_list - Provides the data of a PyListObject
 * @pyt: PyObject
 */

void print_python_list(PyObject *pyt)
{
	Py_ssize_t size = 0;
	PyObject *element;
	int i = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(pyt))
	{
		size = PyList_GET_SIZE(pyt);
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)pyt)->allocated);
		while (i < size)
		{
			element = PyList_GET_ITEM(pyt, i);
			printf("Element %d: %s\n", i, element->ob_type->tp_name);
			if (PyBytes_Check(element))
				print_python_bytes(element);
			else if (PyFloat_Check(element))
				print_python_float(element);
			i++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
