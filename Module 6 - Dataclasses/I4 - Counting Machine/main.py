from dataclasses import dataclass

@dataclass
class Counter:
    number : int = 0

def inc(counter: Counter) -> None:
    counter.number += 1


def dec(counter: Counter) -> None:
    counter.number -= 1






def main():
    counter = Counter()
    while True:
        print(f"Counter: {counter.number}")
        options = input("[inc], [dec], [quit]> ")
        if options == "inc":
            inc(counter)
        elif options == "dec":
            dec(counter)
        elif options == "quit":
            break
        else:
            print("Invalid action.")
if __name__ == "__main__":
    main()