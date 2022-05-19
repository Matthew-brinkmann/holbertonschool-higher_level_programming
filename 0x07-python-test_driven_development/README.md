# Readme for project 0x07. Python - Test-driven development
## By Matthew Brinkmann

### About the project
We are creating tests for functions to ensure that the functions are performing correctly


### :microscope: Tests ran using the following

```
python3 -m doctest ./tests/*
```

### :books: All modules and functions require documentation

```
python3 -c 'print(__import__("my_module").__doc__)'
```
```
python3 -c 'print(__import__("my_module").my_function.__doc__)'
```
## :computer: Technical

* [Ubuntu 20.04 LTS] - operating system

* python3 (version 3.8.5)

* compliant with pycodestyle (version 2.8.*)

## :pushpin: Functions

* **def add_integer(a, b=98):**
  * Function that adds 2 integers

* **def matrix_divided(matrix, div):**
  * Function that divides all elements of a matrix.

* **def say_my_name(first_name, last_name=""):**
  * Function that prints My name is <first name> <last name>

* **def print_square(size):**
  * Function that prints a square with the character #

* **def text_indentation(text):**
  * Function that prints a text with 2 new lines after each of these characters: ., ? and :

* **def max_integer(list=[]):**
  * Function to find and return the max integer in a list of integers
  * Tests are created using the UNITTEST module

:heavy_exclamation_mark: all tests will test that there is documentation for module and functions.

:heavy_exclamation_mark: Tests are created using the docutest module unless otherwise stated.

:heavy_exclamation_mark: Tests are stored in the directory /tests
