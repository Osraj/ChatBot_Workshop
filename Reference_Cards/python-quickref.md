# 🃏 Python Quick Reference Card

[← Back to Reference Cards](README.md) | [← Back to Main README](../README.md)

## Basic Syntax

```python
# Variables
name = "Alice"
age = 30
is_active = True

# f-strings
greeting = f"Hello, {name}! You are {age} years old."

# Conditional statements
if age > 18:
    print("Adult")
elif age > 12:
    print("Teenager")
else:
    print("Child")
```

## Data Structures

```python
# Lists
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
first_fruit = fruits[0]

# Dictionaries
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
person["email"] = "john@example.com"
```

## Functions

```python
# Basic function
def greet(name):
    return f"Hello, {name}!"

# Function with default parameter
def greet_with_time(name, time="morning"):
    return f"Good {time}, {name}!"

# Function call
message = greet("Alice")
```

## Error Handling

```python
# Try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"Error: {str(e)}")
finally:
    print("This always runs")
```

## Working with Files

```python
# Read file
with open("file.txt", "r") as file:
    content = file.read()

# Write file
with open("output.txt", "w") as file:
    file.write("Hello, World!")

# Append to file
with open("log.txt", "a") as file:
    file.write("New log entry\n")
```

## JSON Handling

```python
import json

# Dict to JSON string
data = {"name": "John", "age": 30}
json_string = json.dumps(data)

# JSON string to dict
json_data = '{"name": "Alice", "age": 25}'
python_dict = json.loads(json_data)
```

[← Back to Reference Cards](README.md) | [← Back to Main README](../README.md)