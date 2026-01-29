# Question 5: Find Factorial
# Write a program to calculate the factorial of a non-negative integer using loops.

# Rules:
# No in-built functions allowed (except input() and print())
# Must use loops
# Handle edge cases (n = 0, negative numbers)
# Error handling for invalid input

# Test Cases:

# Test Case 1:
# Input: 5
# Output: 120

# Test Case 2:
# Input: 0
# Output: 1

# Test Case 3:
# Input: 7
# Output: 5040

def factorial(n):
    if type(n) == int and n >= 0:
        fact = 1
        #looping from 1 to n
        for i in range(1,n+1):
            fact *= i
        print(fact)
        
    else:
        print("Enter valid number.")


#test case 1:
factorial(0)

#test case 2:
factorial(5)

#test case 2:
factorial(7)

#test case 4:
factorial(-5)



