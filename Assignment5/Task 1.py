"""
Task 1: Create a Dictionary of Student Marks
Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
"""

#creating a dictionary named students and keys as student names and values as student marks
students = {
    'Alice' : 50,
    'Bob'   : 60,
    'Charlie' : 94,
    'David' : 90,
    'Eve' : 100
}

#taking student name as input from the user for retrieving the student marks 
name = input("Enter Student name\'s name: ")

"""here get() method is used to gets student data .
   if input student name is available in dictionary , then it retrieves the student marks
   if not then it prints the  "Student not found"
"""
print(students.get(name,"Student not found"))
