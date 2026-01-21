# Question 2: Count Element Occurrences in Tuple
# Write a program that takes a tuple and an element as input, and counts how many times that element appears in the tuple.

# Rules:
# No in-built functions allowed (except input() and print())
# Must use loops to count occurrences
# Handle edge cases (empty tuple, element not in tuple)
# Element can be of any type (int, string, etc.)

# Test Cases:

# Test Case 1:
# Input: tuple = (1, 2, 3, 2, 4, 2, 5), element = 2
# Output: 3

# Test Case 2:
# Input: tuple = ('a', 'b', 'c', 'a', 'a'), element = 'a'
# Output: 3

# Test Case 3:
# Input: tuple = (10, 20, 30), element = 40
# Output: 0

def count_element(input_tuple, element):
    try:
        count = 0
        #looping through tuple and counting element's occurence
        for i in input_tuple:
            if i == element:
                count += 1

        print(count)
    except TypeError as e:
        print("Invalid input type, ",e)

#test case 1:
count_element((1, 2, 3, 2, 4, 2, 5), 2)

#test case 2:
count_element(('a', 'b', 'c', 'a', 'a'), 'a')

#test case 3:
count_element((10, 20, 30), 40)

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
    count_element(input_tuple, element)
except TypeError as e:
    print("Invalid input, ",e)
except ValueError as e:
    print("Invalid input, ",e)

