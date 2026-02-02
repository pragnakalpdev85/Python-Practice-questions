# Question 14: Quiz Score Processor 
# Write a program that reads quiz data from a file where each line contains: student_name,answer1,answer2,...,answer10 and a separate file with correct answers. Calculate scores, percentages, pass/fail (pass >= 60%), and generate a detailed report with class statistics.

# Rules:
# You can use file operations: open(), read(), write(), close()
# Must use loops, lists, dictionaries, tuples, and functions
# Create functions for scoring and statistics
# Handle edge cases (missing answers, wrong format)
# Write comprehensive report to output file

# Test Cases:

# Test Case 1:
# Answers: A,B,C,D,A,B,C,D,A,B
# John: A,B,C,D,A,B,C,D,A,B
# Alice: A,B,C,D,A,X,X,X,X,X
# Output:
# John: 10/10 (100%) - Pass
# Alice: 5/10 (50%) - Fail
# Class Average: 75%
# Pass Rate: 50%

# Test Case 2:
# Answers: A,A,A,A,A,A,A,A,A,A
# Bob: A,A,A,A,A,A,B,B,B,B
# Output:
# Bob: 6/10 (60%) - Pass
# Class Average: 60%
# Pass Rate: 100%

# Test Case 3:
# Answers: B,C,D,A,B,C,D,A,B,C
# Charlie: B,C,D,A,B,C,D,A,B,C
# Output:
# Charlie: 10/10 (100%) - Pass
# Class Average: 100%
# Pass Rate: 100%

import os

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

def validate_filename_input(file_name: str) -> bool:
    '''
    validates file name input
    
    Args:
        name (str): name of the file
    returns:
        bool: file formate is correct or not
    '''
    if not file_name.endswith('.txt'):
        print("File formate is incorrect, Enter file name again")
        return False
    
    #file exist of not
    if not os.path.exists(file_name):
        print("File does not exist, Enter file name again")
        return False
    
    return True

def validate_options(list_words: list) -> bool:
    '''
    validate answers of the students

    Args:
        list_words (list): list of all words
    Returns:
        bool: answers of student are valid or not
    '''
    options = 'ABCDXabcdx'
    index = 1
    false_data = False
    while index < 11:
        if list_words[index] not in options:
            false_data = True
            break
        index += 1

    return false_data

def read_line(line: str) -> list:
    '''
    reads each word of line

    Args:
        line (str): line of text
    Returns:
        list: returns list of words
    '''
    data_size = 0
    #calculating length of the line
    for char in line:
        data_size += 1
    
    delimeters = [',',':',"\n"," "]

    index = 0
    word = ''
    list_words = []
    count_words = 0
    for chars in line:
        if chars not in delimeters:
            word += chars
        
        if (chars in delimeters or index == data_size-1) and word != '':
            list_words += [word,]
            count_words += 1
            word = ''

        index += 1

    #check the line has 4 word if not than data is incomplete
    if count_words != 11 and count_words != 0:
        print(f"Answer data of student {list_words[0]} is incorrect")
        list_words = []
    
    # for words in list_words:  
    if count_words == 0:
        list_words = []
    
    return list_words

def data_to_dictionary(file_data: str) -> dict:
    '''
    read file data from input file
    
    Args:
        file_data (str): data of the input file
    Returns:
        dict: dictionary of ans data
    '''
    
    ans_dict = {}
    line_count = 1

    for line in file_data:
    
        list_words = read_line(line)
        if list_words == []:
            continue

        if validate_options(list_words):
            print(f"Answer data of student {list_words[0]} is incorrect")
        else:
            ans_dict[line_count] = list_words
            line_count += 1

    return ans_dict
    
def prepare_report(answers: list, data_dictionary: dict) -> str:
    '''
    prepares report from dictionary of student score

    Args:
        data_dictionary (dict): dictionary of student score
        answers (list): list of answers
    Returns:
        str: report of students scores and class statistics
    '''
    output = ''
    class_avg = 0
    pass_rate = 0
    students = 0
    for answer in data_dictionary:
        marks = 0
        list_answers = data_dictionary[answer]
        index = 1
        while index < 11:
            char1 = list_answers[index]
            char2 = answers[index]
            char1 = character_to_lowercase(char1) if char1 >= 'A' and char1 <= 'Z' else char1
            char2 = character_to_lowercase(char2) if char2 >= 'A' and char2 <= 'Z' else char2
            if char1 == char2:
                marks += 1
            index += 1
        
        output += f"{list_answers[0]}: {marks}/10 ({marks * 10}%) - {'Pass' if marks >= 6 else 'Fail'}\n" 

        class_avg += marks
        pass_rate += 1 if marks >= 6 else 0
        students += 1

    output += f"Class Average: {(class_avg*10)/students :0.2f}%\n"
    output += f"Pass Rate: {(pass_rate/students)*100 :0.2f}%"

    return output

def generate_report(answer_file_name: str, input_file_name: str, output_file_name: str) -> str:
    '''
    Generates a detailed report with class statistics.
    
    Args:
        answer_file_name (str): name of the file which contains answers
        input_file_name (str): name of the input file name
        output_file_name (str): name of the output file name
    Returns:
        str: detailed report with class statistics
    '''
    try:
        with open(answer_file_name,'r') as file:
            answers = file.readlines()
        if answers == []:
            return "There is no content in answers file."
    
        with open(input_file_name,'r') as file:
            student_answers = file.readlines()
        if student_answers == []:
            return "There is no content in student data file."

        answers = data_to_dictionary(answers)
        student_answers = data_to_dictionary(student_answers)

        if student_answers == {}:
            return "There is no content in file."

        output = prepare_report(answers[1], student_answers)
        with open(output_file_name,'w') as file:
            file.write(output)

        return output
    
    except TypeError as e:
        print("Invalid input data. Please enter valid data types in input file.")
    except ValueError as e:
        print("Invalid content structure in input file, Please enter valid data in input file.")

def main():
    try:
        answer_file_name = ''
        input_file_name = ''
        output_file_name = ''

        flag = False
        while flag == False:
            answer_file_name = input("Enter answer file name: ")
            flag = validate_filename_input(answer_file_name)

        flag = False
        while flag == False:
            input_file_name = input("Enter input file name: ")
            flag = validate_filename_input(input_file_name)

        flag = False
        while flag == False:
            output_file_name = input("Enter output file name: ")
            flag = validate_filename_input(output_file_name)

        ans = generate_report(answer_file_name, input_file_name, output_file_name)
        print(ans)
        
    except FileNotFoundError as e:
        print("File Not Found.")
    except OSError as e:
        print("Given File name is not defined.")

if __name__ == "__main__":
    main()