
# ^^^^^   Add your code above   ^^^^^
# vvvvv Don't change code below vvvvv


def input_dog_choice(dog1: Dog, dog2: Dog, dog3: Dog) -> Dog:
    while True:
        print(
            f"Play with [{dog1.name}], [{dog2.name}], [{dog3.name}], or [quit]?"
        )
        dog_choice = input("> ")
        if dog_choice == "quit":
            return None
        elif dog_choice == dog1.name:
            return dog1
        elif dog_choice == dog2.name:
            return dog2
        elif dog_choice == dog3.name:
            return dog3
        else:
            print("Please provide a valid dog name or quit.")


def main():
    dog1 = Dog("Fido", 30, False)
    dog2 = Dog("Rufus", 55, False)
    dog3 = Dog("Big Stuff", 7, False)

    while True:
        print(f"{dog1.name} says {dog_sound(dog1)}")
        print(f"{dog2.name} says {dog_sound(dog2)}")
        print(f"{dog3.name} says {dog_sound(dog3)}")
        dog_to_play_with = input_dog_choice(dog1, dog2, dog3)
        if dog_to_play_with is None:
            break

        print(f"Playing with {dog_to_play_with.name}")
        play_with_dog(dog_to_play_with)


if __name__ == "__main__":
    main()
