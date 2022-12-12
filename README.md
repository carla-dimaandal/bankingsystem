# BANKING SYSTEM IN PYTHON
## Our group created a banking system wherein users can choose what account they want to create. It is either a Savings account wherein the initial deposit will be 5000 and above or a Salary account with 10000 initial deposit and above. Furthermore, the user can display the account details, check their balance, deposit, and withdraw. 
### The program used python libraries: sys, random
#### The program utilized OBJECT-ORIENTED PROGRAMMING

In order to run the program, the user must import the libraries sys, and random. As the user enters the program, they will be asked to choose between whether they intend to create a savings or salary bank account (1 or 2). They will then proceed to enter variables that are required by the program, and will be able to choose to transact or not (y or n). Once the user enters transaction, they will be given the choices on what kind of transaction they wish to proceed with. <br>
If the user chooses: <br>
1 - Account Details <br>
2 - Check Balance <br>
3 - Deposit <br>
4 - Withdraw <br>
5 - Exit
<div hidden>
@startuml uml
class Savings <|--class Salary
class Savings {
  name
  address
  pin
  phone_number
  balance
  +account_detail()
+deposit()
+withdraw()
+check_balance()
+display_receipt()
+transaction()
+user_pin()
+user_balance()
+runSAVINGS()

}

class Salary {
name
address
pin
phone_number
employer
empID
balance
account_number
+getName()
+getAddress()
+getPhone_number()
+getAccountNumber
+getBalance()
+getEmployer()
+getEmpID()
+salary_details()
+withdraw_pass()
+print_salary()
+transaction()
+user_balance()
+runSALARY



}
@enduml
<\div>
![](firstDiagram.svg)

Ratings: <br>
Code Reusability 4/4 <br>
Maintainability 4/4 <br>
Scalability 4/4 <br>
Execution 4/4 <br>
Originality 4/4 <br>
Overall impression 4/4 

Video Link: [Video Presentation](https://www.youtube.com/watch?v=2ee2iAZHNPs&ab_channel=LANCEFREDERICKDIMAANO-BSU)
