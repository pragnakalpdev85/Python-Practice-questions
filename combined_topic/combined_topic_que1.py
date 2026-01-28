# Question 1: Student Grade Management System
# Write a program that reads student data from a file where each line contains: name,marks1,marks2,marks3. Calculate the average for each student, assign grades (A/B/C/D/F), and write the results to a new file.

# Rules:
# You can use file operations: open(), read(), write(), close()
# Must use loops, conditionals, lists, and string operations
# Create a function to calculate average
# Create a function to determine grade based on average
# Handle edge cases (empty file, invalid data)
# Grade criteria: A(90+), B(80-89), C(70-79), D(60-69), F(<60)

# Test Cases:

# Test Case 1:

# Input file:
# John,85,90,88
# Alice,92,95,98

# Output file:
# John,87.67,B
# Alice,95.0,A

# Test Case 2:

# Input file:
# Bob,50,55,45

# Output file:
# Bob,50.0,F

# Test Case 3:

# Input file:
# Charlie,75,75,75

# Output file:
# Charlie,75.0,C


def cal_avg(marks1: float, marks2: float, marks3: float) -> float:
    '''
    calculates average of 3 marks
    
    Args:
        marks1 (float): fist marks of student
        marks2 (float): second marks of student 
        marks3 (float): third marks of student
    Returns:
        float: average marks of the student
    '''

    if marks1 > 100 or marks1 < 0 or marks2 > 100 or marks2 < 0 or marks3 > 100 or marks3 < 0:
        raise ValueError("Marks should be in between 0 - 100")
    
    avg_marks = (marks1 + marks2 + marks3)/3

    return avg_marks

    
def cal_grade(avg_marks: float) -> str:
    '''
    calculate grade based on average marks
    
    Args:
        avg_marks (float): average marks of student
    Returns:
        str: grade
    '''    
    grade = ''
    #calculating grade
    if avg_marks >= 90 and avg_marks <= 100:
        grade = 'A'
    elif avg_marks < 90 and avg_marks >= 80:
        grade = 'B'
    elif avg_marks < 80 and avg_marks >= 70:
        grade = 'C'
    elif avg_marks < 70 and avg_marks >= 60:
        grade = 'D'
    elif avg_marks < 60 and avg_marks >= 0:
        grade = 'F'

    return grade

def grade_management_system(input_file_name: str, output_file_name: str) -> str:
    '''
    reads data from a input file and writes name, average marks and grade into output file.
    
    Args:
        input_file_name (str): name of the input file
        output_file_name (str): name of the output file
    Returns: 
        str: data written in output file
    '''
    try:
        #reading input file
        file =  open(input_file_name, 'r')
        data = file.read()
        file.close()

        #calculating size of the data
        data_size = 0
        for i in data:
            data_size += 1

        word = ''
        character_count = 0

        output_data = ''
        list_words = []

        #looping through input data
        for index in data:
            #data is seprated by coma, newline character and the last word of the data
            if index == ',' or index == '\n' or character_count == data_size-1:
                if character_count == data_size-1:
                    word += index
                if word != '':
                    list_words += [word,]
                    word = ''
            else:
                word += index
            character_count += 1

        size_list = 0
        #calculating list elements
        for words in list_words:
            size_list += 1

        name = ''
        marks1 = 0
        marks2 = 0
        marks3 = 0
        word_count = 0
        words = 0
        #first word in text file is name second, third and fourth are marks of the student
        for word in list_words:
            if word_count == 0:
                name = word
            elif word_count == 1:
                marks1 = float(word)
            elif word_count == 2:
                marks2 = float(word)
            elif word_count == 3:
                marks3 = float(word)
                
                #calculating average and grade
                avg = cal_avg(marks1,marks2,marks3)
                grade = cal_grade(avg)

                #writing student name, average and grade in output data
                if words == size_list-1:
                    output_data += f"{name},{avg:0.2f},{grade}"
                else:
                    output_data += f"{name},{avg:0.2f},{grade}\n"
            

            word_count = (word_count+1)%4
            words += 1

        output_file = open(output_file_name,'w')
        output_file.write(output_data)
        output_file.close()

        return f"New file contains {output_data}" if output_data != '' else "File is empty"
    
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

        ans = grade_management_system(input_file_name, output_file_name)
        print(ans)
    except TypeError as e:
        print("Invalid input, ",e)
    except ValueError as e:
        print("Invalid input, ",e)

    

if __name__ == "__main__":
    main()
