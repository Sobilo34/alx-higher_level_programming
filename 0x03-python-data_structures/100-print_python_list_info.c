#include <Python.h>
#include <stdio.h>


/**
 * print_python_list_info - This is a function that prints
 * information about a Python list.
 * @p: A pointer to a PyObject that represents a Python list
 * Return: Void
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, alloc, a;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "Invalid Python list\n");
		return;
	}

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (a = 0; a < size; a++)
	{
		PyObject *element = PyList_GetItem(p, a);

		if (element != NULL)
			printf("Element %ld: %s\n", a, Py_TYPE(element)->tp_name);
		else
			fprintf(stderr, "Failed to retrieve element %ld\n", a);
	}
}

