# Benchmark - Class Dog Boarder
Your job is to create a *DogBoarder* class that manages the boarding process for dogs at a kennel. It allows for tracking the number of occupied slots, boarding dogs, and calculating the cost of boarding based on a daily rate. This class ensures that the number of dogs does not exceed the available slots and provides functionality to calculate the total cost when a dog is picked up. Also you have provided test cases to help check your methods.

## You should have the following methods:
```
- all_dogs() - Returns the collection of all dogs.

- is_full() - Check if the boarding facility is full.
    - Returns (bool): True if the boarding facility is full, False otherwise.

- slots_occupied() - Get the number of currently occupied slots.
    - Returns (int): The number of slots currently occupied.

- board(dog, breed, name) - Board a dog if there is an available slot. Store the dog as a dictionary (e.g., {"dog": name, "breed": breed, "name": owner}) into the list of all dogs.
    - dog (str): Identifier for the dog (e.g., name or ID).
    - breed (str): Breed of the dog.
    - name (str): Name of the owner.
    - Returns (str): A message if they boarded the dog or there are no available slots.

- pick_up(dog, breed, name, days) - Pick up a dog and calculate the total cost based on the number of days stayed.
    - dog (str): Identifier for the dog (e.g., name or ID).
    - breed (str): Breed of the dog.
    - name (str): Name of the dog.
    - days (int): Number of days the dog has been boarded.
    - Returns (str or int): The total cost of boarding the dog for the specified number of days if they are already boarded. Otherwise, it will return an error message.
```


## Example 1
```
Enter the total number of slots: 10
Enter the daily rate per dog: 5

Dog Boarder Menu:
1. Check if board is full
2. Check slots occupied
3. Board a dog
4. Pick up a dog
5. View all boarded dogs
6. Exit
Choose an option (1-6): 1
There are still slots available.

Dog Boarder Menu:
1. Check if board is full
2. Check slots occupied
3. Board a dog
4. Pick up a dog
5. View all boarded dogs
6. Exit
Choose an option (1-6): 2
Slots occupied: 0/10

Dog Boarder Menu:
1. Check if board is full
2. Check slots occupied
3. Board a dog
4. Pick up a dog
5. View all boarded dogs
6. Exit
Choose an option (1-6): 3
Enter the dog's name: Sam 
Enter the dog's breed: Pit Bull
Enter your name: Brittany
Sam has been boarded.

Dog Boarder Menu:
1. Check if board is full
2. Check slots occupied
3. Board a dog
4. Pick up a dog
5. View all boarded dogs
6. Exit
Choose an option (1-6): 4
Enter the dog's name: Mark
Enter the dog's breed: Jack Russell
Enter your name: RJay
Enter the number of days: 4
Error: Dog not found.

Dog Boarder Menu:
1. Check if board is full
2. Check slots occupied
3. Board a dog
4. Pick up a dog
5. View all boarded dogs
6. Exit
Choose an option (1-6): 5

Currently boarded dogs:
Name: Sam, Breed: Pit Bull, Owner: Brittany

Dog Boarder Menu:
1. Check if board is full
2. Check slots occupied
3. Board a dog
4. Pick up a dog
5. View all boarded dogs
6. Exit
Choose an option (1-6): 4
Enter the dog's name: Sam
Enter the dog's breed: Pit Bull
Enter your name: Brittany
Enter the number of days: 3
Total cost for Sam is $15.00.

Dog Boarder Menu:
1. Check if board is full
2. Check slots occupied
3. Board a dog
4. Pick up a dog
5. View all boarded dogs
6. Exit
Choose an option (1-6): 5
No dogs are currently boarded.

Dog Boarder Menu:
1. Check if board is full
2. Check slots occupied
3. Board a dog
4. Pick up a dog
5. View all boarded dogs
6. Exit
Choose an option (1-6): 6
Exiting the menu.
```

## Example 2
```
Enter the total number of slots: 1
Enter the daily rate per dog: 2

Dog Boarder Menu:
1. Check if board is full
2. Check slots occupied
3. Board a dog
4. Pick up a dog
5. View all boarded dogs
6. Exit
Choose an option (1-6): 3
Enter the dog's name: Red 
Enter the dog's breed: Red Heeler/Australian Sheppard
Enter your name: RJay
Red has been boarded.

Dog Boarder Menu:
1. Check if board is full
2. Check slots occupied
3. Board a dog
4. Pick up a dog
5. View all boarded dogs
6. Exit
Choose an option (1-6): 3
Enter the dog's name: Bailey
Enter the dog's breed: Pomeranian
Enter your name: Samantha
Error: No available slots.

Dog Boarder Menu:
1. Check if board is full
2. Check slots occupied
3. Board a dog
4. Pick up a dog
5. View all boarded dogs
6. Exit
Choose an option (1-6): 2
Slots occupied: 1/1

Dog Boarder Menu:
1. Check if board is full
2. Check slots occupied
3. Board a dog
4. Pick up a dog
5. View all boarded dogs
6. Exit
Choose an option (1-6): 1
There are no slots available.

Dog Boarder Menu:
1. Check if board is full
2. Check slots occupied
3. Board a dog
4. Pick up a dog
5. View all boarded dogs
6. Exit
Choose an option (1-6): 5

Currently boarded dogs:
Name: Red, Breed: Red Heeler/Australian Sheppard, Owner: RJay

Dog Boarder Menu:
1. Check if board is full
2. Check slots occupied
3. Board a dog
4. Pick up a dog
5. View all boarded dogs
6. Exit
Choose an option (1-6): 6
Exiting the menu.
```

### Rubric
- [ ] Pass test.py file
- [ ] **DogBoarder** is a class (*NOT A DATACLASS*)