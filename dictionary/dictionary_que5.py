# Question 5: Group Anagrams
# Write a program that takes a list of strings as input and groups anagrams together using a dictionary. Anagrams are words with the same characters in different order.

# Rules:

# No in-built functions allowed (except input() and print())
# Must use loops to check for anagrams
# Handle edge cases (empty list, no anagrams)
# Create dictionary where keys represent sorted character patterns

# Test Cases:

# Test Case 1:

# Input: ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

# Output: {
#   'aet': ['eat', 'tea', 'ate'],
#   'ant': ['tan', 'nat'],
#   'abt': ['bat']
# }

# Test Case 2:
# Input: ['hello', 'world']
# Output: {
#   'ehllo': ['hello'],
#   'dlorw': ['world']
# }

# Test Case 3:
# Input: ['abc', 'bca', 'cab']
# Output: {
#   'abc': ['abc', 'bca', 'cab']
# }

def sort_string(input_string):
    try:
        ans_str = input_string

        #calculating string size
        str_size = 0
        for i in input_string:
            str_size += 1
        
        i = 0
        #soring the string
        while i < str_size:
            min_char = ans_str[i]
            j = i
            index = j
            #finding minimum character from string and its index
            while j < str_size:
                if ans_str[j] >= min_char:
                    min_char = ans_str[j]
                    index = j
                j += 1
            
            temp_str = min_char

            k = 0
            #in ans string puting minimum character first and than all the remaining characters
            while k < str_size:
                #all character except minimum character
                if k != index:
                    temp_str += ans_str[k]
                k += 1

            ans_str = temp_str
            i += 1
            
        return ans_str

    except TypeError as e:
        print("Invalid input type, ",e)


def group_anagrames(input_list):
    try:
        ans_dict = {}
        key_list = []

        #traversing through list and adding keys
        for i in input_list:
            key = sort_string(i)
            flag = False
            #check if key is present in key list or not
            for j in key_list:
                if j == key:
                    flag = True
                    break

            #key is present in key list then ad in dictionary
            if flag == True:
                ans_dict[key] += [i,]
            #key does not match than enter new entry 
            else:
                ans_dict[key] = [i,]
                key_list += [key]

        return ans_dict

    except TypeError as e:
        print("Invalid input type, ",e)

#test case 1:
ans1 =  group_anagrames(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
print(ans1)

#test case 2:
ans2 = group_anagrames(['hello', 'world'])
print(ans2)

#test case 3:
ans3 = group_anagrames(['abc', 'bca', 'cab'])
print(ans3)

#test case 4:
try:
    input_list = []
    list_size = int(input("Enter the size of the list: "))
    i = 0
    while i < list_size:
        element = input(f"Enter string {i+1}: ")
        input_list += [element,]
        i += 1


    ans4 = group_anagrames(input_list)
    print(ans4)
except Exception:
    print("Input data type is not valid, please enter a list")