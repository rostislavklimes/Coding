file = open("Python/data/bank_account.txt", "r", encoding="utf-8")
data = file.read().split("\n")

balance = int(data[0])
cash = int(data[1])
transactions = []

for t in data[2:]:
    if t != "":
        transactions.append(t)

file.close()

def show_balance(balance, cash):
    print(f"You have {balance}$ on your bank account and {cash}$ in cash")
    

def transactions_history(transactions):
    if len(transactions) == 0:
        print("No transactions yet")
    else:
        print("Transactions:")
        for transaction in transactions:
            print(f"- {transaction}")

def deposit(amount, balance, cash):
    if cash >= amount:
        balance = balance + amount
        cash = cash - amount
        transactions.append(f"deposited {amount}$")
    else:
        print(f"Not enough money in cash")
    return balance, cash

def withdraw(amount, balance, cash):
    if amount <= balance:
        balance = balance - amount
        cash = cash + amount
        transactions.append(f"withdrew {amount}$")
    else:
        print("Not enough money on your bank balance")
    return balance, cash

while True:
    print()
    print("1 - show balance\n2 - show transactions history\n3 - deposit money\n4 - withdraw money\n5 - end")
    print()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print()
        show_balance(balance, cash)
    elif choice == 2:
        print()
        transactions_history(transactions)
    elif choice == 3:
        print()
        amount = int(input("Enter amount you would like to deposit: "))
        balance, cash = deposit(amount, balance, cash)
    elif choice == 4:
        print()
        amount = int(input("Enter amount you would like to withdraw: "))
        balance, cash = withdraw(amount, balance, cash)
    elif choice == 5:
        break

file = open("Python/data/bank_account.txt", "w", encoding="utf-8")
file.write(str(balance) + "\n")
file.write(str(cash) + "\n")
for transaction in transactions:
    file.write(transaction + "\n")
file.close()