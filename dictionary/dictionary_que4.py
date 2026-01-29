# Question 4: Invert Dictionary
# Write a program that takes a dictionary as input and inverts it (keys become values and values become keys). Assume all values are unique.

# Rules:
# No in-built functions allowed (except input() and print())
# Must use loops to invert dictionary
# Handle edge cases (empty dictionary)
# Create a new inverted dictionary

# Test Cases:

# Test Case 1:
# Input: {'a': 1, 'b': 2, 'c': 3}
# Output: {1: 'a', 2: 'b', 3: 'c'}

# Test Case 2:
# Input: {'name': 'John', 'age': '25'}
# Output: {'John': 'name', '25': 'age'}

# Test Case 3:
# Input: {'x': 100}
# Output: {100: 'x'}

def invert_dictionary(input_dictionary):
    try:
        ans_dict = {}

        #travesing through dictionary to replace value with key and key with value
        for i in input_dictionary:
           ans_dict[input_dictionary[i]] = i

        return ans_dict

    except TypeError as e:
        print("Invalid input type, ",e)

#test case 1:
ans1 = invert_dictionary({'a': 1, 'b': 2, 'c': 3})
print(ans1)

#test case 2:
ans2 = invert_dictionary({'name': 'John', 'age': '25'})
print(ans2)

#test case 3:
ans3 =  invert_dictionary({'x': 100})
print(ans3)

#test case 4:
try:
    input_dict = {}
    size = int(input("enter the number of key-value pairs: "))

    i = 0
    while i < size:
        key = input("enter key: ")
        value = input("enter value: ")
        input_dict[key] = value
        i += 1
    
    ans4 = invert_dictionary(input_dict)
    print(ans4)
except TypeError as e:
    print("Invalid Input type, ",e)
except ValueError as e:
    print("Invalid input value, ",e)


