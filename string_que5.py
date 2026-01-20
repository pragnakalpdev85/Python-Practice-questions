# Question 5: Remove Duplicate Characters
# Write a program that takes a string as input and removes all duplicate characters, keeping only the first occurrence of each character (preserve order and case).

# Rules:
# No in-built functions allowed (except input() and print())
# Must use loops and string building
# Handle edge cases (empty string, all unique characters)
# Preserve the original order and case of characters

# Test Cases:

# Test Case 1:
# Input: "programming"
# Output: "progamin"

# Test Case 2:
# Input: "Hello"
# Output: "Helo"

# Test Case 3:
# Input: "aabbcc"
# Output: "abc"

def remove_duplicates(input_str):
    try:
        input_str = str(input_str)
        unique_str = ""
        

        #looping till end of string and adding unique element to the string
        for i in input_str:

            flag = True
            #finding duplicate
            for j in unique_str:
                if i == j:
                    flag = False
                    break
            
            if flag == True:
                unique_str += i

        print(unique_str if unique_str != "" else "String is empty")
                
    except Exception as e:
        print("something went wrong!! ",e)
    
#test case 1:
remove_duplicates("programming")

#test case 2:
remove_duplicates("Hello")

#test case 3:
remove_duplicates("aabbcc")

#test case 4:
input_str = input("Enter a string: ")
remove_duplicates(input_str)
    
