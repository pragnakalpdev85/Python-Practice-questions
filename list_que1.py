# Question 1: Find Second Largest Element
# Write a program that takes a list of integers as input and finds the second largest element in the list.

# Rules:
# No in-built functions allowed (except input() and print())
# Must use loops to find the second largest
# Handle edge cases (list with less than 2 elements, all elements same)
# Do not sort the list

# Test Cases:

# Test Case 1:
# Input: [10, 20, 4, 45, 99]
# Output: 45

# Test Case 2:
# Input: [5, 5, 5, 5]
# Output: No second largest element

# Test Case 3:
# Input: [100, 50, 75, 25]
# Output: 75

def find_second_largest(input_list):
    try:
        largest = float('-inf')
        second_largest = float('-inf')

        #conparing and assigning value to max and second max
        for i in input_list:
            if i > largest:
                second_largest = largest
                largest = i
            elif i > second_largest and i != largest:
                second_largest = i

        #printing result
        print(f"{second_largest}" if second_largest != float('-inf') else "No second largest element")

    except TypeError as e:
        print("Invalid input data type, ",e)

#test case 1:
find_second_largest([10, 20, 4, 45, 99])

#test case 2:
find_second_largest([5, 5, 5, 5])

#test case 3:
find_second_largest([100, 50, 75, 25])

#test case 4:
find_second_largest([1,2])

#test case 5:
find_second_largest([1,])

#test case 6:
find_second_largest([1,"hello"])

#test case 7:
try:
    input_list = []
    print("Write stop to End input.")
    while True:
        list_elements = input("Enter Element :")
        if list_elements == "stop":
            break
        input_list.append(int(list_elements))

    find_second_largest(input_list)
except Exception:
    print("Input data type is not valid, please enter a list")



