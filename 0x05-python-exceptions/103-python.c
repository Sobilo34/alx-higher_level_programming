#include <Python.h>

void ppython_list(PyObject *p);
void ppython_bytes(PyObject *p);
void ppython_float(PyObject *p);

/**
 * ppython_list - This funcion is to print basic info about Python lists
 * @p: A PyObject list object
 */
void ppython_list(PyObject *p)
{
	Py_ssize_t size, mem, a;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	mem = list->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", mem);

	for (a = 0; a < size; a++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", a, type);
		if (strcmp(type, "bytes") == 0)
			ppython_bytes(list->ob_item[a]);
		else if (strcmp(type, "float") == 0)
			ppython_float(list->ob_item[a]);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void ppython_bytes(PyObject *p)
{
	Py_ssize_t size, a;
	PyBytesObject *bytes = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld bytes: ", size);
	for (a = 0; a < size; a++)
	{
		printf("%02hhx", bytes->ob_sval[a]);
		if (a == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * ppython_float - This prints that basic info about Python float objects
 * @p: A PyObject float object
 */
void ppython_float(PyObject *p)
{
	char *bufa = NULL;

	PyFloatObject *float_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	bufa = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", bufa);
	PyMem_Free(bufa);
}
