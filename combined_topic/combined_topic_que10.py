# Question 10: Pattern Matcher in Files 
# Write a program that searches for specific patterns in text files: phone numbers (XXX-XXX-XXXX), email addresses, and URLs. Create a dictionary with pattern types as keys and list of matches as values. Write results to output file.

# Rules:
# You can use file operations: open(), read(), write(), close()
# Must use loops, strings, lists, dictionaries, and conditionals
# Create functions for each pattern type
# Handle edge cases (no matches, malformed patterns)
# Case-insensitive for email/URL matching

# Test Cases:

# Test Case 1:
# Input file: "Contact: 123-456-7890, Email: test@email.com"
# Output:
# Phone Numbers: ['123-456-7890']
# Emails: ['test@email.com']
# URLs: []

# Test Case 2:
# Input file: "Visit https://example.com or call 999-888-7777"
# Output:
# Phone Numbers: ['999-888-7777']
# Emails: []
# URLs: ['https://example.com']

# Test Case 3:
# Input file: "No patterns here"
# Output:
# Phone Numbers: []
# Emails: []
# URLs: []

def string_to_lower_case(data: str) -> str:
    '''
    converts string into lowercase

    Args:
        data (str): data to be converted into lowercase
    Returns:
        str: converted data 
    '''

    name_size = 0
    for char in data:
        name_size += 1

    upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_alpha = "abcdefghijklmnopqrstuvwxyz"

    index = 0
    lower_data = ''
    #manually converting upercase to lower case
    while index < name_size:
        character = data[index]

        #converting uppercase to lower case
        if data[index] >= "A" and data[index] <= "Z":
            index2 = 0
            for j in upper_alpha:
                if(data[index] == j):
                    break
                index2 += 1
            character = lower_alpha[index2]
            lower_data += character
        else:
            lower_data += character
        index += 1

    return lower_data

def read_file(file_name: str) -> dict:
    '''
    read data and creat list of data
    
    Args:
        file_name (str): name of the input file
    Returns:
        list: list of tuples with name and marks
    '''
    data_dict = {}

    #validating file format
    flag = False
    check_word1 = ''
    for chars in file_name:
        if flag == True:
            check_word1 += chars
        if chars == '.':
            flag = True
    
    if check_word1 != 'txt':
            raise FileNotFoundError()

    with open(file_name, 'r') as file:
        list_words = []
        for lines in file:
            line = lines
            data_size = 0

            #calculating length of the line
            for char in line:
                data_size += 1

            index = 0
            word = ''
            count_words = 0
            for chars in line:
                #add all words in the list
                if chars == ',' or chars == '\n' or index == data_size-1 or chars == " ":
                    if index == data_size-1 and chars != " " and chars != "\n":
                        word += chars
                
                    if word != '':
                        list_words += [word,]
                        count_words += 1
                        word = ''
                else:
                    if chars != " ":
                        word += chars
                index += 1

        return list_words

def find_pattern(input_file_name: str, output_file_name: str) -> str:
    '''
    finds patterns from input data file
    
    Args:
        input_file_name (str): name of the input file
        output_file_name (str): name of the output file
    Returns:
        str: returns pattern matching values
    '''
    try:

        word_list = read_file(input_file_name)
        if word_list == []:
            return "There is no content in file."

        ans_dict = {'number': [],'email': [],'url': []}

        for word in word_list:
            #counting size of word
            word_size = 0
            for char in word:
                word_size += 1
            
            #validating if the word is phone number or not
            if word_size == 12:
                number = ''
                index = 0
                for char in word:
                    if char >= '0' and char <= '9' and index != 3 and index != 7:
                        number += char
                    elif char == '-' and (index == 3 or index == 7):
                        number += char
                    else:
                        break
                    index += 1

                present = False
                for numbers in ans_dict['number']:
                    if numbers == number:
                        present = True
                        break

                if index == word_size and present != True:
                    ans_dict['number'] += [number,]

            #validating if the word is url or not
            elif word_size > 12:
                url_start = "https://"
                url_end = ".com"

                index = 0
                flag = False
                while index < 8:
                    if url_start[index] != word[index]:
                        flag = True
                        break
                    index += 1
                
                index = word_size-4
                index2 = 0
                while index < word_size:
                    if url_end[index2] != word[index]:
                        flag = True
                        break
                    index2 += 1
                    index += 1

                present = False
                for urls in ans_dict['url']:
                    if urls == word:
                        present = True
                        break
                
                if flag != True and present != True:
                    ans_dict['url'] += [word,]

            #validating if the word is email or not
            if word_size  > 10:
                email_end = "@email.com"
                
                index = word_size-10
                index2 = 0
                flag = False
                while index < word_size:
                    if email_end[index2] != word[index]:
                        flag = True
                        break
                    index2 += 1
                    index += 1
                
                present = False
                for emails in ans_dict['email']:
                    if emails == word:
                        present = True
                        break
                if present != True and flag != True:
                    ans_dict['email'] += [word,]

        output = f"Phone Numbers: {ans_dict['number']}\nEmails: {ans_dict['email']}\nURLs: {ans_dict['url']}"

        with open(output_file_name,'w') as file:
            file.write(output)

        return output

    except FileNotFoundError as e:
        print("File Not Found or the given file name is incorrect, It should be a text file.")
    except OSError as e:
        print("Given File name is not defined")

def main():
    try:
        flag = False
        while flag == False:
            input_file_name = input("Enter input file name: ")
            try:
                with open(input_file_name,'r') as f:
                    flag = True
            except FileNotFoundError:
                print("File not found Enter name again")

        flag = False
        output_file_name = ''
        while flag == False:
            output_file_name = input("Enter output file name: ")
            try:
                with open(input_file_name,'r') as f:
                    flag = True
            except FileNotFoundError:
                print("File not found Enter name again")

        ans = find_pattern(input_file_name, output_file_name)
        print(ans)

    except FileNotFoundError as e:
        print("File Not Found.")
    except OSError as e:
        print("Given File name is not defined.")
    except TypeError as e:
        print("Invalid file name")
    except ValueError as e:
        print("Invalid file name.")
    
if __name__ == "__main__":
    main()