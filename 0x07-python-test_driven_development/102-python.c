#include "Python.h"

/**
 * print_python_string - This is a function that prints info about Python strings
 * @p: This is a pointer to a PyObject representing a Python string object
 */

void print_python_string(PyObject *p)
{
	const char *string_input;
	long int length;

	fflush(stdout);

	printf("[.] string object info\n");

	string_input = p->ob_type->tp_name;

	if (strcmp(string_input, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	length = ((PyASCIIObject *)(p))->length;

	if (PyUnicode_IS_COMPACT_ASCII(p))
	{
		printf("  type: compact ascii\n");
	}
	else
	{
		printf("  type: compact unicode object\n");
	}

	printf("  length: %ld\n", length);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}
