As your program gets longer, you may want to split it into several files for easier maintenance. You may also want to use a handy function that you’ve written in several programs without copying its definition into each of them.

Modules in Python are simply Python files with the .py extension containing Python definitions and statements. Modules are imported from other modules using the import keyword and the file name without the extension .py.

Let's say you wrote a script called my_funcs.py with a bunch of functions (func1, func2, etc.). Now, if you want to use those in another script that is placed in the same directory, you can do import my_funcs. This does not import the names of the functions defined in my_funcs directly, but using the module name, you can now access the functions, for example:

my_funcs.func1()
Modules can import other modules. It is customary but not required to place all import statements at the beginning of a module.



## Task
Your task is to import the module calculator and create an instance of the class Calculator (calc). Use the add method defined in Calculator in a loop to add up numbers from 0 to 99.


