#Create class and functions here.
class DogBoarder:
    

    def __init__(self, total_slots, daily_rate) -> None:
        self.dogs = []
        self.total_slots = total_slots
        self.daily_rate = daily_rate

    def all_dogs(self):
        return self.dogs
    def is_full(self):
        if len(self.dogs) == self.total_slots:
            return True
        else:
            return False

    def slots_occupied(self):
        return len(self.dogs)

    def board(self, dog, breed, name):
        if self.is_full() == False:
            self.dogs.append({"dog": dog, "breed": breed, "name": name})
            return (f"{dog} has been boarded.")
        elif self.is_full() == True:
            return ("Error: No available slots.")
    
    def pick_up(self, dog, breed, name, days):
        for x in self.dogs:
            if x["dog"] == dog and x["breed"] == breed and x["name"] == name:
                self.dogs.remove(x)
                return self.daily_rate * days
        if  0 < len(self.dogs):
            return ("Error: Dog not found.")
        else:
            return ("Error: No dogs boarded.")
            

                


# ^^^^^^^^^^^^^^^^^^^^^^^ Your code goes above ^^^^^^^^^^^^^^^^^^^^^^^
# VVVVVVVVVVVVVVVVVVV Do not edit below this line VVVVVVVVVVVVVVVVVVVVV
def display_menu():
    print("\nDog Boarder Menu:")
    print("1. Check if board is full")
    print("2. Check slots occupied")
    print("3. Board a dog")
    print("4. Pick up a dog")
    print("5. View all boarded dogs")
    print("6. Exit")

def main():
    # Initialize the DogBoarder with some slots and daily rate
    total_slots = int(input("Enter the total number of slots: "))
    daily_rate = float(input("Enter the daily rate per dog: "))
    boarder = DogBoarder(total_slots, daily_rate)

    while True:
        display_menu()
        option = input("Choose an option (1-6): ")
        if option == "1":
            if boarder.is_full():
                print("There are no slots available.")
            else:
                print("There are still slots available.")
        elif option == "2":
            print(f"Slots occupied: {boarder.slots_occupied()}/{boarder.total_slots}")
        elif option == "3":
            dog_name = input("Enter the dog's name: ")
            dog_breed = input("Enter the dog's breed: ")
            owner_name = input("Enter your name: ")
            board_dog = boarder.board(dog_name, dog_breed, owner_name)
            print(board_dog)
        elif option == "4":
            dog_name = input("Enter the dog's name: ")
            dog_breed = input("Enter the dog's breed: ")
            owner_name = input("Enter your name: ")
            days = int(input("Enter the number of days: "))
            pick_up_dog = boarder.pick_up(dog_name, dog_breed, owner_name, days)
            
            if type(pick_up_dog) == float:
                print(f"Total cost for {dog_name} is ${pick_up_dog:.2f}.")
            else:
                print(pick_up_dog)
        elif option == "5":
            if len(boarder.all_dogs()) == 0:
                print("No dogs are currently boarded.")
            else:
                print("\nCurrently boarded dogs:")
                for dog in boarder.all_dogs():
                    print(f"Name: {dog["dog"]}, Breed: {dog["breed"]}, Owner: {dog["name"]}")
        elif option == "6":
            print("Exiting the menu.")
            break
        else:
            print("Invalid input.")


if __name__ == "__main__":
    main()