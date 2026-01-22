# Question 3: Find Key with Maximum Value
# Write a program that takes a dictionary with integer values as input and finds the key with the maximum value without using any in-built functions.

# Rules:
# No in-built functions allowed (except input() and print())
# Must use loops to find maximum value
# Handle edge cases (empty dictionary, multiple keys with same max value)
# Return the first key found with maximum value

# Test Cases:

# Test Case 1:
# Input: {'a': 10, 'b': 50, 'c': 30}
# Output: 'b'

# Test Case 2:
# Input: {'x': 100, 'y': 100, 'z': 50}
# Output: 'x'

# Test Case 3:
# Input: {'p': 5}
# Output: 'p'

def key_with_maxval(input_dictionary):
    try:
        max_val = float('-inf')
        max_key = ''

        #travesing through dictionary to find maximum value and it's key
        for i in input_dictionary:
           if input_dictionary[i] > max_val:
               max_val = input_dictionary[i]
               max_key = i

        print(f"'{max_key}'")

    except TypeError as e:
        print("Invalid input type, ",e)

#test case 1:
key_with_maxval({'a': 10, 'b': 50, 'c': 30, 'd' : 50})

#test case 2:
key_with_maxval({'x': 100, 'y': 100, 'z': 50})

#test case 3:
key_with_maxval({'p': 5})

#test case 4:
key_with_maxval({'a': 10, 'b': 50, 'c': 30, 'd' : 50, 'e' : 50, 'f' : 50})

#test case 5:
key_with_maxval({})

#test case 6:
try:
    input_dict = {}
    size = int(input("enter the number of key-value pairs: "))

    i = 0
    while i < size:
        key = input("enter key: ")
        value = float(input("enter value: "))
        input_dict[key] = value
        i += 1
    
    key_with_maxval(input_dict)
except TypeError as e:
    print("Invalid Input type, ",e)
except ValueError as e:
    print("Invalid input value, ",e)

