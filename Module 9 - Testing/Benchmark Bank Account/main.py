from dataclasses import dataclass

@dataclass
class BankAccount:
    account_type: str
    current_amount: int
    limit: int

# withdraw takes in: 
#   - amount: An integer that is how much they are taking out of their account.
#   - bank: A bank account.
# withdraws money from bank account if they have dont withdraw more than their limit.
def withdraw(amount: int, bank: BankAccount) -> str:
    if bank.current_amount > 0:
        bank.current_amount -= amount
        if bank.current_amount < bank.limit:
            bank.current_amount += amount
            return "Insufficient Funds."
        else:
            return f"Withdrew ${amount}."
    else:
        return "Cannot withdraw while overdrawn."

# Deposit takes in:
#   - amount: An integer that is how much they are putting into their account.
#   - bank: A bank account.       
# Deposits money into bank account.
def deposit(amount: int, bank: BankAccount) -> None:
    bank.current_amount += amount

# Change account takes in:
#   - options: A string that is what account they would like to change to.
#   - bank: A bank account.
# It changes the account type and limit of the bank account, based on the options parameter. Only if the account is not overdrawn.
def change_account(options: str, bank: BankAccount) -> str:
    if bank.current_amount > 0:
        if options == "Basic" and bank.account_type != "Basic":
            bank.account_type = "Basic"
            bank.limit = -100
            return "Account type changed to 'Basic'."
        elif options == "Super-Duper" and bank.account_type != "Super-Duper":
            bank.account_type = "Super-Duper"
            bank.limit = -500
            return "Account type changed to 'Super-Duper'."
        elif options == "cancel":
            return "Action canceled."
        elif options != "Basic" and options != "Super-Duper" and options != "cancel":
            return "Invalid option."
        else:
            return f"Your already on the account type '{bank.account_type}'."
    else:
        return "Cannot change account type while overdrawn."


def main() -> None:
    balance = BankAccount("Basic", 0, -100)
    while True:
        if balance.current_amount < 0:
            print(f"Balance: ${balance.current_amount} (overdrawn)")
        else:
            print(f"Balance: ${balance.current_amount}")
        select = input("[withdraw], [deposit], change account [type], [quit]> ")

        if select == "deposit":
            amount = int(input("Amount: $"))
            deposit(amount, balance)
        elif select == "withdraw":
            if balance.current_amount < 0:
                print("Cannot withdraw while overdrawn.")
            else:
                amount = int(input("Amount: $"))
                msg = withdraw(amount, balance)
                if msg != None:
                    print(msg)
        elif select == "type":
            if balance.current_amount < 0:
                print("Cannot change account type while overdrawn.")
            else:
                print(f"Current Type: {balance.account_type}")
                options = input("Change to [Basic], change to [Super-Duper], or [cancel]> ")
                print(change_account(options, balance))
        elif select == "quit":
            break
        else:
            print("Invalid Input.")

if __name__ == '__main__':
    main()