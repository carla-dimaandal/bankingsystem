import random
import sys


class SAVINGS:
    def __init__(self, name, address, pin, phone_number, balance):
        self.name = name
        self.address = address
        self.pin = pin
        self.phone_number = phone_number
        self.account_number = random.randint(10000000, 100000000000)  
        self.balance = balance
        

    def account_detail(self):
        print("\n----------ACCOUNT DETAIL----------")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.name.upper()}")
        print(f"Account Holder's Address: {self.address}")
        print(f"Account Holder's Phone Number: {self.phone_number} ")
        print(f"Account Pin Number: {self.pin}")
        print(f"Available Balance: PHP {self.balance}")

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Current Account balance: PHP", self.balance)
        print()

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("\nInsufficient Fund!")
            print(f"Your Balance is PHP {self.balance} only.") 
            print("Try With Lesser Amount Than Balance.\n")
            print()
        else:
            self.balance = self.balance - self.amount
            print(f"\nPHP {amount} Withdrawal Successful!")
            print("Current Account Balance: PHP", self.balance)
            print("\n\n")

    def check_balance(self):
        print("\nAvailable Balance: PHP", self.balance)
        print("\n\n")

    def user_pin():
        while True:
            pin = int(input("Enter 4 digit pin: "))
            if len(str(pin)) == 4:
                return pin
            else:
                print("Invalid Pin. Please Enter 4 digit pin")
    
    def user_balance():
        while True:
            print("\nInitial Deposit Must be 5000 Pesos and Above")
            balance = float(input("Enter  "))
            if balance >= 5000:
                return balance
            else:
                print("Invalid Deposit. Please Deposit Atleast 5000 and Above")
      def display_receipt(self):
        print(f"""
                Printing Receipt..............
          **************************************
              Transaction is Now Complete.                         
              Transaction Number: {random.randint(10000, 1000000)} 
              Account Holder: {self.name.upper()}                  
              Account Number: {self.account_number}                
              Account Pin: **** 
              Available Balance: PHP {self.balance}   


              Thanks for choosing us as your bank                  
          **************************************
          """)
    def transaction(self):
        while True:
            print("""
            TRANSACTION 
            *****************
                Menu:
                1. Account Detail
                2. Check Balance
                3. Deposit
                4. Withdraw
                5. Exit
            *****************
            """)

        
            try:
                option = int(input("Enter Choice -> "))
            except:
                print("Error: Enter 1, 2, 3, 4, or 5 only!\n")
                continue
            else:
                if option == 1:
                    savings.account_detail()
                elif option == 2:
                    savings.check_balance()
                elif option == 3:
                    amount = int(input("How much you want to deposit(PHP):"))
                    savings.deposit(amount)
                elif option == 4:
                    amount = int(input("How much you want to withdraw(PHP):"))
                    savings.withdraw(amount)
                elif option == 5:
                    savings.display_receipt()
                    sys.exit()
    def user_pin():
        while True:
            pin = int(input("Enter 4 digit pin: "))
            if len(str(pin)) == 4:
                return pin
            else:
                print("Invalid Pin. Please Enter 4 digit pin")
    
    def user_balance():
        while True:
            print("\nInitial Deposit Must be 5000 Pesos and Above")
            balance = float(input("Enter  "))
            if balance >= 5000:
                return balance
            else:
                print("Invalid Deposit. Please Deposit Atleast 5000 and Above")

    def runSAVINGS():
        print("\n*******WELCOME TO OUR BANK*******")
        print("_____________________________________\n")
        print("----------ACCOUNT CREATION----------")
        name = input("Enter Your Name: ")
        address = input("Enter Your Address: ")
        phone_number = input("Enter Your Phone Number: ")
        pin = SAVINGS.user_pin()
        balance = SAVINGS.user_balance()
        print("\n\nCongratulations! Account Created Successfully......\n")
        global savings
        savings = SAVINGS(name, address, pin, phone_number, balance)

        while True:
            trans = input("Do you want To Do Any Transaction?(y/n):")
            if trans == "y":
                savings.transaction()
            elif trans == "n":
                print("""
            -------------------------------------
            | Thanks for choosing us as your bank |
            | Visit us again!                     |
             -------------------------------------
                    """)
                break
            else:
                print("Wrong Command!  Enter 'y' for yes and 'n' for no.\n")
