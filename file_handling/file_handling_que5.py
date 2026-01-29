# Question 5: Merge Multiple Files
# Write a program that reads content from multiple files and merges them into a single output file, with each file's content separated by a header showing the source filename.

# Rules:

# You can use open(), read(), write(), close() functions
# Must use loops to read from multiple files
# Handle edge cases (one or more files not found, empty files)
# Add headers like "--- Content from file1.txt ---"
# Proper error handling and file closing required

# Test Cases:

# Test Case 1:
# Input: file1.txt = "Content 1", file2.txt = "Content 2"
# Output: merged.txt =
# --- Content from file1.txt ---
# Content 1
# --- Content from file2.txt ---
# Content 2

# Test Case 2:
# Input: file1.txt = "Hello", file2.txt = "", file3.txt = "World"
# Output: merged.txt =
# --- Content from file1.txt ---
# Hello
# --- Content from file2.txt ---
# --- Content from file3.txt ---
# World

# Test Case 3:
# Input: Only file1.txt = "Single file"
# Output: merged.txt =
# --- Content from file1.txt ---
# Single file

def merge_files(*file_names,result_file):
    try:
        result_file = open(result_file,"w")
        ans_str = ''

        for i in file_names:

            file = open(i,"r")
            
            file_data = file.read()
            # writing data
            result_file.write(f"-----content from {i}-----\n")
            result_file.write(file_data)
            result_file.write("\n")

            ans_str += f"-----content from {i}-----\n{file_data}\n"

            file.close()
        
        result_file.close()

        return ans_str
    
    except FileNotFoundError as e:
        print("File Not Found", e)
    except OSError as e:
        print("Given File name is not defined, ",e)
    except TypeError as e:
        print("Invalid input, ",e)