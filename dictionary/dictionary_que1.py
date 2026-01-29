# Question 1: Count Character Frequency
# Write a program that takes a string as input and creates a dictionary with characters as keys and their frequencies as values.

# Rules:
# No in-built functions allowed (except input() and print())
# Must use loops to count frequency
# Handle edge cases (empty string, spaces and special characters)
# Create dictionary manually

# Test Cases:

# Test Case 1:
# Input: "hello"
# Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# Test Case 2:
# Input: "programming"
# Output: {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}

# Test Case 3:
# Input: "aaa"
# Output: {'a': 3}

def count_character_frequency(input_str):
    try:
        character_list = []
        ans_dict = {}

        #traversing through string 
        for i in input_str:
            #character is present in character list or not
            flag = False
            for j in character_list:
                if i == j:
                    flag = True
                    break
            
            #character is present in character list than increment character count in dictionary
            if flag == True:
                temp = ans_dict[i]
                ans_dict[i] = temp+1
            #if character is not present than enter new character in dictionary with count 1
            else:
                ans_dict[i] = 1
                character_list += [i,]

        return ans_dict
                
    except TypeError as e:
        print("Invalid input type, ",e)

#test case 1:
ans1 = count_character_frequency("hello")
print(ans1)

#test case 2:
ans2 = count_character_frequency("programming")
print(ans2)

#test case 3:
ans3 = count_character_frequency("aaa")
print(ans3)

#test case 4:
try:
    input_str = input("Enter a string: ")
    ans4 = count_character_frequency(input_str)
    print(ans4)
except TypeError as e:
    print("Invalid Input type, ",e)
except ValueError as e:
    print("Invalid input value, ",e)
    




