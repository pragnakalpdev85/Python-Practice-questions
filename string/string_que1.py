# Question 1: Count Vowels and Consonants
# Write a program that takes a string as input and counts the number of vowels and consonants in it.

# Rules:
# No in-built functions allowed (except input() and print())
# Must use loops to iterate through the string
# Handle edge cases (empty string, strings with numbers/special characters)
# Consider both uppercase and lowercase vowels

# Test Cases:

# Test Case 1:
# Input: "Hello World"
# Output: Vowels: 3, Consonants: 7

# Test Case 2:
# Input: "Python123"
# Output: Vowels: 1, Consonants: 5

# Test Case 3:
# Input: "aeiouAEIOU"
# Output: Vowels: 10, Consonants: 0

def count_vowels_consonants(input_str):
    #validating input datatype
    if type(input_str) == str or type(input_str) == int or type(input_str) == float:
        input_str = str(input_str)
        
        vowel_count = 0
        consonant_count = 0

        #counting vowels and consonants
        for i in input_str:
            #for vowels
            if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
                vowel_count += 1
            #for consonants
            elif (i >= "a" and i <= "z") or (i >= "A" and i <= "Z"):
                consonant_count += 1
                        
        print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")
    else:
        print("Invalid datatype as input, Enter a String.")

#test case 1:
count_vowels_consonants("Hello World")

#test case 2:
count_vowels_consonants("Python123")

#test case 3:
count_vowels_consonants("aeiouAEIOU")

#test case 4:
count_vowels_consonants(1234)

#test case 5:
count_vowels_consonants("1123")

#test case 6:
input_str = input("Enter a String: ")
count_vowels_consonants(input_str)