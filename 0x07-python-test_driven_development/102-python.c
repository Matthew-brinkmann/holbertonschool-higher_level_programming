#include <stdio.h>
#include "Python.h"

/**
 * print_python_string - prints information about a python string
 * @p: pointer to PyObject which is assumed is a string
 * Description: This function will grab the information stored in the
 * Python.h header file which is installed with the python3-dev.
 * This takes parts of the object and prints it to the screen.
 * the typedef information can be found at
 * https://medium.com/geekculture/how-variables-are-saved
 * -in-python-and-rust-side-by-side-4-str-string-e9b729682a2f
 *
 * Return: always void.
 */
void print_python_string(PyObject *p)
{
	char *strVal = NULL;
	ssize_t len = 0;
	int i;
	PyObject *str_ob = NULL;

	printf("[.] string object info\n");
	if (PyUnicode_Check(p) == 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	len = (ssize_t)PyUnicode_GET_LENGTH(p);

	str_ob = PyUnicode_AsUTF8String(p);
	strVal = PyBytes_AsString(str_ob);

	if (len == strlen(strVal))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", len);
	printf("  value: %s\n", strVal);
}
