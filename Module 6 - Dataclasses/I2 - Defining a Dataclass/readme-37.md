# Data - Intro 2: Defining a Dataclass

In this exercise, you will swap roles from Intro 1. I have provided the `main` function and input helpers. Your job is to implement `Dog`, `dog_sound`, and `play_with_dog` so that `main` can do its job.

- `Dog` should have three fields:
    - `name`: A string representing the dog's name
    - `weight`: An integer representing the dog's weight in pounds
    - `is_tired`: A boolean representing whether or not the dog is tired
- `dog_sound`
    - 1 argument: A `Dog`
    - Returns a string representing the sound that the provided dog is making.
        - If the dog is tired, it should return `"zzzzz"`
        - If the dog is big (at least 50 pounds), it should return `"RUFF RUFF"`
        - Otherwise, it should return `"yip yip yip"`
- `play_with_dog`
    - 1 argument: A `Dog`
    - It should return `None`
    - It should make the provided `Dog` tired

Example:

```
Fido says yip yip yip
Rufus says RUFF RUFF
Big Stuff says yip yip yip
Play with [Fido], [Rufus], [Big Stuff], or [quit]?
> Big Stuff
Playing with Big Stuff
Fido says yip yip yip
Rufus says RUFF RUFF
Big Stuff says zzzzz
Play with [Fido], [Rufus], [Big Stuff], or [quit]?
> aoeusnth
Please provide a valid dog name or quit.
Play with [Fido], [Rufus], [Big Stuff], or [quit]?
> Fido
Playing with Fido
Fido says zzzzz
Rufus says RUFF RUFF
Big Stuff says zzzzz
Play with [Fido], [Rufus], [Big Stuff], or [quit]?
> Rufus
Playing with Rufus
Fido says zzzzz
Rufus says zzzzz
Big Stuff says zzzzz
Play with [Fido], [Rufus], [Big Stuff], or [quit]?
> Fido
Playing with Fido
Fido says zzzzz
Rufus says zzzzz
Big Stuff says zzzzz
Play with [Fido], [Rufus], [Big Stuff], or [quit]?
> quit
```

### Rubric

- [ ] `Dog` implemented correctly and tested
- [ ] `dog_sound` implemented correctly and tested
- [ ] `play_with_dog` implemented correctly and tested

### Style Guide

- [ ] Variables should have meaningful names that accurately describe what they refer to.
- [ ] No sloppy/unnecessary/commented out code.
- [ ] Functions defined at the top of the file
- [ ] Application is implemented inside `main` function that is called inside `if __name__ == '__main__':`.
- [ ] Input is collected with input helper functions.
- [ ] Input helpers use validation functions that don't contain side effects and are tested thoroughly.
- [ ] Any significant pure logic is extracted and tested thoroughly.
- [ ] All functions have type annotations and pass the type checker.