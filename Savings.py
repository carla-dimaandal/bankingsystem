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
