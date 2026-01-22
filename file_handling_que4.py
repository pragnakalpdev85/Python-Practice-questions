# Question 4: Count Word Frequency in File
# Write a program that reads a text file and creates a frequency count of each word, then writes the results to a new file.

# Rules:
# You can use open(), read(), write(), close() functions
# Must use loops and dictionary to count frequency
# Handle edge cases (empty file, punctuation handling)
# Case-insensitive counting
# Proper error handling required

# Test Cases:

# Test Case 1:
# Input: File contains "hello world hello"
# Output: New file contains:
# hello: 2
# world: 1

# Test Case 2:
# Input: File contains "Python Python python"
# Output: New file contains:
# python: 3

# Test Case 3:
# Input: File contains "a a b b b"
# Output: New file contains:
# a: 2
# b: 3

def word_frequency(file_name,output_file):
    try:
        file = open(file_name,'r')
        file_data = file.read()
        file.close()

        #calculating string length
        data_size = 0
        for i in file_data:
            data_size += 1

        ans_dict = {}
        key_list = []
        i = 0
        word = ''

        upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower_alpha = "abcdefghijklmnopqrstuvwxyz"

        #comparing word with find and if match than replace
        while i < data_size:
            character = file_data[i]
            #converting uppercase to lower case
            if file_data[i] >= "A" and file_data[i] <= "Z":
                index = 0
                for j in upper_alpha:
                    if(file_data[i] == j):
                        break
                    index += 1
                character = lower_alpha[index]
                    
            #if the character is space or last character or newline character
            if file_data[i] == ' ' or i == data_size-1 or file_data[i] == '\n':

                #last character put in word
                if i == data_size-1:
                    word += character
                
                #find if word is already present in key list or not
                present = False
                for j in key_list:
                    if word == j and word:
                        present = True
                        break
                
                #if word is not empty or space 
                if word != ' ' and word != '' and word != "\n":

                    #if key is present than increment in dictionary
                    if present == True:
                        temp = ans_dict[word] + 1
                        ans_dict[word] = temp
                        word = ''
                    #else put new key and value as 1 in dictionary
                    else:
                        ans_dict[word] = 1
                        key_list += [word,]
                        word = ''
            else:
                word += character
            i += 1

        file2 = open(output_file,"w")
        for i in ans_dict:
            file2.write(f"{i}: {ans_dict[i]}\n")
        file2.close()

        return f"New file contains {ans_dict}"


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
    ans = word_frequency(input_file_name, output_file_name)
    print(ans)
except TypeError as e:
    print("Invalid input, ",e)
except ValueError as e:
    print("Invalid input, ",e)

