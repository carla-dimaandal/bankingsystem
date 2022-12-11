import Savings
import random
import sys

class SALARY(Savings.SAVINGS):
    def __init__(self, name, address, pin, phone_number, employer, empID, balance):
        super().__init__(name, address, pin, phone_number, balance)
        self.employer = employer
        self.empID = empID
        self.account_number = {random.randint(10000000, 100000000000)} 

    def getName(self):
        return self.name
    
    def getAddress(self):
        return self.address
    
    def getPhone_number(self):
        return self.phone_number

    def getAccountNumber(self):
        return self.account_number

    def getBalance(self):
        return self.balance

    def getEmployer(self):
        return self.employer

    def getEmpID(self):
        return self.empID

    def salary_details(self):
        salary.account_detail()
        print(f"Account Holder's Employer: {self.employer}")
        print(f"Account Holder's EmployerID: {self.empID}\n")

    def withdraw_pass(self, amount):
        if amount > self.balance:
            print("Insufficient fund!")
            print(f"Your balance is PHP {self.balance} only.")
            print(f"You should have a maintaining balance of: PHP. 10,000")
            print("Try with lesser amount than balance.")
            print()
        else:
            self.balance = self.balance - amount
            print(f"PHP {amount} withdrawal successful!")
            print("Current account balance: PHP", self.balance)
            print()

    def print_salary(self):
        print(f"""
                        printing receipt..............
                  **************************************
                      Transaction is now complete.                         
                      Transaction number: {random.randint(10000, 1000000)} 
                      Account holder: {salary.getName().upper()}                  
                      Account number: {salary.getAccountNumber()}         
                      Employer: {salary.getEmployer()}      
                      Employee ID: {salary.getEmpID()}                                        
                      Available balance: PHP {salary.getBalance()}                 
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
                option = int(input("Enter Choice ->"))
            except:
                print("Error: Enter 1, 2, 3, 4, or 5 only!\n")
                continue
            else:
                if option == 1:
                    salary.salary_details()
                elif option == 2:
                    salary.check_balance()
                elif option == 3:
                    amount = int(input("How much you want to deposit(PHP):"))
                    salary.deposit(amount)
                elif option == 4:
                    amount = int(input("How much you want to withdraw(PHP):"))
                    salary.withdraw_pass(amount)
                elif option == 5:
                    salary.print_salary()
                    sys.exit()

    def user_balance():
        while True:
            print("\nInitial Deposit Must be 10000 Pesos and Above")
            balance = float(input("Enter  "))
            if balance >= 10000:
                return balance
            else:
                print("Invalid Deposit. Please Deposit Atleast 10000 and Above")
    
    def runSALARY():
        print("\n*****WELCOME TO OUR BANK*****")
        print("___________________________________________________________\n")
        print("----------ACCOUNT CREATION----------")
        name = input("Enter your name: ")
        address = input("Enter Your Address: ")
        phone_number = input("Enter Your Phone Number: ")
        employer = input("Enter your employer: ")
        empID = input("Employee ID: ")
        pin = Savings.SAVINGS.user_pin()
        balance = SALARY.user_balance()
        print("Congratulations! Account created successfully......\n")
        global salary
        salary = SALARY(name, address, pin, phone_number, employer, empID, balance)

        while True:
            trans = input("Do you want to do any transaction?(y/n):")
            if trans == "y":
                salary.transaction()
            elif trans == "n":
                print("""
            -------------------------------------
            | Thanks for choosing us as your bank |
            | Visit us again!                     |
            -------------------------------------
                    """)    
                break
            else:
                print("Wrong command!  Enter 'y' for yes and 'n' for NO.\n")
