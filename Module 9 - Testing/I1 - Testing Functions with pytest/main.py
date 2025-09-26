midgard_INFO = """Or Middle Earth, is the realm inhabited by humans. Created from the body of the giant Ymir, Midgard’s land, oceans, mountains, and trees were formed from his flesh, blood, bones, and hair, respectively. The sky is Ymir’s skull, held up by four dwarfs. Midgard is connected to Asgard, the gods’ realm, by the rainbow bridge Bifrost, and lies between the icy Niflheim and fiery Muspelheim.

You can go to: [Q to quit]
- Alfheim
- Helheim
- Jötunheim
- Muspelheim
- Niflheim
"""

alfheim_INFO = """Also known as Álfheimr, is the realm of the light elves, or Ljósálfar. This enchanting world is known for its radiant beauty and is ruled by the god Freyr, who was gifted Alfheim as a tooth-gift in his youth. The light elves, renowned for their wisdom and grace, inhabit this realm, which is often depicted as being high up in the heavens, superior to the earthly realm but below Asgard, the home of the gods

You can go to: [Q to quit]
- Helheim
- Jötunheim
- Muspelheim
- Niflheim
- Midgard
"""

helheim_INFO = """Also known as Hel, is the underworld ruled by the goddess Hel, daughter of Loki and the giantess Angrboda. This cold, dark, and misty realm is where souls who die of old age, illness, or other natural causes reside. Located in the north, Helheim is a place of repose rather than torment, though it is often depicted as a grim and shadowy underworld. The entrance to Helheim is guarded by a giantess named Garm, ensuring that only the dead may enter

You can go to: [Q to quit]
- Jötunheim
- Muspelheim
- Niflheim
- Midgard
- Alfheim
"""

jotunheim_INFO = """Also known as Jötunheimr, is the realm of the jötnar (giants). It is a wild and untamed land, often depicted as being in stark contrast to the orderly world of the gods in Asgard. Jotunheim is home to various giants and trolls, and its chaotic nature ensures constant conflict with the gods. Notable locations within Jotunheim include Utgard, a massive castle, and Mimir’s well. The realm is characterized by its rugged landscapes and is often associated with lawlessness and destruction

You can go to: [Q to quit]
- Muspelheim
- Niflheim
- Midgard
- Alfheim
- Helheim
"""

muspelheim_INFO = """Is a realm of fire and heat. It is described as a hot, glowing land, home to the fire giants and ruled by the formidable fire giant Surtr, who wields a flaming sword. Muspelheim plays a crucial role in both the creation and destruction narratives of Norse mythology. At the beginning of time, the heat from Muspelheim met the ice from Niflheim in the primordial void of Ginnungagap, leading to the creation of the first being, Ymir. During Ragnarök, the end of the world, the fire giants from Muspelheim, led by Surtr, will ride forth to battle the gods, ultimately leading to the world’s fiery destruction

You can go to: [Q to quit]
- Niflheim
- Midgard
- Alfheim
- Helheim 
- Jötunheim
"""

niflheim_INFO = """Is a realm of primordial ice, cold, and mist. It is one of the nine worlds and is often depicted as a dark, foggy, and frigid place. Niflheim is home to the well of Hvergelmir, from which numerous rivers flow, and it is ruled by the goddess Hel, who oversees the realm of the dead. This icy domain is situated beneath one of the roots of Yggdrasil, the world tree. In the Norse creation myth, Niflheim’s icy mists met the fiery heat of Muspelheim in the void of Ginnungagap, leading to the creation of the first being, Ymir. Niflheim is often associated with death and the afterlife, particularly for those who did not die a heroic death in battle

You can go to: [Q to quit]
- Midgard 
- Alfheim
- Helheim 
- Jötunheim
- Muspelheim
"""


def destinations(location) -> str:
    if location == "Midgard":
        return midgard_INFO
    elif location == "Alfheim":
        return alfheim_INFO
    elif location == "Helheim":
        return helheim_INFO
    elif location == "Jotunheim":
        return jotunheim_INFO
    elif location == "Muspelheim":
        return muspelheim_INFO
    elif location == "Niflheim":
        return niflheim_INFO


def adventure(location) -> bool:
    return location == "Midgard" or location == "Alfheim" or location == "Helheim" or location == "Jotunheim" or location == "Muspelheim" or location == "Niflheim"


def main() -> None:
    print("Please make sure you capitalize or, you will have to return to Midgard to continue with your adventure through the realms!\n You are starting in the Mystical Gateway!")
    current_location = "Midgard"
    while True:
        print(f"You are in {current_location.title()}")
        print(destinations(current_location))
        location = input("> ").capitalize()
        if location == "Q":
            break
        elif location == current_location:
            print(f"Your already in {location.title()}")
        elif adventure(location) == True:
            current_location = location
        else:
            print(f"You cannot go to {location} from {current_location}!")

if __name__ == "__main__":
    main()