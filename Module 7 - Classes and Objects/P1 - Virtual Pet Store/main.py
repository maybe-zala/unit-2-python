from abc import ABC, abstractmethod
# ^^^^DO NOT REMOVE THIS IMPORT^^^^
class Pet(ABC):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__energy = 5
        self.__happiness = 5
        self.__hunger = 5

    def name(self):
        return self.__name

    def age(self):
        return self.__age

    def energy(self):
        return self.__energy

    def happiness(self):
        return self.__happiness

    def hunger(self):
        return self.__hunger

    def set_energy(self, value):
        self.energy = max(0, min(10, value))

    def set_happiness(self, value):
        self.happiness = max(0, min(10, value))

    def set_hunger(self, value):
        self.hunger = max(0, min(10, value))

    def eat(self):
        self.set_hunger(self.hunger() - 3)
        self.set_energy(self.energy() + 2)
        print(f"{self.name()} is eating...")

    def sleep(self):
        self.set_energy(self.energy() + 3)
        self.set_hunger(self.hunger() + 1)
        print(f"{self.name()} is sleeping...")

    def get_status(self):
        print(f"{self.name()}'s Status:")
        print(f"Age: {self.age()}")
        print(f"Hunger: {self.hunger()}/10")
        print(f"Energy: {self.energy()}/10")
        print(f"Happiness: {self.happiness()}/10")

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def play(self):
        pass

class Dog(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        print(f"{self.name()} says: Woof")

    def play(self):
        self.set_happiness(self.happiness() + 2)
        self.set_energy(self.energy() - 2)
        print(f"You play fetch with {self.name()}")

    def fetch(self):
        print(f"{self.name()} is happily fetching the ball!")
        self.set_happiness(self.happiness() + 1)
        self.set_energy(self.energy() - 1)

class Cat(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        print(f"{self.name()} says: Meow")

    def play(self):
        self.set_happiness(self.happiness() + 2)
        self.set_energy(self.energy() - 1)
        print(f"{self.name()} chases a laser pointer!")

    def scratch(self):
        print(f"{self.name()} is scratching the post (and not the furniture!).")
        self.set_happiness(self.happiness() + 1)

class Bird(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        print(f"{self.name()} says: Tweet Tweet")

    def play(self):
        self.set_happiness(self.happiness() + 3)
        self.set_energy(self.energy() - 3)
        print(f"{self.name()} flies in circles happily.")

    def sing(self):
        print(f"{self.name()} is singing a beautiful melody.")
        self.set_happiness(self.happiness() + 2)
        
def interact(pet: Pet):
    pet.speak()
    pet.play()
    pet.get_status()
    
pets = {}

def display_menu():
    print("\nMenu:")
    print("1. Adopt a pet")
    print("2. Feed pet")
    print("3. Play with pet")
    print("4. Let pet sleep")
    print("5. View pet status")
    print("6. Let pet speak")
    print("7. Interact")
    print("8. Quit")

def get_pet_choice():
    if not pets:
        print("No pets adopted yet. Adopt one first!")
        return None

    print("Your pets:")
    for i, name in enumerate(pets.keys()):
        print(f"{i+1}. {name}")

    while True:
        try:
            choice = int(input("Enter pet number: "))
            if 1 <= choice <= len(pets):
                return list(pets.values())[choice - 1]
            else:
                print("Invalid pet number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

print("Welcome to the Pet Simulator!")
while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Pet's name: ")
        age = int(input("Pet's age: "))
        pet = print("Select pet type: Dog, Cat, Bird")
        pet_type = input("Type: ").capitalize()

        if pet_type == "Dog":
            pets[name] = Dog(name, age)
        elif pet_type == "Cat":
            pets[name] = Cat(name, age)
        elif pet_type == "Bird":
            pets[name] = Bird(name, age)
        else:
            print("Invalid pet type.")
            continue
        print(f"{name} the {pet_type} has been adopted!")

    elif choice == '2':
        pet = get_pet_choice()
        if pet:
            pet.eat()

    elif choice == '3':
        pet = get_pet_choice()
        if pet:
            pet.play()

    elif choice == '4':
        pet = get_pet_choice()
        if pet:
            pet.sleep()

    elif choice == '5':
        pet = get_pet_choice()
        if pet:
            pet.get_status()

    elif choice == '6':
        pet = get_pet_choice()
        if pet:
            pet.speak()

    elif choice == '7':
        pet = get_pet_choice()
        if pet:
            interact(pet)

    elif choice == '8':
        print("Thanks for playing!")
        break

    else:
        print("Invalid choice. Please try again.")