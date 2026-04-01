# Assignment 5 – Python Programs
# Task 1: Create a Dictionary of Student Marks

##  Overview

This program demonstrates the use of **dictionaries in Python**. It stores student names and their marks, allows the user to search for a student, and retrieves the corresponding marks. If the student is not found, an appropriate message is displayed.

##  Program Functionality

The program performs the following steps:
1. Creates a dictionary with:
   * Student names as **keys**
   * Marks as **values**
2. Takes a student name as input from the user.
3. Uses the `get()` method to retrieve the student’s marks.
4. Displays:
   * Marks if the student exists
   * "Student not found" if the name is not in the dictionary
   * 
## Requirements
* Python 3 installed on the system
## How to Run the Program
1. Save the Python file (e.g., `assignment5.py`)
2. Open terminal or command prompt in the file location
3. Run:

id="task1"
python task1.py

##  Example Output
Enter Student name's name: Alice
50

If student not found:
Enter Student name's name: John
Student not found

## Concepts Used
* Dictionary in Python
* Key-Value pairs
* `get()` method
* User input (`input()`)
* Conditional handling using default values

## Learning Outcome
* Understanding how dictionaries store and retrieve data
* Handling missing keys safely using `get()`
* Improving data lookup logic

# Task 2: Demonstrate List Slicing

## Overview
This program demonstrates **list slicing techniques in Python**. It extracts a portion of a list and reverses it using slicing operations.

## Program Functionality

The program performs the following steps:
1. Creates a list of numbers from 1 to 10.
2. Extracts the first five elements using slicing.
3. Reverses the extracted elements using slicing.
4. Prints:
   * Original list
   * Extracted list
   * Reversed list
     
## Example Output
Original List: [1,2,3,4,5,6,7,8,9,10]
Extracted first five elements: [1,2,3,4,5]
Reversed the extracted elements: [5,4,3,2,1]

## Concepts Used
* Lists in Python
* List slicing (`start:end`)
* Reverse slicing (`[::-1]`)
* `print()` formatting

## Learning Outcome
* Understanding list slicing techniques
* Extracting subsets of data from lists
* Reversing lists efficiently without loops

# Overall Learning from Assignment 5
Through this assignment, the following concepts are practiced:
* Working with **dictionaries**
* Using **built-in methods like `get()`**
* Understanding **list slicing and reversing**
* Writing clean and readable Python code

# Conclusion
This assignment strengthens fundamental Python concepts such as **data structures (lists and dictionaries)** and improves problem-solving skills using built-in Python features.
