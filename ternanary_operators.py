"""Write a Python function called check_odd_even that takes an integer as input and
uses a ternary operator to return "Even" if the number is even, and "Odd" if the
number is odd.
"""
def check_odd_even(number):
    result = 'Even' if number % 2 == 0 else 'Odd'
    return result 

print(check_odd_even(0)) #output:Even
print(check_odd_even(1)) #output:Odd
print(check_odd_even(4)) #output:Even

"""Create a Python function check_leap_year that takes a year as input and uses a
ternary operator to determine if it's a leap year. Return "Leap Year" if it is, otherwise
"Not a Leap Year." (A leap year is divisible by 4, except for years divisible by 100
but not divisible by 400).
"""
def check_leap_year(year):
    result = 'Leap year' if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 'Not a Leap Year'
    return result

print(check_leap_year(2000)) #output: Leap year
print(check_leap_year(2021)) #output:Not a Leap Year

"""Write a function find_bigger_number that takes three integers as input and uses a
ternary operator to return the larger number. If all numbers are equal, return
"Equal."
"""
def find_bigger_number(a,b,c):
    result = 'Equal' if a == b == c else (a if a>=b and a>=c else (b if b>=c else c))
    return result
print(find_bigger_number(2,4,3)) #output:4
print(find_bigger_number(3,3,3)) #output:Equal

"""Implement a function called check_prime that takes a positive integer as input and
uses a ternary operator to determine if it's a prime number. Return "Prime" if it is,
otherwise "Not Prime."""
def check_prime(number):
    if number < 2:
        return "Not Prime"
    is_prime = all(number % i != 0 for i in range(2, int(number**0.5) + 1))
    return "Prime" if is_prime else "Not Prime"
print(check_prime(2)) #output:Prime
print(check_prime(22)) #output:Not Prime
print(check_prime(15)) #output:Not Prime
