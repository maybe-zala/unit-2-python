# --------------------- Example ----------------------
import my_module

my_module.hello_world("John")
# --------------- Dont edit this above ---------------

# Import the module `calculator` here
import calculator

calc = calculator.Calculator()
for i in range(99):
    calc.add(1)
    # Use Calculator method `add` to add `i` to the current value.
    print(calc.get_current())