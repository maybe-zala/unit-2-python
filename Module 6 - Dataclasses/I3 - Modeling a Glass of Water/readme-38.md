# Data - Intro 3 - Modeling a Glass of Water

In this exercise you will implement a dataclass and application that model a glass of water that can be filled up and poured out.

The dataclass that you implement should be named `Glass`. It should have `capacity` and `current_amount` of water in it. You should define the following methods to operate on instances of your dataclass:

- `pour_in`
    - Two arguments: one for the `Glass` instance and one for the amount of water being poured in.
    - Doesn't return anything.
    - Mutates the provided `Glass` instance by adding the provided amount of water without exceeding the `Glass`'s capacity.

- `pour_out`
    - Two arguments: one for the `Glass` instance and one for the amount of water being poured out.
    - Doesn't return anything.
    - Mutates the provided `Glass` instance by subtracting the provided amount of water without going below 0.


Your application should allow the user to pour into and out of the glass. At the start of the program, the user should be able to specify the capacity of the glass.

Example:
```
Capacity? 15
Glass capacity: 15
Glass amount: 0
Pour [in], pour [out], or [quit]? in
Amount? 5
Glass capacity: 15
Glass amount: 5
Amount? 20
Glass capacity: 15
Glass amount: 15
Pour [in], pour [out], or [quit]? out
Amount? 3
Glass capacity: 15
Glass amount: 12
Pour [in], pour [out], or [quit]? in
Amount? 5
Glass capacity: 15
Glass amount: 15
Pour [in], pour [out], or [quit]? out
Amount? 100
Glass capacity: 15
Glass amount: 0
Pour [in], pour [out], or [quit]? quit
```

### Rubric

- [ ] `Glass` is defined correctly
- [ ] `pour_in` is defined correctly
- [ ] `pour_out` is defined correctly
- [ ] User can specify the capacity of the glass being used.
- [ ] User can pour water into the glass
- [ ] User can pour water out of the glass
- [ ] User can quit
- [ ] You have input Validation
- [ ] The state of the glass is shown before each action
- [ ] Both test.py and test2.py pass

### Style Guide

- [ ] Variables should have meaningful names that accurately describe what they refer to.
- [ ] No sloppy/unnecessary/commented out code.
- [ ] Functions defined at the top of the file
- [ ] Application is implemented inside `main` function that is called inside `if __name__ == '__main__':`.
- [ ] Any significant pure logic is extracted and tested thoroughly.
- [ ] All functions have type annotations and pass the type checker.