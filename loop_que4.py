# Question 4: Print Pattern
# Write a program that takes a positive integer n and prints the following pattern:

# For n = 4:
# 1
# 1 2
# 1 2 3
# 1 2 3 4

# Rules:
# No in-built functions allowed (except input() and print())
# Must use nested loops
# Handle edge cases (n < 1)

# Test Cases:

# Test Case 1:
# Input: n = 3
# Output:
# 1
# 1 2
# 1 2 3

# Test Case 2:
# Input: n = 1
# Output:
# 1

# Test Case 3:
# Input: n = 5
# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

def print_pattern(n):
    if type(n) == int and n > 0:
        #looping from 1 to n
        for i in range(1,n+1):
            #looping from 1 to i
            for j in range(1,i+1):
                print(j,end=" ")
            print("")
    else:
        print("Invalid input, Enter valid possitive number.")

#test case 1:
print_pattern(3)

#test case 4:
print_pattern(1)

#test case 3:
print_pattern(5)

#test case 4:
print_pattern(-1)
