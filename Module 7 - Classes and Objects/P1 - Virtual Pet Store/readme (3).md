# 🐾 Python OOP Assignment: Pet Simulator

## Objective

Build a **Pet Simulator** using all major Object-Oriented Programming (OOP) principles in Python.

Your implementation **must demonstrate**:
- Encapsulation
- Abstraction
- Inheritance
- Polymorphism

---

##  Overview

You will model different types of pets (Dog, Cat, Bird) with unique behaviors.
The program will let a user adopt, interact with, and monitor the well-being of one or more pets.

---

##  Requirements

### 🔹 1. Abstract Base Class: `Pet`
Create a class `Pet` using Python's `abc` module with the following features:

- **Private Attributes** (encapsulation):
  - `name`, `age`, `energy`, `happiness`, `hunger` 

- **Getter/Setter methods** to access and modify private attributes.
  ----- Getters -----
   get_name
   get_age
   get_energy
   get_happiness
   get_hunger

    ----- Setters -----
  set_energy
  set_happiness:
  set_hunger


- **Concrete Methods**:
  - `eat()` → decreases hunger by 3, increases energy by 2

  - `sleep()` → increases energy by 3 and increase hunger by 1

  - `get_status()` → prints current stats

  All animals should start with
  - 5 out of 10 energy, happiness, and hunger 


- **Abstract Methods** (abstraction):
  - `speak()` → must be implemented by all pets
    - Dog should say woof
    - Cat should say meow
    - Bird should say tweet tweet
  - `play()` → must be implemented by all pets
    - Dog: increase happiness by 2 and decreases energy by 2
    You play fetch with (Dog's name)
    - Cat: increase happiness by 2 and decreases energy by 1
    (Cat's name) chases a laser pointer!"
    - Bird: increase happiness by 3 and decreases energy by 3
    (Bird's name) flies in circles happily.


---

### 🔹 2. Subclasses: `Dog`, `Cat`, `Bird`
Each subclass must:
- Inherit from `Pet` (inheritance)
- Implement `speak()` and `play()`
- Add one **unique behavior**:
  - Dog: `fetch()`
  - Cat: `scratch()`
  - Bird: `sing()`

---

### 🔹 3. Polymorphism
Create a function:
```python
def interact(pet: Pet):
    pet.speak()
    pet.play()
    pet.get_status()
```
This function must work with any subclass of `Pet`.

---

### 🔹 4. Encapsulation
- All attributes should be **private**
- Use getter/setter methods to manage access

---

## Example
```console
Welcome to the Pet Simulator!

Menu:
1. Adopt a pet
2. Feed pet
3. Play with pet
4. Let pet sleep
5. View pet status
6. Let pet speak
7. Interact
8. Quit
Enter your choice: 1
Pet's name: Abby
Pet's age: 3
Select pet type: Dog, Cat, Bird
Type: Cat

Menu:
1. Adopt a pet
2. Feed pet
3. Play with pet
4. Let pet sleep
5. View pet status
6. Let pet speak
7. Interact
8. Quit
Enter your choice: 5

Abby's Status:
Age: 3
Hunger: 5/10
Energy: 5/10
Happiness: 5/10

Menu:
1. Adopt a pet
2. Feed pet
3. Play with pet
4. Let pet sleep
5. View pet status
6. Let pet speak
7. Interact
8. Quit
Enter your choice: 2
Abby is eating...

Menu:
1. Adopt a pet
2. Feed pet
3. Play with pet
4. Let pet sleep
5. View pet status
6. Let pet speak
7. Interact
8. Quit
Enter your choice: 3
Abby chases a laser pointer!

Menu:
1. Adopt a pet
2. Feed pet
3. Play with pet
4. Let pet sleep
5. View pet status
6. Let pet speak
7. Interact
8. Quit
Enter your choice: 4
Abby is sleeping...

Menu:
1. Adopt a pet
2. Feed pet
3. Play with pet
4. Let pet sleep
5. View pet status
6. Let pet speak
7. Interact
8. Quit
Enter your choice: 6
Abby says: Meow

Menu:
1. Adopt a pet
2.  pet
3. Play with pet
4. Let pet sleep
5. View pet status
6. Let pet speak
7. Interact
8. Quit
Enter your choice: 7
Abby says: Meow
Abby chases a laser pointer!

Abby's Status:
Age: 3
Hunger: 3/10
Energy: 8/10
Happiness: 9/10

Menu:
1. Adopt a pet
2. Feed pet
3. Play with pet
4. Let pet sleep
5. View pet status
6. Let pet speak
7. Interact 
8. Quit
Enter your choice: 5

Abby's Status:
Age: 3
Hunger: 3/10
Energy: 8/10
Happiness: 9/10

Menu:
1. Adopt a pet
2. Feed pet
3. Play with pet
4. Let pet sleep
5. View pet status
6. Let pet speak
7. Interact 
8. Quit
Enter your choice: 8
Thanks for playing!
```