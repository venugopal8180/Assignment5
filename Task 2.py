'''
Task 2: Demonstrate List Slicing 
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
 '''

#Created a list of numbers from 1 to 10
numbers = [1,2,3,4,5,6,7,8,9,10]


""" it prints a type of numbers.
    displaying the original list.
"""
print(type(numbers))
print(f"Original List: {numbers}")


"""extracting the first five list elements by slicing technique,
   displaying the extracted list elements.
"""
extracted_list = numbers[0:5]
print(f"Extracted first five elements: {extracted_list}")


"""reversing the extracted list elements by using slicing technique
   #displaying the reversed list elements
"""
reversed_list = extracted_list[::-1]
print(f"Reversed the extracted elements: {reversed_list}")    
