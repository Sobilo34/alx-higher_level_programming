#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - THis is the function that prints bytes info
 * @p: The Python obj
 * Return: return 0
 */
void print_python_bytes(PyObject *p)
{
	long int size, a;
	long int bound;
	char *input;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	input = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", input);

	if (size >= 10)
		bound = 10;
	else
		bound = size + 1;

	printf("  first %ld bytes:", bound);

	for (a = 0; a < bound; a++)
		if (input[a] >= 0)
			printf(" %02x", input[a]);
		else
			printf(" %02x", 256 + input[a]);
	printf("\n");
}

/**
 * print_python_list - This is the function that prints list information
 * @p: The python object
 * Return: It returns 0 always
 */
void print_python_list(PyObject *p)
{
	long int size, a;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (a = 0; a < size; a++)
	{
		obj = ((PyListObject *)p)->ob_item[a];
		printf("Element %ld: %s\n", a, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
