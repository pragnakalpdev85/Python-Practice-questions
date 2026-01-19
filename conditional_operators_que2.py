# Question 2: Grade Calculator
# Write a program that takes a student's marks (0-100) as input and prints the grade based on the following criteria:

# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F

# Rules:
# No in-built functions allowed (except input() and print())
# Must use conditional operators
# Handle edge cases (marks < 0 or marks > 100)
# Display error message for invalid input

# Test Cases:

# Test Case 1:
# Input: marks = 85
# Output: B

# Test Case 2:
# Input: marks = 59
# Output: F

# Test Case 3:
# Input: marks = 101
# Output: Invalid marks. Please enter marks between 0 and 100.

def grade_calculator(marks):
    if (type(marks) == int or type(marks) == float) and marks >= 0 and marks <= 100:
        if(marks >= 90 and marks <= 100):
            print("A")
        elif(marks >= 80 and marks < 90):
            print("B")
        elif(marks >= 70 and marks < 80):
            print("C")
        elif(marks >= 60 and marks < 70):
            print("D")
        else:
            print("F")
    elif marks < 0 and marks > 100:
        print("Please enter marks between 0 and 100.")
    else:
        print("Invalid input, Enter a Number between 0 and 100")

# test case 1:
grade_calculator(85)

#test case 2:
grade_calculator(59)

# test case 3:
grade_calculator(101)

# test case 4: 
grade_calculator(0)

# test case 5:
grade_calculator(66.66)

#test case 6:
grade_calculator(-1)

#test case 7:
try:
    a = float(input("Enter marks: "))
    grade_calculator(a)
except Exception as e:
    print("Invalid datatype as input, Enter a number. ")


