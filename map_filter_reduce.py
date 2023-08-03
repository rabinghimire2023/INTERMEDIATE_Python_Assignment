"""[map] Write a Python function square_numbers that takes a list of integers as
input and uses the map function to return a new list containing the square of each
element."""
def square_numbers(numbers):
    squared_list=list(map(lambda x:x**2,numbers))
    return squared_list
input_list=[1,2,3,4,5]
print(square_numbers(input_list)) #output:[1, 4, 9, 16, 25]
input_list=[-1,100,-3,400,-5]
print(square_numbers(input_list)) #output:[1, 10000, 9, 160000, 25]

""" [map] Create a function convert_to_uppercase that takes a list of strings as input
and uses the map function to return a new list with all the strings converted to
uppercase.
"""
def convert_to_uppercase(strings):
    upercase_list=list(map(str.upper,strings))
    return upercase_list
input_list = ["hello", "world", "python", "map"]
print(convert_to_uppercase(input_list))  # Output: ['HELLO', 'WORLD', 'PYTHON', 'MAP']
input_list = ["One", "Two", "Three", "Four", "Five"]
print(convert_to_uppercase(input_list))  # Output: ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE']

"""[filter] Implement a function called filter_prime_numbers that takes a list of
integers as input and uses the filter function to return a new list containing only the
prime numbers."""
def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def filter_prime_numbers(numbers):
    prime_numbers = list(filter(is_prime,numbers))
    return prime_numbers
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_prime_numbers(input_list))  # Output: [2, 3, 5, 7]
input_list = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(filter_prime_numbers(input_list))  # Output: [11, 13, 17, 19]

"""[filter] Write a Python function filter_long_strings that takes a list of strings as
input and uses the filter function to return a new list containing strings with more
than 5 characters.
"""
def filter_long_strings(strings):
    long_strings =list(filter(lambda x:len(x)>5,strings))
    return long_strings
input_list = ["apple", "banana", "orange", "grape", "kiwi"]
print(filter_long_strings(input_list))  # Output: ['banana', 'orange']
input_list = ["short", "medium", "long", "verylong", "tiny"]
print(filter_long_strings(input_list))  # Output: ['medium', 'verylong']

"""[reduce] Write a Python function calculate_factorial that takes an integer as input
and uses the reduce function to return the factorial of that number."""
from functools import reduce 
def calculate_factorial(n):
    if n<0:
        raise ValueError('Factorial is not defined for negative number')
    elif n == 0:
        return 1
    else:
        return reduce(lambda x,y:x*y,range(1,n+1))
print(calculate_factorial(5))   # Output: 120
print(calculate_factorial(10))   # Output: 3628800

"""[reduce] Implement a function called concatenate_strings that takes a list of
strings as input and uses the reduce function to return a single string containing the
concatenation of all the elements.
"""
def concatenate_strings(strings):
    concatenated_string=reduce(lambda x,y:x+y,strings)
    return concatenated_string
input_list = ["Hello", " ", "World", "!"]
print(concatenate_strings(input_list))  # Output: "Hello World!"




    
        
