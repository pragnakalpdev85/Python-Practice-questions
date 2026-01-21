# Question 5: Reverse a Tuple
# Write a program that takes a tuple as input and returns a new tuple with elements in reverse order without using any in-built reverse functions.

# Rules:
# No in-built functions allowed (except input() and print())
# Must use loops to reverse
# Handle edge cases (empty tuple, single element)
# Create and return a new tuple

# Test Cases:

# Test Case 1:
# Input: (1, 2, 3, 4, 5)
# Output: (5, 4, 3, 2, 1)

# Test Case 2:
# Input: ('a', 'b', 'c')
# Output: ('c', 'b', 'a')

# Test Case 3:
# Input: (100,)
# Output: (100,)

def reverse_tuple(input_tuple):
    try:
        #counting size of tuple
        size = 0
        for i in input_tuple:
            size += 1

        #adding element from last to first in answer tuple
        ans_tuple = tuple(())
        size -= 1
        while size >= 0:
            ans_tuple += (input_tuple[size],)
            size -= 1

        return ans_tuple
            
    except TypeError as e:
        print("Invalid input type, ",e)

#test case 1:
print(reverse_tuple((1, 2, 3, 4, 5)))

#test case 2:
print(reverse_tuple(('a', 'b', 'c')))

#test case 3:
print(reverse_tuple((100,)))

#test case 4:
print(reverse_tuple(()))

#Test case 5:
try:
    input_tuple = tuple(())
    list_size = int(input("Enter the size of the touple: "))
    i = 0
    while i < list_size:
        element = input(f"Enter element {i+1}: ")
        input_tuple += (element,)
        i += 1

    print(reverse_tuple(input_tuple))
except TypeError as e:
    print("Invalid input, ",e)
except ValueError as e:
    print("Invalid input, ",e)