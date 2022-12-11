import Salary
import Savings
while True:
    choice = int(input("Select Bank Account Type\n 1. Savings Account\n 2. Salary Account\n 3. Exit\n-> "))
    if choice == 1:
        Savings.SAVINGS.runSAVINGS()
    elif choice == 2:
        Salary.SALARY.runSALARY()
    elif choice == 3:
        exit()
    else:
        print("Invalid!")
