"""
Task 1: Personal Info

1. Ask the user to enter their name.

2. Ask for their age.

3. Convert the age to an integer.

4. Create a greeting that uses both their name and age.

"""
name = input("Enter your fullname: ")
age = int(input("Enter your age: "))
print(f'Hello, {name}, your are {age} years old.')

"""
Task 2: Account Setup

1.Ask the user to input the amount they want to deposit into their bank account (float).

2.Ask whether they want to receive SMS alerts (type: bool) – accept True or False as string input, then convert to boolean.

3.Print a formatted account summary that includes:

Name

Age

Initial Deposit

SMS Alerts enabled or not (True/False)

"""

deposit = float(input("How much would you like to deposit: "))
sms_alert = bool(input("Would you like to receive sms alerts? (True/ False): "))


print("----ACCOUNT SUMMARY----- ")

print('Name',name)
print('Age',age)
print('Initial Deposit',deposit)
print('SMS Alerts Enables',sms_alert)

"""

Task 3: Bonus Calculation

1.Add a bonus of 2% of their deposit to the balance.

2.Show the new balance with the bonus.

"""

new_balance = (0.02 * deposit ) + deposit
print("Adding a 2%  bonus ...")
print('New Balance',new_balance)
