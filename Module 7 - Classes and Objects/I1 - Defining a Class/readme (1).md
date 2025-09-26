# I1 - Defining a Class

Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Classes are essentially templates for creating your objects. Each class instance (object) can have attributes attached to maintain its state. Functions defined within a class are called methods, and they can modify their state. Methods are defined by the object's class.

The generalized form of class definition looks like this:
```
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```

Class definitions, like function definitions (def statements) must be executed before they have any effect.

The statements inside a class definition will usually be function definitions, but other statements are sometimes useful. The function definitions inside a class normally have a peculiar form of argument list — this is explained later.

Class objects support two kinds of operations: attribute references and instantiation. Attribute references will be discussed in the following sections. Class instantiation uses function notation. Just imagine that the class object is a parameter-less function that returns a new instance of the class. For example:

```
class SomeClass:
    """A simple example class"""
    i = 12345

x = SomeClass()
```

`x = SomeClass()` creates a new instance of the class and assigns this object to the local variable `x`.

You can find out more about class definition syntax by reading this section of [Python Documentation](https://docs.python.org/3/tutorial/classes.html).

## Task
Assign any value to the variable inside `MyClass` and create an object `my_class` of the class `MyClass()`. Run the code and see what happens! This should not throw an error. 