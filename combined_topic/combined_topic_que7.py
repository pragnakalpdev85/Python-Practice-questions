# Question 7: Student Performance Analyzer 
# Write a program that reads student exam data from multiple files (one file per subject). Each file contains: student_name,marks. Create a comprehensive report showing: student-wise total, average, rank, subject-wise toppers, and class statistics.

# Rules:

# You can use file operations: open(), read(), write(), close()
# Must use loops, dictionaries, lists, tuples, sets, and functions
# Create functions for calculations and rankings
# Handle edge cases (missing students in some subjects)
# Write detailed report to output file

# Test Cases:

# Test Case 1:
# Math.txt: John,85 | Alice,95
# Science.txt: John,90 | Alice,92
# Output:
# Student Report:
# John - Total: 175, Average: 87.5, Rank: 2
# Alice - Total: 187, Average: 93.5, Rank: 1
# Subject Toppers:
# Math: Alice(95)
# Science: John(90)

# Test Case 2:
# English.txt: Bob,70 | Charlie,75
# History.txt: Bob,80 | Charlie,70
# Output:
# Student Report:
# Bob - Total: 150, Average: 75.0, Rank: 1
# Charlie - Total: 145, Average: 72.5, Rank: 2
# Subject Toppers:
# English: Charlie(75)
# History: Bob(80)

# Test Case 3:
# Physics.txt: Alice,100
# Chemistry.txt: Alice,98 | Bob,95
# Output:
# Student Report:
# Alice - Total: 198, Average: 99.0, Rank: 1
# Bob - Total: 95, Average: 95.0, Rank: 2
# Subject Toppers:
# Physics: Alice(100)
# Chemistry: Alice(98)

def to_lower_case(data: str) -> str:
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

        if character == " ":
            index += 1
            continue

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

def sort_lists(marks_list: list, sort_by_name: bool) -> list:
    """
    sort list by name or by marks 

    Args:
        marks_list (list): list of student with name and marks
        sort_by_name (bool): True then it will sort by name otherwise by marks
    Returns:
        List: sorted list
    """
    size_list = 0
    for elements in marks_list:
        size_list += 1

    index1 = 0

    #sorting should be done based on name or marks
    if sort_by_name == True:
        key = 0
    else:
        key = 1

    #sorting elements in list
    while index1 < size_list:
        index2 = 0
        while index2 < size_list-index1-1:
            if marks_list[index2][key] < marks_list[index2+1][key]:
                temp = marks_list[index2+1]
                marks_list[index2+1] = marks_list[index2]
                marks_list[index2] = temp
            index2 += 1
        index1 += 1

    return marks_list

def read_data(file_name: str) -> list:
    '''
    read data and creat list of data
    
    Args:
        file_name (str): name of the input file
    Returns:
        list: list of tuples with name and marks
    '''
    with open(file_name, 'r') as file:
        data = file.read()
    if data == '':
        return []
    
    data = to_lower_case(data)
    data_size = 0

    for char in data:
        data_size += 1

    list_words = []
    words_count = 0
    index = 0
    word = ''

    for chars in data:
        #add all words in the list
        if chars == ',' or chars == '|' or chars == '\n' or index == data_size-1:
            if index == data_size-1:
                word += chars
        
            if word != '':
                list_words += [word,]
                words_count += 1
                word = ''
        else:
            word += chars
        index += 1

    output_list = []
    index = 0

    while index < words_count:
        if index+1 != words_count:
            marks = float(list_words[index+1])
            if marks >= 0 and marks <= 100:
                output_list += [tuple((list_words[index], float(list_words[index+1]))),]
            else:
                print(f"Marks of {list_words[index]} is invalid, Marks should be in between 0 to 100.")
        index += 2

    return output_list

def calculate_total_avg(total_marks_list: list, marks_lists: list) -> list:
    '''
    calculate total and avg from marks lists

    Args:
        total_marks_list: list of total marks and avg marks
        marks_list: list of marks of any subjects
    Returns:
        list: total and avg marks with name
    '''
    ans_list = []
    if total_marks_list == []:
        for index in marks_lists:
            ans_list += [tuple((index[0], index[1], index[1])),]
    
        return ans_list
    else:
        #calculating size of the marks list
        size_marks_list = 0
        for element in total_marks_list:
            size_marks_list += 1

        #adding marks to the total marks list with the total and average
        for marks in marks_lists:
            index = 0
            flag = False
            for total in total_marks_list:
                if marks[0] == total[0]:
                    flag = True
                    total_marks = marks[1] + total[1]
                    total_marks_list[index] = tuple((marks[0],total_marks,total_marks/2))
                    break
                index += 1
            if flag == False:
                total_marks_list += [tuple((marks[0],marks[1],marks[1])),]

        return total_marks_list
    
def student_performance_analyzer(file_names: list,output_file: str) -> str:
    '''
    analyze and writes student performance report in output file
    
    Args:
        file_name: Description
        output_file: Description
    Returns:
        str: student performance report
    '''
    try:
        ans_dict = {"total": []}
        subjects = []
        #reading each arbitrary argument and adding file data
        for names in file_names:
            word = ''
            check = ''
            flag = False
            for chars in names:
                if flag == True:
                    check += chars
                else:
                    if chars != ".":
                        word += chars

                if chars == '.':
                    flag = True
            
            #storing all subject names
            flag = False
            for subject in subjects:
                if subject == word:
                    flag = True
                    break
            if flag == False:
                subjects += [word,]

            if check != "txt":
                raise FileNotFoundError("File Should be .txt format.")

            #storing subject wise marks of student
            ans_dict[word] = sort_lists(read_data(names),True)
            #updating total and avg of the students
            ans_dict["total"] = sort_lists(calculate_total_avg(ans_dict["total"],ans_dict[word]),True)
        
        output = 'Student report: \n'
        total_list = sort_lists(ans_dict["total"],False)
        rank = 1
        #listing all student rank wise
        for total in total_list:
            output += f"{total[0]} - Total: {total[1]}, Average: {total[2]}, Rank: {rank}\n"
            rank += 1
        
        output += "Subject Toppers:\n"
        #listing all subject's topper
        subject_cout = 1
        for subject in subjects:

            if subject_cout == 1:
                output += f"{subject}: "
            else:
                output += f"\n{subject}: "

            topper_list = sort_lists(ans_dict[subject],False)
            mark = topper_list[0][1]
            
            number = 1
            for topers in topper_list:
                if topers[1] == mark:
                    if number == 1:
                        output += f"{topers[0]}({topers[1]})"
                    else:
                        output += f", {topers[0]}({topers[1]})"
                number += 1
            subject_cout += 1

        with open(output_file, 'w') as file:
            file.write(output)

        return output
    except FileNotFoundError as e:
        print("File Not Found: ",e)
    except OSError as e:
        print("Given File name is not defined: ",e)
    except TypeError as e:
        print("Invalid input data. Please enter valid data types in input file.")
    except ValueError as e:
        print("Invalid content structure in input file, Please enter valid data in input file.")

#defining main function
def main():
    try:
        files_count = int(input("Enter number of files: "))
        index = 0
        files = []
        while index < files_count:
            flag = False
            input_file_name = ''
            while flag == False:
                input_file_name = input(f"Enter input file {index+1} name: ")
                try:
                    with open(input_file_name,'r') as f:
                        flag = True
                except FileNotFoundError:
                    print("File not found Enter name again")
            files += [input_file_name,]
            index += 1

        flag = False
        output_file_name = ''
        while flag == False:
            output_file_name = input(f"Enter input output name: ")
            try:
                with open(input_file_name,'r') as f:
                    flag = True
            except FileNotFoundError:
                print("File not found Enter name again")

        ans = student_performance_analyzer(file_names = files, output_file = output_file_name)
        print(ans)

    except FileNotFoundError as e:
        print("File Not Found: ",e)
    except OSError as e:
        print("Given File name is not defined: ",e)
    except TypeError as e:
        print("Invalid input data in file, ",e)
    except ValueError as e:
        print("Invalid input data type in file, ",e)

if __name__ == "__main__":
    main()



