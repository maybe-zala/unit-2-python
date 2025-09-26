# Intro 1: Using a Dataclass

In this exercise, you will learn to use a provided dataclass by instantiating and using new instances of the dataclass. I have provided you a `Cat` dataclass, a `cat_sound` function, and a `feed_cat` function. Your job is to use these tools to create the application described below.

In this application, you are managing two `Cat`s. One should be named Kit, and the other should be named Kat. At the beginning of the application, they should both be hungry. You should ask the user to feed one of the cats or quit the program. 

Example:

```
Kit says hiss
Kat says hiss
Feed [Kit], Feed [Kat], [quit]?
> hello
Please provide a valid cat name or quit.
Feed [Kit], Feed [Kat], [quit]?
> Kit
Feeding Kit
Kit says meow
Kat says hiss
Feed [Kit], Feed [Kat], [quit]?
> Kit
Feeding Kit
Kit says meow
Kat says hiss
Feed [Kit], Feed [Kat], [quit]?
> Kat
Feeding Kat
Kit says meow
Kat says meow
Feed [Kit], Feed [Kat], [quit]?
> Kit
Feeding Kit
Kit says meow
Kat says meow
Feed [Kit], Feed [Kat], [quit]?
> quit
```

### Rubric

- [ ] User can feed Kit
- [ ] User can feed Kat
- [ ] User can quit
- [ ] Code uses `Cat`, `cat_sound`, and `feed_cat` appropriately

### Style Guide
- [ ] Appropriate and meaningful comments
- [ ] Code should be formatted with the replit auto-formatter.
- [ ] Variables should have meaningful names that accurately describe what they refer to.
- [ ] No sloppy/unnecessary/commented out code.
- [ ] Functions defined at the top of the file
- [ ] Application is implemented inside `main` function that is called inside `if __name__ == '__main__':`.
- [ ] Input is collected with input helper functions.
- [ ] Input helpers use validation functions that don't contain side effects and are tested thoroughly.
- [ ] Any significant pure logic is extracted and tested thoroughly.
- [ ] All functions have type annotations and pass the type checker. 