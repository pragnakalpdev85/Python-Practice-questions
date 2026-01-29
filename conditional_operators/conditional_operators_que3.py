# Question 3: Leap Year Checker
# Write a program that takes a year as input and determines whether it is a leap year or not.

# Leap Year Rules:
# Divisible by 4 AND not divisible by 100, OR
# Divisible by 400

# Rules:
# No in-built functions allowed (except input() and print())
# Must use conditional operators
# Handle edge cases (negative years, year 0)

# Test Cases:

# Test Case 1:
# Input: year = 2024
# Output: Leap Year

# Test Case 2:
# Input: year = 1900
# Output: Not a Leap Year

# Test Case 3:
# Input: year = 2000
# Output: Leap Year

def leap_checker(input_year):
    #checking input year is valid or not
    if type(input_year) == int and input_year > 0:
        if (input_year%4 == 0 and not input_year%100 == 0) or input_year%400 == 0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Invalid input, Enter valid year")

#test case 1:
leap_checker(2024)

#test case 2:
leap_checker(1900)

#test case 3:
leap_checker(2000)

#test case 4:
leap_checker(2020)