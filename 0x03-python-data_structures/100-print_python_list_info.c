#include <stdlib.h>
#include "Python.h"

/**
 * print_python_list_info - prints information about a python list
 * @p: pointer to PyObject which is assumed is a list
 * Description: This function will grab the information stored in the
 * Python.h header file which is installed with the python3-dev.
 * This takes parts of the object and prints it to the screen.
 * the typedef information can be found at
 * https://docs.python.org/3/extending/newtypes.html
 * https://medium.com/geekculture/how-variables-are-
 * saved-in-python-and-rust-side-by-side-5-list-array-418012c01ccd
 *
 * Return: always void.
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *pythonList = NULL;
	ssize_t listLen = 0, i = 0;
	const char *elemType = NULL;

	listLen = PyList_Size(p);
	pythonList = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", listLen);
	printf("[*] Allocated = %ld\n", (signed long)(pythonList->allocated));
	while (i < listLen)
	{
		elemType = Py_TYPE(pythonList->ob_item[i])->tp_name;
		printf("Element %ld: %s\n", i, elemType);
		i++;
	}
}
