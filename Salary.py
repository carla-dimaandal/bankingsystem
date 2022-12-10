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