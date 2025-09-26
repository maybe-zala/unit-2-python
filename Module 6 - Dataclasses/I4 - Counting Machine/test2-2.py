import subprocess
import platform
import difflib

# Defined test cases
# For each test case:
# The first element is the input string (with "\n" for each user input)
# The second element is the expected output string

test_cases = [
    (
        "inc\ninc\ninc\ninc\ndec\ndec\ndec\ndec\ndec\nquit", 
        '''Counter: 0
[inc], [dec], [quit]> Counter: 1
[inc], [dec], [quit]> Counter: 2
[inc], [dec], [quit]> Counter: 3
[inc], [dec], [quit]> Counter: 4
[inc], [dec], [quit]> Counter: 3
[inc], [dec], [quit]> Counter: 2
[inc], [dec], [quit]> Counter: 1
[inc], [dec], [quit]> Counter: 0
[inc], [dec], [quit]> Counter: -1
[inc], [dec], [quit]>'''
    ),
    (
        "inc\ninc\ndec\nincrease\ndecrease\nquit", 
        '''Counter: 0
[inc], [dec], [quit]> Counter: 1
[inc], [dec], [quit]> Counter: 2
[inc], [dec], [quit]> Counter: 1
[inc], [dec], [quit]> Invalid action.
Counter: 1
[inc], [dec], [quit]> Invalid action.
Counter: 1
[inc], [dec], [quit]>'''
    )
]

# Run test cases
for idx, (input_data, expected_output) in enumerate(test_cases, 1):
    print(f"Running Test Case {idx}:")
    
    os_name = platform.system()
    python_command = 'python3' if os_name == 'Darwin' else 'python'
    
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