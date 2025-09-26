from dataclasses import dataclass


@dataclass
class Cat:
    name: str
    is_hungry: bool


def cat_sound(cat: Cat) -> str:
    #Makes cat noise based off if fed or not
    if cat.is_hungry:
        return "hiss"
    else:
        return "meow"


def feed_cat(cat: Cat) -> None:
    cat.is_hungry = False

def main():
    #Cat 1: Kit
    kit = Cat(name= "kit",is_hungry=True)
    #Cat 2: Kat
    kat = Cat(name= "kat",is_hungry=True)
    #First Cat Sounds
    print("Kit says",cat_sound(kit))
    print("Kat says",cat_sound(kat))

    while True:
        #Options to feed either cat or quit
        print("Feed [Kit], Feed [Kat], [quit]?")
        options = input("> ")
        if options.lower() == "kit":
            #feeds Kit
            feed_cat(kit)
            print("Feeding Kit")
            print("Kit says",cat_sound(kit))
            print("Kat says",cat_sound(kat))
        elif options.lower() == "kat":
            #feeds Kat
            feed_cat(kat)
            print("Feeding Kat")
            print("Kit says",cat_sound(kit))
            print("Kat says",cat_sound(kat))
        elif options.lower() == "quit":
            break
        else:
            #Invalid Input
            print("Please provide a valid cat name or quit.")


if __name__ == "__main__":
    main()
