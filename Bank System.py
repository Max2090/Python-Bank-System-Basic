# Bank System

def Check_Balance(balance):
    print("****************************")
    print(f"Your balance is ${balance:.2f}")
    print("****************************")

def Deposit():
    print("****************************")
    amount = float(input("Enter an amount to be deposited: "))
    print("****************************")
    
    if amount < 0:
        print("****************************")
        print("That's not a valid amount")
        print("****************************")
        return 0
    else:
        return amount

def Withdraw(balance):
    amount = float(input("Enter amount to be withdrawn: "))
    
    if amount > balance:
        print("****************************")
        print("Insufficient funds")
        print("****************************")
        return 0
    elif amount < 0:
        print("****************************")
        print("Amount must be greater than 0")
        print("****************************")
        return 0
    else:
        return amount
    
def main():
    
    balance = 0

    is_running = True

    while is_running:
        print("****************************")
        print("       Bank Program         ")
        print("****************************")
        
        print("1. Check Balance")
        print("2. Deposit Balance")
        print("3. Withdraw Balance")
        print("4. Exit")
        print("****************************")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            Check_Balance(balance)
        elif choice == "2":
            balance += Deposit()
        elif choice == "3":
            balance -= Withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("****************************")
            print("Enter a vaild choice")
            print("****************************")
            
    print("****************************")
    print("Thank you! Have a nice day")
    print("****************************")
    
if __name__ == "__main__":
    
    main()




    