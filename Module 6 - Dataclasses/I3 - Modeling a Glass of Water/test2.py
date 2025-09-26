import subprocess
import platform
import difflib

# Defined test cases
# For each test case:
# The first element is the input string (with "\n" for each user input)
# The second element is the expected output string

test_cases = [
    (
        "15\nin\n5\nin\n20\nout\n3\nin\n5\nout\n100\nquit", 
        '''Capacity? Glass capacity: 15
Glass amount: 0
Pour [in], pour [out], or [quit]? Amount? Glass capacity: 15
Glass amount: 5
Pour [in], pour [out], or [quit]? Amount? Glass capacity: 15
Glass amount: 15
Pour [in], pour [out], or [quit]? Amount? Glass capacity: 15
Glass amount: 12
Pour [in], pour [out], or [quit]? Amount? Glass capacity: 15
Glass amount: 15
Pour [in], pour [out], or [quit]? Amount? Glass capacity: 15
Glass amount: 0
Pour [in], pour [out], or [quit]?'''
    ),
    (
        "15\nin\n5\nrestart\nquit", 
        '''Capacity? Glass capacity: 15
Glass amount: 0
Pour [in], pour [out], or [quit]? Amount? Glass capacity: 15
Glass amount: 5
Pour [in], pour [out], or [quit]? Invalid action. Please enter 'in', 'out', or 'quit'.
Glass capacity: 15
Glass amount: 5
Pour [in], pour [out], or [quit]?'''
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
        
        from dataclasses import dataclass
