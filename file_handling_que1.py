# Question 1: Count Lines, Words, and Characters
# Write a program that reads a text file and counts the total number of lines, words, and characters in it.

# Rules:
# You can use open(), read(), close() functions
# Must use loops to count words and characters
# Handle edge cases (empty file, file not found)
# Proper error handling required

# Test Cases:

# Test Case 1:
# Input: File contains "Hello World
#                       Python Programming"
# Output: Lines: 2, Words: 4, Characters: 30

# Test Case 2:
# Input: File contains "Test"
# Output: Lines: 1, Words: 1, Characters: 4

# Test Case 3:
# Input: Empty file
# Output: Lines: 0, Words: 0, Characters: 0

def count_lines_words_characters(file_name):
    try:
        file = open(file_name,'r')
        file_data = file.read()
        file.close()

        line_count = 0
        word_count = 0
        character_count = 0

        #calculating string size
        data_size = 0
        for i in file_data:
            data_size += 1

        j = 0
        word = ''
        #looping through file data
        for i in file_data:

            #character is new line or last character increment line count
            if j == data_size-1 or i == '\n':
                if word != '':
                    word_count += 1
                    line_count += 1
                    word = ''
                else:
                    line_count += 1

            #character is space and word is there then increment word count
            elif i == " ":
                if word != '':
                    word_count += 1
                    word = ''
            else:
                word += i

            character_count += 1
            j += 1
    

        return f"Lines: {line_count}, Words: {word_count}, Characters: {character_count}"

    except FileNotFoundError as e:
        print("File Not Found", e)
    except OSError as e:
        print("Given File name is not defined, ",e)
    except TypeError as e:
        print("Invalid input, ",e)

# test case 1:
try:
    input_file_name = input("Enter file name: ")
    ans = count_lines_words_characters(input_file_name)
    print(ans)
except TypeError as e:
    print("Invalid input, ",e)
except ValueError as e:
    print("Invalid input, ",e)
