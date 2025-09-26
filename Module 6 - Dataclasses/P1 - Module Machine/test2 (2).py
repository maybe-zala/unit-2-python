import subprocess
import platform
import difflib

# Defined test cases
# For each test case:
# The first element is the input string (with "\n" for each user input)
# The second element is the expected output string

test_cases = [
    (
        "Complete\nPass\nComplete\nFail\nComplete\nPass", 
        '''Current State: Introductory Exercises
> Current State: Project
> Error: Invalid transition
Current State: Project
> Current State: Benchmark
> Current State: Project
> Current State: Benchmark
> Current State: Module Complete'''
    ),
    (
        "Pass\nFail\nComplete\nPass\nFail\nComplete\nComplete\nFail\nquit\nComplete\nPass", 
        '''Current State: Introductory Exercises
> Error: Invalid transition
Current State: Introductory Exercises
> Error: Invalid transition
Current State: Introductory Exercises
> Current State: Project
> Error: Invalid transition
Current State: Project
> Error: Invalid transition
Current State: Project
> Current State: Benchmark
> Error: Invalid transition
Current State: Benchmark
> Current State: Project
> Error: Invalid action
Current State: Project
> Current State: Benchmark
> Current State: Module Complete'''
    ),
    ("Complete\nComplete\nFail\nComplete\nFail\nComplete\nFail",
     '''Current State: Introductory Exercises
> Current State: Project
> Current State: Benchmark
> Current State: Project
> Current State: Benchmark
> Current State: Project
> Current State: Benchmark
> Current State: Failed'''
),
    ("Complete\nComplete\nFail\nComplete\nFail\nComplete\nPass",
     '''Current State: Introductory Exercises
> Current State: Project
> Current State: Benchmark
> Current State: Project
> Current State: Benchmark
> Current State: Project
> Current State: Benchmark
> Current State: Module Complete'''
    )
]

# Run test cases
for idx, (input_data, expected_output) in enumerate(test_cases, 1):
    print(f"Running Test Case {idx}:")
    
    os_name = platform.system()
    print(f'OS: {os_name}')
    python_command = 'python3' if os_name == 'Darwin'or os_name =='Linux' else 'python'
    
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