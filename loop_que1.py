#question 1: Sum of Even Numbers
#Write a program that takes a positive integer n as input and calculates the sum of all even numbers from 1 to n (inclusive).

# Rules:
# No in-built functions allowed (except input() and print())
# Must use loops
# Handle edge cases (n < 1)

# Test Cases:

# Test Case 1:
# Input: n = 10
# Output: 30
# Explanation: 2 + 4 + 6 + 8 + 10 = 30

# Test Case 2:
# Input: n = 1
# Output: 0
# Explanation: No even numbers from 1 to 1

# Test Case 3:
# Input: n = 15
# Output: 56
# Explanation: 2 + 4 + 6 + 8 + 10 + 12 + 14 = 56

#code
def sum_of_evens(n):

    sum = 0

    if not n < 0:
        #looping from 1 to n
        for i in range(1,n+1):
            #filtering even numbers and adding it to sum.
            if i%2 == 0:
                sum += i
    
    print(sum)

#test case 1:
sum_of_evens(10)

#test case 2:
sum_of_evens(1)

#test case 3:
sum_of_evens(15)

#extra test case:
sum_of_evens(-3)