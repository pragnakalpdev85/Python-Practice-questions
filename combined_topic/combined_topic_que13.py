# Question 13: Duplicate File Content Finder 
# Write a program that takes multiple file paths as input, reads their content, and identifies files with duplicate content. Group duplicate files together and write a report showing which files have identical content.

# Rules:
# You can use file operations: open(), read(), write(), close()
# Must use loops, dictionaries, lists, sets, and functions
# Create functions for content comparison
# Handle edge cases (empty files, single file)
# Write report to output file

# Test Cases:

# Test Case 1:
# file1.txt: "Hello World"
# file2.txt: "Hello World"
# file3.txt: "Different"
# Output:
# Duplicate Group 1:
# file1.txt, file2.txt
# Unique Files:
# file3.txt

# Test Case 2:
# file1.txt: "Test"
# file2.txt: "Test"
# file3.txt: "Test"
# Output:
# Duplicate Group 1:
# file1.txt, file2.txt, file3.txt

# Test Case 3:
# file1.txt: "A"
# file2.txt: "B"
# file3.txt: "C"
# Output:
# No duplicates found
# Unique Files:
# file1.txt, file2.txt, file3.txt
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

def read_file_data(file_name: str) -> str:
    '''
    read file data from input file
    
    Args:
        file_name (str): name of the input file
    Returns:
        str: file data as string
    '''
    content_list = []
    with open(file_name, 'r') as file:
        #reading line and storing all words in content list
        for line in file:
            data_size = 0
            #calculating length of the line
            for _ in line:
                data_size += 1

            word = ''
            index = 0
            for char in line:
                if char == ' ' or char == '\n' or index == data_size-1:
                    if index == data_size-1:
                        word += char

                    if word != '':
                        content_list += [word,]
                        word = ''
                else:
                    word += char
            
                index += 1
                    
        return content_list
    
def content_comparison(list_contents: list) -> dict:
    '''
    compares contents of different files and group them based on same content

    Args:
        list_contents (list): list of contents with filename
    Returns:
        dict: dictionary of grouped file and unique file
    '''
    unique_list = []
    #finding all unique contents
    for content in list_contents:
        flag = False
        for duplicate in unique_list:
            if content[1] == duplicate:
                flag = True
                break

        if flag == False:
            unique_list += [content[1]]

    ans_dict = {}
    index = 0
    #Grouping all file name based on content 
    for data in unique_list:
        content_list = []
        for content in list_contents:
            if content[1] == data:
                content_list += [content[0]]

        ans_dict[index] = content_list
        index += 1

    return ans_dict
        
def find_duplicate_content(files: list, output_file: str) -> str:
    '''
    Groups duplicate files together and write a report
    
    Args:
        files (list): list of file names
        output_file (str): name of the output file
    Returns:
        str: report of duplicate and unique files
    '''
    file_contents = []
    files = set(files)
    #reading files and storing file content in list with file name
    for file_name in files:
        content = read_file_data(file_name)
        if content == []:
            print(f"{file_name} is Empty")
        else:
            file_contents += [tuple((file_name,content))]

    ans_dict = content_comparison(file_contents)
    duplicate = ''
    group_count = 0
    unique_count = 0
    unique = ''
    #preparing report 
    for answers in ans_dict:
        temp = ans_dict[answers]
        size = 0
        for _ in temp:
            size += 1

        if size == 1:
            #adding file names with unique content 
            unique += temp[0] if unique_count == 0 else f", {temp[0]}"
            unique_count += 1
        else:
            #adding file name with duplicate contents
            group_count += 1
            if group_count == 1:
                duplicate += f"Duplicate Group {group_count}:\n"
            else:
                duplicate += f"\nDuplicate Group {group_count}:\n"

            index = 0
            for names in temp:
                duplicate += names if index == 0 else f", {names}"
                index += 1

    output = ''
    output += "No duplicates found" if duplicate == '' else duplicate
    output += "\nNo Uniques found" if unique == '' else f"\nUnique Files:\n{unique}"
    
    with open(output_file,'w') as file:
        file.write(output)
        
    return output

#defining main function
def main():
    try:
        files_count = int(input("Enter number of files: "))
        if files_count <= 0:
            print("Enter atleast 1 file name")
            return
        
        index = 0
        files = []
        while index < files_count:
            flag = False
            input_file_name = ''
            while flag == False:
                input_file_name = input(f"Enter input file name {index+1}: ")
                flag = validate_filename_input(input_file_name)
            
            files += [input_file_name,]
            index += 1

        output_file_name = ''
        flag = False
        while flag == False:
            output_file_name = input("Enter output file name: ")
            flag = validate_filename_input(output_file_name)

        ans = find_duplicate_content(files, output_file = output_file_name)
        print(ans)

    except FileNotFoundError as e:
        print("File Not Found")
    except OSError as e:
        print("Given File name is not defined")
    except ValueError as e:
        print("Invalid input in number of files.")

if __name__ == "__main__":
    main()


