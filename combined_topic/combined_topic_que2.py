# Question 2: Word Analysis Tool 
# Write a program that reads a text file and creates a comprehensive analysis including: total words, unique words, word frequency dictionary, and the top 3 most frequent words. Write the analysis to a new file.

# Rules:
# You can use file operations: open(), read(), write(), close()
# Must use loops, dictionaries, sets, and string operations
# Create functions for counting and sorting
# Handle edge cases (empty file, punctuation)
# Case-insensitive analysis

# Test Cases:

# Test Case 1:
# Input file: "hello world hello python world world"
# Output file:
# Total Words: 6
# Unique Words: 3
# Word Frequency:
# hello: 2
# world: 3
# python: 1
# Top 3 Words: world(3), hello(2), python(1)

# Test Case 2:
# Input file: "test test test"
# Output file:
# Total Words: 3
# Unique Words: 1
# Word Frequency:
# test: 3
# Top 3 Words: test(3)

# Test Case 3:
# Input file: "a b c d e"
# Output file:
# Total Words: 5
# Unique Words: 5
# Word Frequency:
# a: 1
# b: 1
# c: 1
# d: 1
# e: 1
# Top 3 Words: a(1), b(1), c(1)

def count_words_frequency(data: str) -> dict:
    '''
    countes words and its frequency in given input string

    Args:
        data (str): input data from file
    Returns:
        dict: dictionary of words with its frequency as values
    '''

    #calculating string length
    data_size = 0
    for character in data:
        data_size += 1

    frequency_dict = {}
    key_list = []
    set_keys = {}
    index = 0
    word = ''

    upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_alpha = "abcdefghijklmnopqrstuvwxyz"

    while index < data_size:
        character = data[index]
        #converting uppercase to lower case
        if data[index] >= "A" and data[index] <= "Z":
            index = 0
            for j in upper_alpha:
                if(data[index] == j):
                    break
                index += 1
            character = lower_alpha[index]
                    
        #if the character is space or last character or newline character
        if data[index] == ' ' or index == data_size-1 or data[index] == '\n':

            #last character put in word
            if index == data_size-1:
                word += character
                
            #find if word is already present in key list or not
            present = False
            for key in set_keys:
                if word == key and word:
                    present = True
                    break
                
            #if word is not empty or space 
            if word != ' ' and word != '' and word != "\n":

                #if key is present than increment in dictionary
                if present == True:
                    temp = frequency_dict[word] + 1
                    frequency_dict[word] = temp
                    word = ''
                #else put new key and value as 1 in dictionary
                else:
                    frequency_dict[word] = 1
                    key_list += [word,]
                    set_keys = set(key_list)
                    word = ''
        else:
            word += character
        index += 1

    return frequency_dict

def sort_word_freq(words_freq: dict) -> set:
    '''
    sort the dictionary keys according to the values

    Args:
        words_freq (dict): contains words as keys and it's frequency as values
    Returns:
        set:set of sorted keys
    '''
    list_keys = []
    dict_size = 0
    #calculating size of the dictionary
    for index in words_freq:
        dict_size += 1
        list_keys += [index,]

    index1 = 0
    #sorting keys of list based on the values
    while index1 < dict_size:
        index2 = 0
        while index2 < (dict_size-index1-1):
            if words_freq[list_keys[index2]] < words_freq[list_keys[index2+1]]:
                temp = list_keys[index2]
                list_keys[index2] = list_keys[index2+1]
                list_keys[index2+1] = temp
            index2 += 1
        index1 += 1

    return list_keys

def word_analysis_tool(input_file_name: str, output_file_name: str) -> str:
    try:
        file_data = ''
        with open(input_file_name, 'r') as file:
            file_data = file.read()

        Total_words = 0
        unique_words = 0
        output_data = 'Word Frequency:\n'

        ans_dict = count_words_frequency(file_data)

        #counting total words and unique words
        for index in ans_dict:
            Total_words += ans_dict[index]
            output_data += f"{index}: {ans_dict[index]}\n"
            unique_words += 1

        output_data = f"Total words: {Total_words}\nUnique words: {unique_words}\n" + output_data
        
        #sorting index and adding top 3 to the output data
        key_list = sort_word_freq(ans_dict)
        output_data += f"Top 3 words: {key_list[0]}({ans_dict[key_list[0]]}), {key_list[1]}({ans_dict[key_list[1]]}), {key_list[1]}({ans_dict[key_list[1]]})"

        with open(output_file_name,'w') as file:
            file.write(output_data)

        return output_data
        
    except FileNotFoundError as e:
        print("File Not Found: ",e)
    except OSError as e:
        print("Given File name is not defined: ",e)
    except TypeError as e:
        print("Invalid input data. Please enter valid data types in input file: ",e)
    except ValueError as e:
        print("Invalid values as input, Please enter valid data in input file: ",e)
    


#defining main function
def main():
    try:
        input_file_name = input("Enter input file name: ")
        output_file_name = input("Enter output file name: ")

        ans = word_analysis_tool(input_file_name, output_file_name)
        print(ans)
    except TypeError as e:
        print("Invalid input, ",e)
    except ValueError as e:
        print("Invalid input, ",e)

    

if __name__ == "__main__":
    main()


