# Question 2: Copy File Content
# Write a program that reads content from one file and copies it to another file line by line.

# Rules:
# You can use open(), read(), write(), close() functions
# Must use loops to read and write lines
# Handle edge cases (source file not found, destination file already exists)
# Proper error handling and file closing required

# Test Cases:

# Test Case 1:
# Input: source.txt contains "Line 1
# Line 2
# Line 3"
# Output: destination.txt contains exact same content

# Test Case 2:
# Input: source.txt contains "Single line"
# Output: destination.txt contains "Single line"

# Test Case 3:
# Input: source.txt is empty
# Output: destination.txt is empty

def copy_file_content(input_file_name, output_file_name):
    try:
        #opening input file reading data and closing file
        file1 = open(input_file_name,"r")
        file_data = file1.read()
        file1.close()

        if file_data == '':
            return f"{output_file_name} is Empty"

        #opening file 1
        file2 = open(output_file_name,"w")

        #calculating string length
        data_size = 0
        for i in file_data:
            data_size += 1

        line = ''
        i = 0
        line_count = 0
        #writing input file data into the output file line by line
        while i < data_size:
            if file_data[i] == '\n' or i == data_size-1:
                line_count += 1
                line += file_data[i]
                file2.write(line)
                line = ''
            else:
                line += file_data[i]
            i += 1
        file2.close()

        return f"{output_file_name} contains 'Single line'" if line_count == 1 else f"{output_file_name} contains exact same content"

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
    ans = copy_file_content(input_file_name, output_file_name)
    print(ans)
except TypeError as e:
    print("Invalid input, ",e)
except ValueError as e:
    print("Invalid input, ",e)