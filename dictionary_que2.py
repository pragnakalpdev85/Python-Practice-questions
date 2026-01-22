# uestion 2: Merge Two Dictionaries
# Write a program that takes two dictionaries as input and merges them. If a key exists in both dictionaries, sum their values.

# Rules:
# No in-built functions allowed (except input() and print())
# Must use loops to merge dictionaries
# Handle edge cases (empty dictionaries, no common keys)
# Create a new dictionary with merged values

# Test Cases:

# Test Case 1:
# Input: dict1 = {'a': 10, 'b': 20}, dict2 = {'b': 30, 'c': 40}
# Output: {'a': 10, 'b': 50, 'c': 40}

# Test Case 2:
# Input: dict1 = {'x': 5}, dict2 = {'y': 10, 'z': 15}
# Output: {'x': 5, 'y': 10, 'z': 15}

# Test Case 3:
# Input: dict1 = {}, dict2 = {'a': 1, 'b': 2}
# Output: {'a': 1, 'b': 2}

def dictionary_input():
    try:
        d = {}
        n = int(input("enter the number of key-value pairs: "))

        i = 0
        while i < n:
            key = input("enter key: ")
            value = float(input("enter value: "))
            d[key] = value
            i += 1

        return d
    except TypeError as e:
        print("Invalid Input type, ",e)
    except ValueError as e:
        print("Invalid input value, ",e)


def merge_dictionaries(input_dictionary1, input_dictionary2):
    try:
        key_list = []
        ans_dict = {}
       
        #traversing through dictionary 1 and puting it into ans dictionary
        for i in input_dictionary1:
            ans_dict[i] = input_dictionary1[i]
            key_list += [i,]

        #checking keys from key list is present or not
        for i in input_dictionary2:
            flag = False
            for j in key_list:
                if i == j:
                    flag = True
                    break
            #key is present in key list than sum dictionary 1 value and dictionary 2 value.
            if flag == True:
                temp = ans_dict[i]
                ans_dict[i] = temp+input_dictionary2[i]
            else:
                ans_dict[i] = input_dictionary2[i]

        return ans_dict
        
    except TypeError as e:
        print("Invalid input type, ",e)

#test case 1:
ans1 = merge_dictionaries({'a': 10, 'b': 20},{'b': 30, 'c': 40})
print(ans1)

#test case 2:
ans2 = merge_dictionaries({'x': 5},{'y': 10, 'z': 15})
print(ans2)

#test case 3:
ans3 = merge_dictionaries({},{'a': 1, 'b': 2})
print(ans3)

#test case 4:
try:
    print("Enter Dictionary 1: ")
    input_dictionary1 = dictionary_input()
    print("Enter Dictionary 2: ")
    input_dictionary2 = dictionary_input()

    ans4 = merge_dictionaries(input_dictionary1, input_dictionary2)
    print(ans4)
except TypeError as e:
    print("Invalid Input, ",e)




