#include <Python.h>
#include <stdio.h>

void print_bytes_info(PyObject *p);
void print_list_info(PyObject *p);

/**
 * print_bytes_info - THis is a function that Prints bytes object information
 * @p: The python bytes object
 */
void print_bytes_info(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	long int size, i, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = bytes->ob_base.ob_size;

	printf("  size: %ld\n", size);
	printf("  data: %s\n", bytes->ob_sval);

	limit = size >= 10 ? 10 : size + 1;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
		printf(" %02x", bytes->ob_sval[i] & 0xff);

	printf("\n");
}

/**
 * print_list_info - THis is the function that prints list information
 * @p: The python list object
 */
void print_list_info(PyObject *p)
{
	long int size, i;
	PyOject *element;

	printf("[*] Python list info\n");
	size = Py_SIZE(p);

	printf("[*] List size = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		element = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((element)->ob_type)->tp_name);

		if (PyBytes_Check(element))
			print_bytes_info(element);
	}
}

