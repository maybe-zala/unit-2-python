                       
import subprocess
import platform
import difflib

# Defined test cases
# For each test case:
# The first element is the input string (with "\n" for each user input)
# The second element is the expected output string

test_cases = [
    # Example test cases from readme.md
    (
        "1234\non\nopen\noff\n1234\nclose\nquit", 
        '''Alarm Code? Alarm: Off
Door: Closed
turn alarm [on], turn alarm [off], [open] door, [close] door, [quit]> Alarm: On
Door: Closed
turn alarm [on], turn alarm [off], [open] door, [close] door, [quit]> Alarm: *SIREN*
Door: Open
turn alarm [on], turn alarm [off], [open] door, [close] door, [quit]> Alarm Code? Alarm: Off
Door: Open
turn alarm [on], turn alarm [off], [open] door, [close] door, [quit]> Alarm: Off
Door: Closed
turn alarm [on], turn alarm [off], [open] door, [close] door, [quit]>'''
    ),
    # Additional test case
    (
        "1908\nopen\non\nclose\nclose\non\nclose\nopen\nclose\non\noff\n1234\noff\n1908\nopen\nclose\non\nopen\ngoodbye\nquit", 
        '''Alarm Code? Alarm: Off
Door: Closed
turn alarm [on], turn alarm [off], [open] door, [close] door, [quit]> Alarm: Off
Door: Open
turn alarm [on], turn alarm [off], [open] door, [close] door, [quit]> Alarm: Off
Door: Open
turn alarm [on], turn alarm [off], [open] door, [close] door, [quit]> Alarm: Off
Door: Closed
turn alarm [on], turn alarm [off], [open] door, [close] door, [quit]> Alarm: Off
Door: Closed
turn alarm [on], turn alarm [off], [open] door, [close] door, [quit]> Alarm: On
Door: Closed
turn alarm [on], turn alarm [off], [open] door, [close] door, [quit]> Alarm: On
Door: Closed
turn alarm [on], turn alarm [off], [open] door, [close] door, [quit]> Alarm: *SIREN*
Door: Open
turn alarm [on], turn alarm [off], [open] door, [close] door, [quit]> Alarm: *SIREN*
Door: Closed
turn alarm [on], turn alarm [off], [open] door, [close] door, [quit]> Alarm: *SIREN*
Door: Closed
turn alarm [on], turn alarm [off], [open] door, [close] door, [quit]> Alarm Code? Alarm: *SIREN*
Door: Closed
turn alarm [on], turn alarm [off], [open] door, [close] door, [quit]> Alarm Code? Alarm: Off
Door: Closed
turn alarm [on], turn alarm [off], [open] door, [close] door, [quit]> Alarm: Off
Door: Open
turn alarm [on], turn alarm [off], [open] door, [close] door, [quit]> Alarm: Off
Door: Closed
turn alarm [on], turn alarm [off], [open] door, [close] door, [quit]> Alarm: On
Door: Closed
turn alarm [on], turn alarm [off], [open] door, [close] door, [quit]> Alarm: *SIREN*
Door: Open
turn alarm [on], turn alarm [off], [open] door, [close] door, [quit]> Invalid input.
Alarm: *SIREN*
Door: Open
turn alarm [on], turn alarm [off], [open] door, [close] door, [quit]>'''
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