# Question 6: Text File Cipher System 
# Write a program that encrypts and decrypts text files using Caesar cipher. Implement functions to: encrypt file, decrypt file, and brute force decrypt (try all possible shifts). Handle uppercase, lowercase, and preserve non-alphabetic characters.

# Rules:
# You can use file operations: open(), read(), write(), close()
# Must use loops, conditionals, strings, and functions
# Create separate functions for encryption and decryption
# Handle edge cases (empty file, special characters)
# Shift value between 1-25

# Test Cases:

# Test Case 1:
# Input: "Hello World", shift = 3
# Output (Encrypted): "Khoor Zruog"
# Output (Decrypted): "Hello World"

# Test Case 2:
# Input: "Python 123!", shift = 5
# Output (Encrypted): "Udymts 123!"
# Output (Decrypted): "Python 123!"

# Test Case 3:
# Input: "ABC xyz", shift = 1
# Output (Encrypted): "BCD yza"
# Output (Decrypted): "ABC xyz"

def encrypt(input_file_name: str, output_file_name: str, shift: int) -> str:
    '''
    encrypt the data from the file
    
    Args:
        file_name (str): name of the input file
        shift (int):character shift for encryption
    Returns:
        str: encrypted string 
    '''
    try:
        flag = False
        check_word1 = ''
        for chars in input_file_name:
            if flag == True:
                check_word1 += chars
            if chars == '.':
                flag = True
        
        flag = False
        check_word2 = ''
        for chars in output_file_name:
            if flag == True:
                check_word2 += chars
            if chars == '.':
                flag = True
        
        if check_word1 != 'txt' and check_word2 != 'txt':
            raise FileNotFoundError("File Should be .txt format.")

        #opening file and reading data
        with open(input_file_name,'r') as file:
            data = file.read()

        if data == '':
            return "There is no content in file"

        upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower_alpha = "abcdefghijklmnopqrstuvwxyz"

        #shift is >26 than reduce it between 1-26
        if shift > 26:
            shift %= 26
        
        output = ''
        
        #shifting each character with given shifts
        for char in data:
            if char >= 'A' and char <= 'Z':
                index = 0
                for alphabet in upper_alpha:
                    if char == alphabet:
                        output += upper_alpha[(index+shift)%26]
                    index += 1
            elif char >= 'a' and char <= 'z':
                index = 0
                for alphabet in lower_alpha:
                    if char == alphabet:
                        output += lower_alpha[(index+shift)%26]
                    index += 1
            else:
                output += char
        
        with open(output_file_name,'w') as file:
            file.write(output)

        return f"(Encrypted): {output}"

    except TypeError as e:
        print("Invalid input, ",e)
    except ValueError as e:
        print("Invalid input, ",e)
    except FileNotFoundError as e:
        print("File Not Found: ",e)
    except OSError as e:
        print("Given File name is not defined: ",e)

def decrypt(input_file_name: str, output_file_name: str, shift: int) -> str:
    '''
    decrypt the data from the file
    
    Args:
        file_name (str): name of the input file
        shift (int):character shift for decryption
    Returns:
        str: decrypted string 
    '''
    try:
        flag = False
        check_word1 = ''
        for chars in input_file_name:
            if flag == True:
                check_word1 += chars
            if chars == '.':
                flag = True
        
        flag = False
        check_word2 = ''
        for chars in output_file_name:
            if flag == True:
                check_word2 += chars
            if chars == '.':
                flag = True
        
        if check_word1 != 'txt' and check_word2 != 'txt':
            raise FileNotFoundError("File Should be .txt format.")

        #opening file and reading data
        with open(input_file_name,'r') as file:
            data = file.read()

        if data == '':
            return "There is no content in file"

        upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower_alpha = "abcdefghijklmnopqrstuvwxyz"

        #shift is >26 than reduce it between 1-26
        if shift > 26:
            shift %= 26
        
        output = ''
        
        #shifting each character with given shifts backwords
        for char in data:
            if char >= 'A' and char <= 'Z':
                index = 0
                for alphabet in upper_alpha:
                    if char == alphabet:
                        output += upper_alpha[(index-shift)%26]
                    index += 1
            elif char >= 'a' and char <= 'z':
                index = 0
                for alphabet in lower_alpha:
                    if char == alphabet:
                        output += lower_alpha[(index-shift)%26]
                    index += 1
            else:
                output += char
        
        with open(output_file_name,'w') as file:
            file.write(output)
        
        return output
    except TypeError as e:
        print("Invalid input, ",e)
    except ValueError as e:
        print("Invalid input, ",e)
    except FileNotFoundError as e:
        print("File Not Found: ",e)
    except OSError as e:
        print("Given File name is not defined: ",e)

def brute_force_decrypt(input_file_name: str, output_file_name: str, original_data: str) -> str:
    '''
    decrypt the data from the file using brute force approach
    
    Args:
        file_name (str): name of the input file
        original_data (str): original data from the input file
    Returns:
        str: decrypted string 
    '''
    shifts = 1
    temp = ''
    #trying all possible values of shift
    while shifts <= 26:
        temp = decrypt(input_file_name, output_file_name,shifts)
        if original_data == temp:
            break
        shifts += 1
     
    return f"(Decrypted): {temp}"
        
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

        shift = int(input("Enter Shift: "))

        ans = encrypt(input_file_name, output_file_name, shift)
        print(ans)
        ans = decrypt(output_file_name, input_file_name, shift)
        decrypted_ans = brute_force_decrypt(output_file_name, input_file_name, ans)
        print(decrypted_ans)

    except FileNotFoundError as e:
        print("File Not Found: ",e)
    except OSError as e:
        print("Given File name is not defined: ",e)
    except TypeError as e:
        print("Invalid input, ",e)
    except ValueError as e:
        print("Invalid input, ",e)

if __name__ == "__main__":
    main()