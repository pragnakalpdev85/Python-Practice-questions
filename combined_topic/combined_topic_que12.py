# Question 12: Text Formatter and Beautifier 
# Write a program that reads a text file and formats it by: removing extra spaces, capitalizing first letter of sentences, ensuring proper punctuation spacing, and breaking long lines (>80 characters) at word boundaries. Write formatted text to new file.

# Rules:

# You can use file operations: open(), read(), write(), close()
# Must use loops, strings, conditionals, and functions
# Create functions for each formatting rule
# Handle edge cases (empty file, already formatted text)
# Preserve paragraph breaks

# Test Cases:
# Test Case 1:
# Input: "hello   world.this is    a test."
# Output: "Hello world. This is a test."

# Test Case 2:
# Input: "python is great.   it's   easy to learn."
# Output: "Python is great. It's easy to learn."

# Test Case 3:
# Input: "a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d"
# Output:
# "A b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k
# l m n o p q r s t u v w x y z a b c d"
import os

def validate_filename_input(file_name: str) -> bool:
    '''
    validates file name input
    
    Args:
        name (str): name of the file
    returns:
        bool: file formate is correct or not
    '''
    #validating file formate
    flag = False
    check_word1 = ''

    for chars in file_name:
        if flag == True:
            check_word1 += chars
        if chars == '.':
            flag = True

    if check_word1 != 'txt':
        print("File formate is incorrect, Enter file name again")
        return False
    
    #file exist of not
    if not os.path.exists(file_name):
        print("File does not exist, Enter file name again")
        return False
    
    return True

def character_to_uppercase(character: str) -> str:
    '''
    converts character into uppercase
    
    Args:
        character (str): character to convert
    Returns:
        str: character converted to upper case
    '''
    upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_alpha = "abcdefghijklmnopqrstuvwxyz"

    index = 0
    for char in lower_alpha:
        if char == character:
            break
        index += 1

    return upper_alpha[index]

def character_to_lowercase(character: str) -> str:
    '''
    converts character into lowercase
    
    Args:
        character (str): character to convert
    Returns:
        str: character converted to lower case
    '''
    upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_alpha = "abcdefghijklmnopqrstuvwxyz"

    index = 0
    for char in upper_alpha:
        if char == character:
            break
        index += 1

    return lower_alpha[index]

def preserve_para(file_data: str) -> str:
    '''
    preserves paragraph at the start of line

    Args:
        file_data (str): data in file
    Returns:
        str: returns paragraph if present
    '''
    count_space = 0
    if file_data[0] == ' ':
        for char in file_data:
            if char == ' ':
                count_space += 1
            else:
                break
        
    if count_space > 2:
        return "    "
    else:
        return ''

def remove_extra_spaces(file_data: str) -> str:
    '''
    removes extra spaces from the data

    Args:
        file_data (str): input string data
    Returns:
        str: returns new data without extra spaces
    '''
    ans_str = ''
    prev_char = ''

    #looping through each character
    for char in file_data:
        #character is space than check prev character
        if char == ' ':
            #prev character is also space than continue
            if prev_char == ' ' or prev_char == '.' or prev_char == '?' or prev_char == "!":
                continue
            else:
                if ans_str != '':
                    ans_str += ' '
                prev_char = ' '
        else:
            ans_str += char
            prev_char = char
    
    return ans_str

def capitalize_first_letter(file_data: str) -> str:
    '''
    capitalizes first letter of every sentence

    Args:
        file_data (str): input string data
    Returns:
        str: returns new data with first letter of every line capitalized
    '''
    ans_str = ''
    prev_char = ''
    index = 0
    #looping through file data
    for char in file_data:
        #if prev character is end of the sentence symbol than conver character to capital
        if prev_char == '.' or prev_char == '?' or prev_char == "!" or index == 0:
            if char >= 'a' and char <= 'z':
                ans_str += character_to_uppercase(char)
            else:
                ans_str += char
            prev_char = char
        #convert other characters in sentence to lowercase
        else:
            if char >= 'A' and char <= 'Z':
                ans_str += character_to_lowercase(char)
            else:
                ans_str += char
            prev_char = char
        index += 1

    return ans_str
        
def format_punctuation_spacing(file_data: str) -> str:
    '''
    Ensures proper punctuation spacing

    Args:
        file_data (str): input string data
    Returns:
        str: returns new data with proper punctuation spacing
    '''
    data_size = 0
    for char in file_data:
        data_size += 1

    ans_str = ''
    prev_char = ''
    index = 0
    #looping through file data
    for char in file_data:
        #panctuation occurs then add panctuation and a space in ans string
        if char == '.' or char == ',' or char == '!' or char == '?' or char == ":" or char == ";":
            if index == data_size-1:
                ans_str += char
            else:
                ans_str += char + ' '
            prev_char = char
        #space occurs add to prev char
        elif char == ' ':
            prev_char = char
        #prev character is space than add space and character to the ans string
        elif prev_char == ' ':
            ans_str += ' '+char
            prev_char = char
        else:
            ans_str += char
            prev_char = char
        index += 1

    return ans_str

def break_long_lines(file_data: str) -> str:
    '''
    breaks line if characters in line are more than 80 

    Args:
        file_data (str): input string data
    Returns:
        str: returns new data with long lines breaked
    '''
    ans_str = ''
    char_count = 0
    #looping through file data
    for char in file_data:
        #break line if there is sentence termination punctuation or space and character count is over 80
        if (char ==  ' ' or char == '.') and char_count > 80:
            ans_str += '\n'
            char_count = 0
        else:
            ans_str += char

        char_count += 1

    temp_data = ans_str
    ans_str = ''
    prev_char = ''
    for char in temp_data:
        if prev_char == ' ':
            if char == '\n':
                ans_str += char
                prev_char = char
            else:
                ans_str += " " + char
                prev_char = char
        else:
            if char == ' ':
                prev_char = ' '
            else:
                ans_str += char
                prev_char = char

    return ans_str

def formate_beautify_text(input_file_name: str, output_file_name: str) -> str:
    '''
    formates and beautifies text from the input file.

    Args:
        input_file_name (str): name of the input file
        output_file_name (str): name of the output file
    Returns:
        str: formated and beautified text
    ''' 
    try:
        data = ''
        with open(input_file_name, 'r') as file:
            #formating the text
            for lines in file:
                flag = False
                for char in lines:
                    if char != " " and char != "\n":
                        flag = True
                        break

                if flag == True:
                    preserve_paragraph = preserve_para(lines)
                    ans_data = ''
                    ans_data = remove_extra_spaces(lines)
                    ans_data = capitalize_first_letter(ans_data)
                    ans_data = format_punctuation_spacing(ans_data)
                    ans_data = break_long_lines(ans_data)
                    data += preserve_paragraph + ans_data
                    
        if data == "":
            return "There is no content in file"
        
        data_size = 0
        for char in data:
            data_size += 1

        if data[data_size-1] == '\n':
            final = ''
            index = 0
            for char in data:
                if data_size-1 != index:
                    final += char
                index += 1
            data = final

        with open(output_file_name,'w') as file:
            file.write(data)        

        return data
    
    except FileNotFoundError as e:
        print("File Not Found or the given file name is incorrect, It should be a text file.")
    except OSError as e:
        print("Given File name is not defined")

#defining main function
def main():
    try:
        input_file_name = ''
        output_file_name = ''

        flag = False
        while flag == False:
            input_file_name = input("Enter input file name: ")
            flag = validate_filename_input(input_file_name)

        flag = False
        while flag == False:
            output_file_name = input("Enter output file name: ")
            flag = validate_filename_input(output_file_name)

        ans = formate_beautify_text(input_file_name, output_file_name)
        print(ans)
        
    except FileNotFoundError as e:
        print("File Not Found.")
    except OSError as e:
        print("Given File name is not defined.")

if __name__ == "__main__":
    main()