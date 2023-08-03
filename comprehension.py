"""[list comprehension] Given a list of strings, create a new list that contains only the
strings with more than 5 characters using list comprehension."""
def filter_long_strings(strings):
    long_strings = [s for s in strings if len(s)>5]
    return long_strings
input_list = ["apple", "banana", "orange", "grape", "kiwi"]
print(filter_long_strings(input_list))  # Output: ['banana', 'orange']

input_list = ["hello", "world", "python", "map"]
print(filter_long_strings(input_list))  # Output: ['python']

"""[list comprehension] Given two lists of integers, create a list that contains the
product of each element of the first list with the corresponding element in the
second list using list comprehension.
"""
def multiply_lists(list1, list2):
    product_list = [x * y for x, y in zip(list1, list2)]
    return product_list
list1=[1,2,3,4]
list2=[10,20,30,40]
print(multiply_lists(list1,list2)) #output:[10, 40, 90, 160]

"""[list comprehension] Given three lists list1, list2, and list3, each containing
integers, write a Python program using list comprehension to generate a new list of
unique triplets (x, y, z) where x is from list1, y is from list2, and z is from list3, such
that x + y + z = 0."""
def find_triplets(list1,list2,list3):
    triplets=[(x,y,z) for x in list1 for y in list2 for z in list3 if x+y+z==0]
    return triplets
list1 = [-1, 0, 1, 2, -1, -4]
list2 = [-3, -1, 0, 2, 3, 5]
list3 = [3, 4, 5, -2, -3, -1]
print(find_triplets(list1,list2,list3)) #output:[(-1, -3, 4), (-1, 2, -1), (-1, 3, -2), (0, -3, 3), (0, 2, -2), (0, 3, -3), (1, 0, -1), (1, 2, -3), (2, -1, -1), (2, 0, -2), (-1, -3, 4), (-1, 2, -1), (-1, 3, -2), (-4, -1, 5), (-4, 0, 4), (-4, 5, -1)]

"""[dictionary comprehension] Given two lists - one containing keys and another
containing values, create a dictionary using dictionary comprehension.
"""
def create_dict(key,values):
    dict={key:values for key, values in zip(key,values)}
    return dict
keys_list = ['x', 'y', 'z']
values_list = [10, 20, 30]
print(create_dict(keys_list,values_list)) #output:{'x': 10, 'y': 20, 'z': 30}
"""[dictionary comprehension] Given a dictionary with students' names as keys and
their respective scores as values, create a new dictionary that contains only the
students who scored more than 80 using dictionary comprehension."""
def filter_high_score(scores):
    high_score={name:score for name,score in scores.items() if score > 80}
    return high_score
student_scores={
    'Rabin':95,
    'Shyam':100,
    'Ram':34,
    'Sita':20
}
print(filter_high_score(student_scores)) #output:{'Rabin': 95, 'Shyam': 100}

"""[dictionary comprehension] Create a dictionary using dictionary comprehension
to represent the ASCII values of lowercase alphabets (a-z) where the keys are the
alphabets, and the values are their corresponding ASCII values.
"""
def ascii_values():
    ascii_values = {chr(ord('a') + i): ord('a') + i for i in range(26)}
    return ascii_values
print(ascii_values())
#output:{'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}

""" [set comprehension] Given a list of numbers, create a set using set
comprehension that contains only unique even numbers."""
def unique_even_numbers(numbers):
    even_numbers={num for num in numbers if num %2 == 0}
    return even_numbers
numbers_list=[1,2,3,4,5,6,7,8,9,10]
print(unique_even_numbers(numbers_list)) #output:{2, 4, 6, 8, 10}

"""[set comprehension] Given a list of words, write a Python program to create a set
using set comprehension that contains all the unique characters present in the
words.
"""
def get_unique_characters(words):
    unique_characters= {char for word in words for char in word}
    return unique_characters
words_list=["apple", "banana", "orange", "grape"]
print(get_unique_characters(words_list))
#output:{'b', 'g', 'n', 'p', 'o', 'e', 'r', 'l', 'a'}

"""[set comprehension] Given two strings, write a Python program to create a set
using set comprehension that contains all the characters that are common in both
strings."""
def common_char(str1,str2):
    common={char for char in str1 if char in str2}
    return common
string1 = "hello"
string2 = "world"
print(common_char(string1, string2)) #output:{'o', 'l'}