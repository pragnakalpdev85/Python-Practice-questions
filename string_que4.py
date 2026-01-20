# Question 4: Count Character Frequency
# Write a program that takes a string and a character as input, and counts how many times that character appears in the string (case-insensitive).

# Rules:
# No in-built functions allowed (except input() and print())
# Must use loops to iterate through string
# Handle edge cases (character not in string, empty string)
# Case-insensitive comparison

# Test Cases:

# Test Case 1:
# Input: string = "Programming", character = "g"
# Output: 2

# Test Case 2:
# Input: string = "Hello World", character = "o"
# Output: 2

# Test Case 3:
# Input: string = "Python", character = "z"
# Output: 0

def count_frequency(input_str, character):
    #validating input data type
    if type(input_str) == str or type(input_str) == int or type(input_str) == float:
        input_str = str(input_str)

        upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower_alpha = "abcdefghijklmnopqrstuvwxyz"

        #calculating character length
        len_character = 0
        for i in character:
            len_character += 1
        
        #validate character input 
        if len_character == 1:
            #conveting char to lower case
            if character >= "A" and character <= "Z":
                index = 0
                for j in upper_alpha:
                    if(i == j):
                        break
                    index += 1
                character = lower_alpha[index]

            count = 0
            #counting frequency
            for i in input_str:
                #if i is uppercase converting and counting
                if i >= "A" and i <= "Z":
                    index = 0
                    for j in upper_alpha:
                        if(i == j):
                            break
                        index += 1 
                    if i == lower_alpha[index]:
                        count += 1 
                #counting if i and character are same
                elif i == character:
                    count += 1

            print(count)
        else:
            print("Invalid input character, Character length should not be more or less than 1")

    else:
        print("Invalid datatype as input, Enter a String.")

#test case 1:
count_frequency("Programming","g")

#test case 2:
count_frequency("Hello World","o")

#test case 3:
count_frequency("Python","z")

#test case 4:
input_str = input("Enter a String: ")
character = input("Enter a character: ")
count_frequency(input_str,character)

