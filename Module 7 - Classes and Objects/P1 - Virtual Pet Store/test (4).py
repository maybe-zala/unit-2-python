import subprocess
import platform
import difflib

# Defined test cases
# For each test case:
# The first element is the input string (with "\n" for each user input)
# The second element is the expected output string

test_cases = [
    # Test 1: Readme Example.
    (
        "1\nAbby\n3\nCat\n5\n2\n3\n4\n6\n7\n5\n8", 
        '''Welcome to the Pet Simulator!

Menu:
1. Adopt a pet
2. Feed pet
3. Play with pet
4. Let pet sleep
5. View pet status
6. Let pet speak
7. Interact
8. Quit
Enter your choice: Pet's name: Pet's age: Select pet type: Dog, Cat, Bird
Type: 
Menu:
1. Adopt a pet
2. Feed pet
3. Play with pet
4. Let pet sleep
5. View pet status
6. Let pet speak
7. Interact
8. Quit
Enter your choice: 
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
Enter your choice: Abby is eating...

Menu:
1. Adopt a pet
2. Feed pet
3. Play with pet
4. Let pet sleep
5. View pet status
6. Let pet speak
7. Interact
8. Quit
Enter your choice: Abby chases a laser pointer!

Menu:
1. Adopt a pet
2. Feed pet
3. Play with pet
4. Let pet sleep
5. View pet status
6. Let pet speak
7. Interact
8. Quit
Enter your choice: Abby is sleeping...

Menu:
1. Adopt a pet
2. Feed pet
3. Play with pet
4. Let pet sleep
5. View pet status
6. Let pet speak
7. Interact
8. Quit
Enter your choice: Abby says: Meow

Menu:
1. Adopt a pet
2. Feed pet
3. Play with pet
4. Let pet sleep
5. View pet status
6. Let pet speak
7. Interact
8. Quit
Enter your choice: Abby says: Meow
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
Enter your choice: 
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
Enter your choice: Thanks for playing!'''
    ),
    # Test 2: Checking Input Validation.
    (
        "2\n3\n4\n5\n6\n7\n1\nJessica\n1\nWolf\n5\n1\nJessica\n1\nDog\n5\n9\n8",
     '''Welcome to the Pet Simulator!

Menu:
1. Adopt a pet
2. Feed pet
3. Play with pet
4. Let pet sleep
5. View pet status
6. Let pet speak
7. Interact
8. Quit
Enter your choice: You haven't adopted a pet yet.

Menu:
1. Adopt a pet
2. Feed pet
3. Play with pet
4. Let pet sleep
5. View pet status
6. Let pet speak
7. Interact
8. Quit
Enter your choice: You haven't adopted a pet yet.

Menu:
1. Adopt a pet
2. Feed pet
3. Play with pet
4. Let pet sleep
5. View pet status
6. Let pet speak
7. Interact
8. Quit
Enter your choice: You haven't adopted a pet yet.

Menu:
1. Adopt a pet
2. Feed pet
3. Play with pet
4. Let pet sleep
5. View pet status
6. Let pet speak
7. Interact
8. Quit
Enter your choice: You haven't adopted a pet yet.

Menu:
1. Adopt a pet
2. Feed pet
3. Play with pet
4. Let pet sleep
5. View pet status
6. Let pet speak
7. Interact
8. Quit
Enter your choice: You haven't adopted a pet yet.

Menu:
1. Adopt a pet
2. Feed pet
3. Play with pet
4. Let pet sleep
5. View pet status
6. Let pet speak
7. Interact
8. Quit
Enter your choice: You haven't adopted a pet yet.

Menu:
1. Adopt a pet
2. Feed pet
3. Play with pet
4. Let pet sleep
5. View pet status
6. Let pet speak
7. Interact
8. Quit
Enter your choice: Pet's name: Pet's age: Select pet type: Dog, Cat, Bird
Type: Invalid pet type.

Menu:
1. Adopt a pet
2. Feed pet
3. Play with pet
4. Let pet sleep
5. View pet status
6. Let pet speak
7. Interact
8. Quit
Enter your choice: You haven't adopted a pet yet.

Menu:
1. Adopt a pet
2. Feed pet
3. Play with pet
4. Let pet sleep
5. View pet status
6. Let pet speak
7. Interact
8. Quit
Enter your choice: Pet's name: Pet's age: Select pet type: Dog, Cat, Bird
Type: 
Menu:
1. Adopt a pet
2. Feed pet
3. Play with pet
4. Let pet sleep
5. View pet status
6. Let pet speak
7. Interact
8. Quit
Enter your choice: 
Jessica's Status:
Age: 1
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
Enter your choice: Invalid choice. Try again.

Menu:
1. Adopt a pet
2. Feed pet
3. Play with pet
4. Let pet sleep
5. View pet status
6. Let pet speak
7. Interact
8. Quit
Enter your choice: Thanks for playing!'''
    ),
    # Test 3: Custom Test (only keeps up with the last adopted animal)
    (
     "1\nOreo\n4\nCat\n5\n3\n2\n5\n1\nPeaches\n5\nBird\n5\n8",
     '''Welcome to the Pet Simulator!

Menu:
1. Adopt a pet
2. Feed pet
3. Play with pet
4. Let pet sleep
5. View pet status
6. Let pet speak
7. Interact
8. Quit
Enter your choice: Pet's name: Pet's age: Select pet type: Dog, Cat, Bird
Type: 
Menu:
1. Adopt a pet
2. Feed pet
3. Play with pet
4. Let pet sleep
5. View pet status
6. Let pet speak
7. Interact
8. Quit
Enter your choice: 
Oreo's Status:
Age: 4
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
Enter your choice: Oreo chases a laser pointer!

Menu:
1. Adopt a pet
2. Feed pet
3. Play with pet
4. Let pet sleep
5. View pet status
6. Let pet speak
7. Interact
8. Quit
Enter your choice: Oreo is eating...

Menu:
1. Adopt a pet
2. Feed pet
3. Play with pet
4. Let pet sleep
5. View pet status
6. Let pet speak
7. Interact
8. Quit
Enter your choice: 
Oreo's Status:
Age: 4
Hunger: 2/10
Energy: 6/10
Happiness: 7/10

Menu:
1. Adopt a pet
2. Feed pet
3. Play with pet
4. Let pet sleep
5. View pet status
6. Let pet speak
7. Interact
8. Quit
Enter your choice: Pet's name: Pet's age: Select pet type: Dog, Cat, Bird
Type: 
Menu:
1. Adopt a pet
2. Feed pet
3. Play with pet
4. Let pet sleep
5. View pet status
6. Let pet speak
7. Interact
8. Quit
Enter your choice: 
Peaches's Status:
Age: 5
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
Enter your choice: Thanks for playing!'''
    )
]

# Run test cases
for idx, (input_data, expected_output) in enumerate(test_cases, 1):
    print(f"Running Test Case {idx}:")
    
    os_name = platform.system()
    python_command = 'python3' if os_name == 'Darwin' or os_name =='Linux' else 'python'
    
    # Run the main.py file
    process = subprocess.Popen(
        [python_command, 'main.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    output, _ = process.communicate(input=input_data)
    output = output.strip()

    if output == expected_output:
        print("Test Passed!\n")
    else:
        print("Test Failed!")
        diff = difflib.unified_diff(
            expected_output.splitlines(),
            output.splitlines(),
            lineterm=''
        )
        print("🔍 Difference:")
        print('\n'.join(diff))