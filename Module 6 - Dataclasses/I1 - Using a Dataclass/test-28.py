import subprocess
import platform
import difflib

# Defined test cases
# For each test case:
# The first element is the input string (with "\n" for each user input)
# The second element is the expected output string

test_cases = [ 
    (
        "hello\nKit\nKit\nKat\nKit\nquit", 
        '''Kit says hiss
Kat says hiss
Feed [Kit], Feed [Kat], [quit]?
> Please provide a valid cat name or quit.
Feed [Kit], Feed [Kat], [quit]?
> Feeding Kit
Kit says meow
Kat says hiss
Feed [Kit], Feed [Kat], [quit]?
> Feeding Kit
Kit says meow
Kat says hiss
Feed [Kit], Feed [Kat], [quit]?
> Feeding Kat
Kit says meow
Kat says meow
Feed [Kit], Feed [Kat], [quit]?
> Feeding Kit
Kit says meow
Kat says meow
Feed [Kit], Feed [Kat], [quit]?
>'''
    ),


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