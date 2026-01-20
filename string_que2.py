# Question 2: Reverse Words in a String
# Write a program that takes a string as input and reverses each word in the string while maintaining the word order.

# Rules:
# No in-built functions allowed (except input() and print())
# Must use loops to process the string
# Handle edge cases (single word, multiple spaces between words)
# Maintain single space between words in output

# Test Cases:

# Test Case 1:
# Input: "Hello World"
# Output: "olleH dlroW"

# Test Case 2:
# Input: "Python Programming"
# Output: "nohtyP gnimmargorP"

# Test Case 3:
# Input: "Code"
# Output: "edoC"

def reverse_words(input_str):
    #validating input datatype
    if type(input_str) == str or type(input_str) == int or type(input_str) == float:
        input_str = str(input_str)
        output_str = ""

        last_idx = 0
        for i in input_str:
            last_idx += 1

        counter = 0
        start_index = 0
        #reversing string
        for i in input_str:
            
            #condition for separated words
            if i == ' ':
                end_idx = counter-1
                while end_idx >= start_index:
                    output_str += input_str[end_idx]
                    end_idx -= 1
                output_str += " "
                start_index = counter+1

            #condition for last word
            elif i == input_str[last_idx-1]:
                end_idx = last_idx-1
                while end_idx >= start_index:
                    output_str += input_str[end_idx]
                    end_idx -= 1
                start_index = last_idx

            counter += 1
        print(output_str)

    else:
        print("Invalid datatype as input, Enter a String.")

#test case 1:
reverse_words("Hello World")

#test case 2:
reverse_words("Python Programming")

#test case 3:
reverse_words("Code")

#test case 4:
input_string = input("Enter a String: ")
reverse_words(input_string)