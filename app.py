name = "Timothy"
age = 27

price = 150
interest_rate = 3.5
is_logged_in = True
greeting = 'Hello, world'

#To know what type a variable is ...

print(type(price))
print(type(interest_rate))
print(type(is_logged_in))
print(type(greeting))

"""

This is a
multi-line comment.
Useful for documentation.

"""

#normal print statements
print("Hello", name)

#formated string used in print statements
print(f"My age is {age}")

#getting user input  
# last_name = input("Enter your last_name: ")
# print("Hello", last_name)

#Typecasting

num = int('25') 
print (num)

text = str(100)
print (text)

bool(0)     # False
bool(5)     # True
bool('')    # False
bool("Hi")  # True


num1 = int(input("Enter first number: "))
num2 = int (input("Enter second number: "))
print (f"Sum is {num1 + num2}")

