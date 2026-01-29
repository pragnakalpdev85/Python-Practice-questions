# Question 2: Find GCD (Greatest Common Divisor)
# Write a function find_gcd(num1, num2) that finds the GCD of two positive integers using the Euclidean algorithm.

# Rules:
# No in-built functions allowed (except input() and print())
# Must create and use a function
# Handle edge cases (one or both numbers are 0)
# Must use loops or recursion

# Test Cases:

# Test Case 1:
# Input: num1 = 48, num2 = 18
# Output: 6

# Test Case 2:
# Input: num1 = 100, num2 = 50
# Output: 50

# Test Case 3:
# Input: num1 = 17, num2 = 19
# Output: 1

def find_gcd(num1, num2):
    #validating input datatype
    if type(num1) == int and type(num2) == int:

        #validating entered number is negative or not
        if num2 > 0 and num1 > 0:
            #looping till remainder becomes 0
            while(num1 > 0):
                temp = num1
                num1 = num2%num1
                num2 = temp
            print(num2)
        else:
            print("Invalid input, Enter possitive integers.")
    else:
        print("Invalid datatype as input, Enter a possitive integer.")

#test case 1:
find_gcd(48, 18)

#test case 2:
find_gcd(100, 50)

#test case 3:
find_gcd(17,19)

#test case 4:
try:
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    find_gcd(a, b)
except Exception as e:
    print("Invalid datatype as input, Enter a number. ")

