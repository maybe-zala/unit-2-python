from main import *
# Just in case you use unittest.
import unittest

# ------------------------- Dont touch code above -------------------------
#python3 -m pytest

from main import *
def test_BankAccount():
    balance = BankAccount("Basic", 0, -100)
    assert balance.account_type == "Basic"
    assert balance.current_amount == 0
    assert balance.limit == -100
    balance2 = BankAccount("Super-Duper", 0, -500)
    assert balance2.account_type == "Super-Duper"
    assert balance2.current_amount == 0
    assert balance2.limit == -500


def test_withdraw_function():
    balance1 = BankAccount("Basic", 100, -100)
    balance2 = BankAccount("Super-Duper", 100, -500)
    balance3 = BankAccount("Basic", -50, -100)
    assert balance1.account_type == "Basic"
    assert balance1.current_amount == 100
    assert balance1.limit == -100
    assert balance2.account_type == "Super-Duper"
    assert balance2.current_amount == 100
    assert balance2.limit == -500
    assert balance3.account_type == "Basic"
    assert balance3.current_amount == -50
    assert balance3.limit == -100
    amount = 300
    withdraw1 = withdraw(amount, balance1)
    withdraw2 = withdraw(amount, balance2)
    withdraw3 = withdraw(amount, balance3)

    assert withdraw1 == "Insufficient Funds."
    assert withdraw2 == f"Withdrew ${amount}."
    assert withdraw3 == "Cannot withdraw while overdrawn."

    assert balance1.account_type == "Basic"
    assert balance1.current_amount == 100
    assert balance1.limit == -100
    assert balance2.account_type == "Super-Duper"
    assert balance2.current_amount == -200
    assert balance2.limit == -500
    assert balance3.account_type == "Basic"
    assert balance3.current_amount == -50
    assert balance3.limit == -100
    
def test_deposit_function():
    balance1 = BankAccount("Basic", 100, -100)
    balance2 = BankAccount("Super-Duper", 0, -500)
    balance3 = BankAccount("Basic", 0, -100)
    assert balance1.account_type == "Basic"
    assert balance1.current_amount == 100
    assert balance1.limit == -100
    assert balance2.account_type == "Super-Duper"
    assert balance2.current_amount == 0
    assert balance2.limit == -500
    assert balance3.account_type == "Basic"
    assert balance3.current_amount == 0
    assert balance3.limit == -100

    amount = 300

    deposit1 = deposit(amount,balance1)
    assert balance1.current_amount == 400

    assert balance1.account_type == "Basic"
    assert balance1.current_amount == 400
    assert balance1.limit == -100
    assert balance2.account_type == "Super-Duper"
    assert balance2.current_amount == 0
    assert balance2.limit == -500
    assert balance3.account_type == "Basic"
    assert balance3.current_amount == 0
    assert balance3.limit == -100

def test_account_function():
    balance1 = BankAccount("Basic", 100, -100)
    option = "Super-Duper"
    change1 = change_account(option,balance1)
    assert balance1.account_type == "Super-Duper"

    balance2 = BankAccount("Super-Duper", 1, -500)
    option2 = "cancel"
    change2 = change_account(option2,balance2)
    assert change2 == "Action canceled."
    assert balance2.account_type == "Super-Duper"

    balance3 = BankAccount("Super-Duper", 1, -500)
    option3 = "Super-Duper"
    change3 = change_account(option3,balance3)
    assert change3 == f"Your already on the account type 'Super-Duper'."
    assert balance3.account_type == "Super-Duper"

    balance4 = BankAccount("Super-Duper", 100, -500)
    option4 = "beep"
    change4 = change_account(option4,balance4)
    assert change4 == "Invalid option."
    assert balance4.account_type == "Super-Duper"
    
    balance5 = BankAccount("Super-Duper", -100, -500)
    option5 = "Basic"
    change5 = change_account(option5,balance5)
    assert change5 == "Cannot change account type while overdrawn."
    assert balance5.account_type == "Super-Duper"




