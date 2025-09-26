# Dataclass - Benchmark 1: Home Alarm System

In this benchmark you will simulate a home alarm system. The alarm system is monitoring a single door that is either open or closed. The alarm is configured with a code at the beginning of the program. To turn the alarm off, the user must provide the correct code.

You must use a dataclass to represent the state of the alarm system, and you must implement each of the actions as functions. You should use the dataclass to store the `alarm code`, the `alarm state` (if the alarm is on or off), and the `door state` (if the door is opened or closed).

```
Alarm Code? 1234
Alarm: Off
Door: Closed
turn alarm [on], turn alarm [off], [open] door, [close] door, [quit]> on
Alarm: On
Door: Closed
turn alarm [on], turn alarm [off], [open] door, [close] door, [quit]> open
Alarm: *SIREN*
Door: Open
turn alarm [on], turn alarm [off], [open] door, [close] door, [quit]> off
Alarm Code? 1234
Alarm: Off
Door: Open
turn alarm [on], turn alarm [off], [open] door, [close] door, [quit]> close
Alarm: Off
Door: Closed
turn alarm [on], turn alarm [off], [open] door, [close] door, [quit]> quit
```

### Rubric

- [ ] The user configures the alarm's code at the beginning of the program
- [ ] The user can turn the alarm on
    - The door must be closed and the alarm must be off to turn the alarm on
- [ ] The user can turn the alarm off
    - The user must provide the correct code to turn it off
- [ ] The user can open the door
    - The alarm sirens if the door is opened while the alarm is on
- [ ] The user can close the door
- [ ] The user can quit the application
- [ ] State of the home alarm system modelled with a single dataclass.
- [ ] on, off, open, and close logic implemented in functions.
- [ ] You need input validation.

### Style Guide

- [ ] Variables should have meaningful names that accurately describe what they refer to.
- [ ] No sloppy/unnecessary/commented out code.
- [ ] Functions defined at the top of the file
- [ ] Application is implemented inside `main` function that is called inside `if __name__ == '__main__':`.
- [ ] Input is collected with input helper functions.
- [ ] Input helpers use validation functions that don't contain side effects and are tested thoroughly.
- [ ] Any significant pure logic is extracted and tested thoroughly.
- [ ] All functions have type annotations and pass the type checker.