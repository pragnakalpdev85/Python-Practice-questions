# Question 1: Find Maximum and Minimum in Tuple
# Write a program that takes a tuple of integers as input and finds both the maximum and minimum elements without using any in-built functions.

# Rules:
# No in-built functions allowed (except input() and print())
# Must use loops to find max and min
# Handle edge cases (single element tuple, all elements same)
# Return both max and min values

# Test Cases:

# Test Case 1:
# Input: (10, 5, 20, 15, 30)
# Output: Maximum: 30, Minimum: 5

# Test Case 2:
# Input: (7, 7, 7, 7)
# Output: Maximum: 7, Minimum: 7

# Test Case 3:
# Input: (-5, -10, -3, -8)
# Output: Maximum: -3, Minimum: -10

def find_min_max(input_tuple):
    try:
        maximum = float('-inf')
        minimum = float('inf')
        #looping through touple to find minimum and maximum
        for i in input_tuple:
            if i > maximum:
                maximum = i
            if i < minimum:
                minimum = i
        print(f"Maximum: {maximum}, Minimum: {minimum}" if maximum != float('-inf') and minimum != float('inf') else "Empty tuple")
    except TypeError as e:
        print("Invalid input type, ",e)

#test case 1:
find_min_max((10, 5, 20, 15, 30))

#test case 2:
find_min_max((7, 7, 7, 7))

#test case 3:
find_min_max((-5, -10, -3, -8))

#test case 4:
try:
    input_tuple = tuple(())
    list_size = int(input("Enter the size of the touple: "))
    i = 0
    while i < list_size:
        element = float(input(f"Enter element {i+1}: "))
        input_tuple += (element,)
        i += 1

    find_min_max(input_tuple)
except Exception:
    print("Invalid input, please enter Integer or float as input.")