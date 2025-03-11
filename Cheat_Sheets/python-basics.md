# 📋 Python Basics Cheat Sheet

[← Back to Main README](../README.md) | [View All Cheat Sheets](README.md)

This cheat sheet provides a quick reference for Python basics that will be helpful during the chatbot workshop.

## Table of Contents
- [📋 Python Basics Cheat Sheet](#-python-basics-cheat-sheet)
  - [Table of Contents](#table-of-contents)
  - [Variables and Data Types](#variables-and-data-types)
  - [Basic Operations](#basic-operations)
  - [Control Flow](#control-flow)
  - [Data Structures](#data-structures)
    - [Lists](#lists)
    - [Dictionaries](#dictionaries)
  - [Functions](#functions)
  - [Error Handling](#error-handling)
  - [Working with Files](#working-with-files)
  - [Modules and Imports](#modules-and-imports)
  - [Environment Variables](#environment-variables)
  - [JSON Handling](#json-handling)
  - [Tips for Workshop](#tips-for-workshop)

## Variables and Data Types

```python
# Integer
age = 25

# Float
price = 19.99

# String
name = "Python"
multiline = """This is a
multiline string"""

# Boolean
is_active = True
is_closed = False

# None
result = None

# Check type
print(type(age))  # <class 'int'>

# Type conversion
str_num = "42"
num = int(str_num)  # 42
float_num = float(str_num)  # 42.0
```

[Back to Top](#-python-basics-cheat-sheet)

## Basic Operations

```python
# Arithmetic
sum_result = 5 + 3  # 8
difference = 10 - 4  # 6
product = 3 * 7  # 21
quotient = 20 / 4  # 5.0 (float)
integer_division = 20 // 4  # 5 (integer)
remainder = 20 % 3  # 2
power = 2 ** 3  # 8

# String operations
greeting = "Hello"
name = "World"
message = greeting + " " + name  # "Hello World"
repeat = "Python " * 3  # "Python Python Python "

# String methods
text = "python programming"
print(text.upper())  # "PYTHON PROGRAMMING"
print(text.capitalize())  # "Python programming"
print(text.replace("p", "j"))  # "jython jrogramming"
print(text.split(" "))  # ["python", "programming"]
```

[Back to Top](#-python-basics-cheat-sheet)

## Control Flow

```python
# If statement
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# For loop
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# Loop with break and continue
for i in range(10):
    if i == 3:
        continue  # Skip 3
    if i == 7:
        break  # Stop at 7
    print(i)
```

[Back to Top](#-python-basics-cheat-sheet)

## Data Structures

### Lists

```python
# Create a list
fruits = ["apple", "banana", "cherry"]

# Access elements
first_fruit = fruits[0]  # "apple"
last_fruit = fruits[-1]  # "cherry"

# Modify elements
fruits[1] = "orange"  # ["apple", "orange", "cherry"]

# List methods
fruits.append("mango")  # Add to end
fruits.insert(1, "blueberry")  # Insert at index
fruits.remove("cherry")  # Remove specific item
popped = fruits.pop()  # Remove and return last item
fruits.sort()  # Sort in place

# List slicing
numbers = [0, 1, 2, 3, 4, 5]
subset = numbers[1:4]  # [1, 2, 3]
reversed_list = numbers[::-1]  # [5, 4, 3, 2, 1, 0]

# List comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
even_nums = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
```

### Dictionaries

```python
# Create a dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Access values
name = person["name"]  # "John"
# Safer access with get
age = person.get("age", 0)  # 30 (returns 0 if key doesn't exist)

# Modify values
person["age"] = 31
person["email"] = "john@example.com"  # Add new key-value pair

# Dictionary methods
keys = person.keys()  # dict_keys(['name', 'age', 'city', 'email'])
values = person.values()  # dict_values(['John', 31, 'New York', 'john@example.com'])
items = person.items()  # dict_items([('name', 'John'), ('age', 31), ...])

# Check if key exists
if "name" in person:
    print("Name exists")

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

[Back to Top](#-python-basics-cheat-sheet)

## Functions

```python
# Define a function
def greet(name):
    return f"Hello, {name}!"

# Call a function
message = greet("Alice")  # "Hello, Alice!"

# Default parameters
def greet_with_time(name, time="morning"):
    return f"Good {time}, {name}!"

morning_greeting = greet_with_time("Bob")  # "Good morning, Bob!"
evening_greeting = greet_with_time("Bob", "evening")  # "Good evening, Bob!"

# Variable number of arguments
def sum_all(*args):
    return sum(args)

total = sum_all(1, 2, 3, 4)  # 10

# Keyword arguments
def build_profile(**kwargs):
    return kwargs

profile = build_profile(name="Alice", age=30, job="Developer")
# {'name': 'Alice', 'age': 30, 'job': 'Developer'}

# Lambda functions
square = lambda x: x**2
print(square(5))  # 25

# Function as argument
def apply_function(func, value):
    return func(value)

result = apply_function(lambda x: x*2, 10)  # 20
```

[Back to Top](#-python-basics-cheat-sheet)

## Error Handling

```python
# Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Multiple exceptions
try:
    value = int("abc")
except ValueError:
    print("Invalid conversion")
except TypeError:
    print("Type error occurred")

# Handling any exception
try:
    # risky code
    pass
except Exception as e:
    print(f"An error occurred: {str(e)}")

# Finally clause (always executes)
try:
    file = open("data.txt", "r")
    # process file
except FileNotFoundError:
    print("File not found")
finally:
    file.close()  # This will always run

# With statement (context manager)
with open("data.txt", "r") as file:
    content = file.read()
    # File is automatically closed after this block
```

[Back to Top](#-python-basics-cheat-sheet)

## Working with Files

```python
# Reading a file
with open("file.txt", "r") as file:
    content = file.read()  # Read entire file
    
with open("file.txt", "r") as file:
    lines = file.readlines()  # Read lines into a list
    
with open("file.txt", "r") as file:
    for line in file:  # Process line by line
        print(line.strip())

# Writing to a file
with open("output.txt", "w") as file:
    file.write("Hello, World!")  # Write string
    
with open("output.txt", "a") as file:
    file.write("\nAppended text")  # Append to file
    
# Writing multiple lines
lines = ["Line 1", "Line 2", "Line 3"]
with open("output.txt", "w") as file:
    file.writelines([line + "\n" for line in lines])
```

[Back to Top](#-python-basics-cheat-sheet)

## Modules and Imports

```python
# Import entire module
import math
result = math.sqrt(16)  # 4.0

# Import specific functions
from math import sqrt, pi
result = sqrt(16)  # 4.0

# Import with alias
import pandas as pd
import numpy as np

# Import all (not recommended)
from math import *

# Create your own module
# In mymodule.py:
def my_function():
    return "Hello from module"

# In main script:
import mymodule
result = mymodule.my_function()
```

[Back to Top](#-python-basics-cheat-sheet)

## Environment Variables

```python
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get environment variable
api_key = os.getenv("API_KEY")
debug_mode = os.getenv("DEBUG", "False") == "True"

# Set environment variable (only for current process)
os.environ["TEMP_VAR"] = "value"
```

[Back to Top](#-python-basics-cheat-sheet)

## JSON Handling

```python
import json

# Python dict to JSON string
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
json_string = json.dumps(data, indent=4)

# JSON string to Python dict
json_data = '{"name": "Alice", "age": 25}'
python_dict = json.loads(json_data)

# Write JSON to file
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

# Read JSON from file
with open("data.json", "r") as file:
    loaded_data = json.load(file)
```

[Back to Top](#-python-basics-cheat-sheet)

## Tips for Workshop

- Use descriptive variable names to make your code more readable
- Break down complex problems into smaller functions
- Add comments to explain non-obvious code sections
- Use list comprehensions and dictionary comprehensions for cleaner code
- Properly handle potential errors with try-except blocks
- Use the with statement when working with files to ensure they're properly closed
- Keep functions small and focused on a single task
- Test your code with different inputs to ensure it works correctly

[Back to Top](#-python-basics-cheat-sheet)

[← Back to Main README](../README.md) | [View All Cheat Sheets](README.md)