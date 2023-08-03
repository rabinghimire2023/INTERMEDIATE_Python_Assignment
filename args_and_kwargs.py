"""[*args]Write a Python function that takes an arbitrary number of positional
arguments and returns the sum of all the numbers. Test your function with various
input cases.
"""
def sum_of_numbers(*args):
    result = sum(args)
    return result
print(sum_of_numbers(1, 2, 3))             # Output: 6 
print(sum_of_numbers(10, 20, 30, 40))      # Output: 100 
print(sum_of_numbers(2.5, 3.5, 4.5))       # Output: 10.5 
print(sum_of_numbers(0))                   # Output: 0 
print(sum_of_numbers())                    # Output: 0 
print(sum_of_numbers(-5, 5, -10, 10, 0))   # Output: 0 

"""[*args] Write a Python function concat_strings that takes any number of strings as
arguments and returns a single concatenated string.
"""
def concat_strings(*args):
    concatnated_string = ''.join(args)
    return concatnated_string

print(concat_strings("Hello", " ", "World", "!"))     # Output: "Hello World!"
print(concat_strings("Concatenate", " ", "these", " ", "strings."))  # Output: "Concatenate these strings."
print(concat_strings("One", " ", "Two", " ", "Three", " ", "Four"))    # Output: "One Two Three Four"
print(concat_strings("This", " ", "is", " ", "a", " ", "test."))       # Output: "This is a test."
print(concat_strings(""))                                       # Output: ""

"""[**kwargs] Write a Python function calculate_total_cost that calculates the total
cost of items purchased from a store. The function should accept multiple keyword
arguments, where the key is the item name, and the value is the item's price. The
function should return the total cost of all items."""
def calculate_total_cost(**kwargs):
    total_cost=sum(kwargs.values())
    return total_cost
print(calculate_total_cost(shoes=50, shirt=25, pants=40, socks=10)) # Output: 125 
print(calculate_total_cost(book=15.99, pen=1.5, notebook=5.25))     # Output: 22.740000000000002

"""[**kwargs] Create a function create_student_report that takes the student's
name as the first argument, the student's age as the second argument, and an
arbitrary number of keyword arguments for the subjects and their respective
scores. The function should return a dictionary with the student's information and a
list of subjects along with their scores.
"""
def create_Student_report(name,age,**kwargs):
    student_info={
        'Name':name,
        'Age':age,
        'Subject':[]    
    }
    for subject,score in kwargs.items():
        student_info['Subject'].append({'subject': subject, 'score': score})
    return student_info
print(create_Student_report('Rabin',23,math=99,science=90)) 
#output:{'Name': 'Rabin', 'Age': 23, 'Subject': [{'subject': 'math', 'score': 99}, {'subject': 'science', 'score': 90}]}
print(create_Student_report('Shyam',20,math=19,science=10,english=30,social=32))
#outpur:{'Name': 'Shyam', 'Age': 20, 'Subject': [{'subject': 'math', 'score': 19}, {'subject': 'science', 'score': 10}, {'subject': 'english', 'score': 30}, {'subject': 'social', 'score': 32}]}