# Question 3: Find and Replace in File
# Write a program that reads a file, finds all occurrences of a specific word, replaces it with another word, and writes the result to a new file.

# Rules:
# You can use open(), read(), write(), close() functions
# Must use loops to process and replace text
# Handle edge cases (word not found, empty file)
# Case-sensitive replacement
# Proper error handling required

# Test Cases:

# Test Case 1:
# Input: File contains "Hello World Hello", find = "Hello", replace = "Hi"
# Output: New file contains "Hi World Hi"

# Test Case 2:
# Input: File contains "Python is great", find = "Java", replace = "C++"
# Output: New file contains "Python is great"

# Test Case 3:
# Input: File contains "test test test", find = "test", replace = "exam"
# Output: New file contains "exam exam exam"

def find_and_replace(file_name, output_file_name, find, replace):
    try:
        file = open(file_name,'r')
        file_data = file.read()
        file.close()

        ans_data = ''
        word = ''

        #calculating string length
        data_size = 0
        for i in file_data:
            data_size += 1

        i = 0
        while i < data_size:
            #if there is space or new line character or the last character of the string 
            if file_data[i] == " " or file_data[i] == '\n' or i == data_size-1:
                
                #last word than add thw character to the word first
                if i == data_size-1:
                    word += file_data[i]
                
                #word is not empty and word is not space and word is equal to find
                if word != '' and word != ' ' and word == find:
                    ans_data += replace
                else:
                    ans_data += word + " "

                #adding space if there is space or
                if file_data[i] == " ":
                    ans_data += " "
                elif file_data[i] == "\n":
                    ans_data += "\n"
                
                word = ''
            else:
                word += file_data[i]
            i += 1


        output_file = open(output_file_name,"w")
        output_file.write(ans_data)
        output_file.close()

        return f"New file contains {ans_data}"


    except FileNotFoundError as e:
        print("File Not Found", e)
    except OSError as e:
        print("Given File name is not defined, ",e)
    except TypeError as e:
        print("Invalid input, ",e)

#test case 1:
try:
    input_file_name = input("Enter input file name: ")
    output_file_name = input("Enter output file name: ")
    find = input("Enter word for find: ")
    replace = input("Enter word for replace: ")

    ans = find_and_replace(input_file_name, output_file_name, find, replace)
    print(ans)
except TypeError as e:
    print("Invalid input, ",e)
except ValueError as e:
    print("Invalid input, ",e)

