#include <Python.h>

/**
* print_python_list_info - Print basic info about Python lists
* @p: The Python object
*/
void print_python_list_info(PyObject *p)
{
int size = Py_SIZE(p);
int x;

printf("[*] Size of the Python List = %d\n", size);
printf("[*] Allocated = %li\n", ((PyListObject *) p)->allocated);
for (x = 0; x < size; x++)
printf("Element %d: %s\n", x,
Py_TYPE(PyList_GetItem(p, x))->tp_name);
}
