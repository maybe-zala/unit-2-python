# Benchmark: Bank Account

You will now need to test the provided class in `main.py` to see if all of the function work properly.

## Rubric

- [ ] `main.py` functions are tested correctly.
    - [ ] `BankAccount` initial state is tested correctly.
        - This should have at least 2 test cases.
        - You can two different initial states of the dataclass.
    - [ ] `withdraw` function is tested correctly.
        - This should have at least 3 test cases.
        - One test should test a successful withdraw.
        - One test should test a unsuccessful withdraw.
            - If they have money in their account and withdraw more than their bank limit.
        - One test should test if they withdraw when they don't have money in their account or are overdrawn.
    - [ ] `deposit` function is tested correctly.
        - This should have at least 1 test cases.
        - This should test them depositing money to their account.
    - [ ] `change_account` function is tested correctly.
        - This should have at least 5 test cases.
        - One test should test if the change their account to basic or super-duper.
        - One test should test if they cancel the account change.
        - One test should test if they have a invalid option.
        - One test should test if they try to change to the account that they are already on.
        - One test should test if they cannot change account types if they are overdrawn.
    - [ ] You should have at least 11 test cases in total.
- [ ] You need to test the main file using pytest or unittest.