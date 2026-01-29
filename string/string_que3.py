# Question 3: Check String Palindrome
# Write a program that checks whether a given string is a palindrome or not (ignoring spaces and case).

# Rules:
# No in-built functions allowed (except input() and print())
# Must use loops to compare characters
# Handle edge cases (empty string, single character)
# Ignore spaces and case sensitivity

# Test Cases:

# Test Case 1:
# Input: "racecar"
# Output: Palindrome

# Test Case 2:
# Input: "A man a plan a canal Panama"
# Output: Palindrome

# Test Case 3:
# Input: "Hello"
# Output: Not a Palindrome

def check_palindrome(input_str):
    if type(input_str) == str or type(input_str) == int or type(input_str) == float:
        input_str = str(input_str)

        upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower_alpha = "abcdefghijklmnopqrstuvwxyz"
        new_str = ""
        #converting string into lower case and without space or special characters
        for i in input_str:
            #lowercase than adding into new string
            if i >= "a" and i <= "z":
                new_str += i
            
            #character is upper case than convert into lower case
            elif i >= "A" and i <= "Z":
                index = 0
                for j in upper_alpha:
                    if(i == j):
                        break
                    index += 1
                new_str += lower_alpha[index]

            #character is number than add into new string
            elif i >= "0" and i <= "9":
                new_str += i

        #checking match or converted string and it's reverse are equal or not
        check_string = new_str
        n = 0
        for i in new_str:
            n += 1
        n -= 1
        flag = True
        for i in new_str:
            if i != new_str[n]:
                flag = False
                break
            n -= 1

        print(f"Palindrome" if flag == True else "Not a palindrome")

               
    else:
        print("Invalid datatype as input, Enter a String.")

#test case 1:
check_palindrome("racecar")

#test case 2:
check_palindrome("A man a plan a canal Panama")

#test case 3:
check_palindrome("Hello")

#test case 4:
input_str = input("Enter a String: ")
check_palindrome(input_str)
