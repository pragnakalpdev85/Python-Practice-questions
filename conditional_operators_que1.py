# Question 1: Maximum of Three Numbers
# Write a program that takes three integers as input and prints the largest among them using conditional operators.

# Rules:
# No in-built functions allowed (except input() and print())
# Must use conditional operators (if, elif, else)
# Handle edge cases (all numbers equal, two numbers equal)

# Test Cases:

# Test Case 1:
# Input: a = 10, b = 25, c = 15
# Output: 25

# Test Case 2:
# Input: a = 50, b = 50, c = 30
# Output: 50

# Test Case 3:
# Input: a = -5, b = -10, c = -3
# Output: -3

def max_of_three(a, b, c):
    #checking inputs are numbers
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float) and (type(c) == int or type(c) == float) :

        if(a >= b and a >= c):
            print(a)
        elif(b > c):
            print(b)
        else:
            print(c)
    else:
        print("Enter valid numbers.")
    
#test case 1:    
max_of_three(10,10,15.5)

#test case 2:
max_of_three(50,50,30)

#test case 3:
max_of_three(-5,-10,-3)

#test case 4:
max_of_three(50,50,50)

#test case 5:
max_of_three(3,-1,2)