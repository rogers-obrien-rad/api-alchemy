# Basic Python Introduction Script

# --- Package Imports ---
# Importing external packages enhances Python's capabilities.
# 'requests' is for making HTTP requests and 'pandas' is for data manipulation.
import requests
import pandas as pd

# --- Basic Outputs ---
# The 'print' function outputs text to the console.
print("Hello, World!")

# --- Variables ---
# Variables store data for us to use and manipulate in our scripts.
name = "Hagen"     # A string variable to hold textual data.
age = 29           # An integer variable to hold whole numbers.
height = 6.0       # A float variable to hold decimal numbers.
works_at_ro = True # A boolean variable to hold binary True/False

print(name)
print(age)
print(height)
print(works_at_ro)

# --- Lists ---
# Lists are ordered collections of items, which can be of any type.
fruits = ["apple", "banana", "cherry"]
years = [1987, 1993, 1996]
print(fruits[0])  # Accessing the first item in the list using its index.

# --- Dictionaries ---
# Dictionaries store data in key-value pairs.
person = {
    "name": "Hagen",
    "age": 29,
    "city": "Austin"
}
print(person["name"])  # Accessing a value using its key.

# --- Advanced Outputs: F-strings ---
# f-strings offer a concise way to embed expressions inside string literals

name = "John"
age = 25
greeting = f"My name is {name} and I am {age} years old."
print(greeting)  # Output: My name is John and I am 25 years old.

double_age = f"Twice my age is {age * 2}."
print(double_age)  # Output: Twice my age is 50.

# --- Conditionals ---
# Conditionals help in executing a block of code only if a condition is true.
if age > 18:
    print("John is an adult.")
else:
    print("John is not an adult.")

# --- Loops ---
# Loops help in executing a block of code multiple times.

# The 'for' loop executes a block of code iterating through a list of items
for fruit in fruits:
    print(fruit)

# The 'while' loop executes a block of code as long as a condition remains true.
count = 0
while count < 3:
    print(f"Count is: {count}")
    count += 1

# --- Functions ---
# Functions are reusable blocks of code.
def greet(person_name):
    return "Hello, " + person_name + "!"

message = greet(name)
print(message)
