# Question 4: Find Index of Element in Tuple
# Write a program that takes a tuple and an element as input, and returns the index of the first occurrence of that element. If the element is not found, return -1.

# Rules:
# No in-built functions allowed (except input() and print())
# Must use loops to search for the element
# Handle edge cases (empty tuple, element not found)
# Return only the first occurrence index

# Test Cases:

# Test Case 1:
# Input: tuple = (10, 20, 30, 40, 20), element = 20
# Output: 1

# Test Case 2:
# Input: tuple = ('apple', 'banana', 'cherry'), element = 'cherry'
# Output: 2

# Test Case 3:
# Input: tuple = (1, 2, 3, 4), element = 5
# Output: -1

def find_index(input_tuple, element):
    try:
        idx = 0
        #traversing through input_tuple to find index of element
        for i in input_tuple:
            if i == element:
                return idx
            idx += 1
        if idx == 0:
            return "Empty tuple."
        return -1
                
    except TypeError as e:
        print("Invalid input type, ",e)

#test case 1:
print(find_index((10, 20, 30, 40, 20),20))

#test case 2:
print(find_index(('apple', 'banana', 'cherry'), 'cherry'))

#test case 3:
print(find_index((1, 2, 3, 4),5))

#test case 4:
try:
    input_tuple = tuple(())
    list_size = int(input("Enter the size of the touple: "))
    i = 0
    while i < list_size:
        element = input(f"Enter element {i+1}: ")
        input_tuple += (element,)
        i += 1

    element = input("Enter the Element: ")
    print(find_index(input_tuple, element))
except TypeError as e:
    print("Invalid input, ",e)
except ValueError as e:
    print("Invalid input, ",e)