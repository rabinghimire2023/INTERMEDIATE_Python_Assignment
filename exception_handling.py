"""Write a Python program that takes two integers as input and performs division
(num1 / num2). Handle the ZeroDivisionError and display a custom error message
when the second number is zero"""
def division(num1,num2):
    try:
        result = num1/num2
        return result
    except ZeroDivisionError:
        print("Error:Division by zero!")
        return None
        
print(division(5,5)) #output: 1.0
print(division(5,0)) #output: Error:Division by zero! --None

"""Implement a program that takes user input for a filename, opens the file in read
mode, and displays its contents. Handle the FileNotFoundError and display an error
message if the file is not found.
"""
def read_file(filename):
    try:
        with open(filename,'r') as file:
            content=file.read()
            print(f"filename is {filename}")
            print(content)
    except FileNotFoundError:
        print("Error:File not found")
        
filename=input(str("Enter filename:"))
read_file(filename)

#output:
#Enter filename:rabin
#Error:File not found

"""Write a Python program that takes a user input and converts it to an integer. Handle
the ValueError and display a custom error message when the input cannot be
converted to an integer."""
def converted_integer(user_input):
    try:
        result=int(user_input)
        return result
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
        return None
    
user_input = input("Enter an integer: ")
result = converted_integer(user_input)
if result is not None:
    print(f"The converted integer is: {result}")
#output:
#Enter an integer: 34
#The converted integer is: 34

#Enter an integer: 56.23
#Error: Invalid input. Please enter a valid integer.

"""Write a Python program that takes two integers as input and performs division (num1
/ num2). Handle both ValueError (if non-integer input) and ZeroDivisionError and
display appropriate error messages.
"""
def perform_division(num1, num2):
    try:
        result = num1 / num2
        return result
    except ValueError:
        print("Error: Invalid input. Please enter valid integers.")
        return None
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
    
result = perform_division(num1, num2)
if result is not None:
    print(f"The result of division is: {result}")
    
#output:
# Enter the first number: 23
#Enter the second number: 0
#Error: Cannot divide by zero.

#Enter the first number: 23
#Enter the second number: 23
#The result of division is: 1.0

"""Write a Python program that takes user input for age. Create a custom exception
InvalidAgeError to handle cases where the age is below 0 or above 120."""
class InvalidAgeError(Exception):
    pass
def check_age(age):
    try:
        if age < 0 or age > 120:
          raise InvalidAgeError
        return age
    except InvalidAgeError as e:
        print(e,"Error: Invalid age.")
        return None
age = int(input("Enter ager: "))

    
check_result = check_age(age)
if check_result is not None:
    print(f"Your age: {check_result}")
    
#output:
#Enter ager: 125
#Error: Invalid age.

#Enter ager: 20
#Your age: 20

"""Implement a program that reads user input for a password. Create a custom
exception WeakPasswordError to handle cases where the password is shorter
than 8 characters.
"""
class WeakPasswordError(Exception):
    pass
def check_password_strength(password):
  try:
    if len(password) < 8:
        raise WeakPasswordError("Weak password. Password must be at least 8 characters long.")
    return password
  except WeakPasswordError as e:
    print(e)

password = input("Enter your password: ")
password = check_password_strength(password)
if password is not None:
  print("Password set successfully!")
  
#ouput:
# Enter your password: 12
#Weak password. Password must be at least 8 characters long.

#Enter your password: 12346789
#Password set successfully!
