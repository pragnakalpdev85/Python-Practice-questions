# Question 4: Count Digits
# Write a function count_digit_frequency(number, digit) that counts how many times a specific digit appears in a given number.

# Rules:
# No in-built functions allowed (except input() and print())
# Must create and use a function
# Handle edge cases (negative numbers, digit not in range 0-9)
# Use loops to extract digits

# Test Cases:

# Test Case 1:
# Input: number = 122333, digit = 3
# Output: 3

# Test Case 2:
# Input: number = 100000, digit = 0
# Output: 5

# Test Case 3:
# Input: number = 987654, digit = 5
# Output: 1

def count_digit_frequency(number, digit):
    #validating input data type
    if type(number) == int:

        #validating number is possitive or not
        if number >= 0:

            #validate digit is between 0-9 or not
            if digit >= 0 and digit <= 9:
                count = 0
                while number > 0:
                    r = number%10
                    number //= 10
                    if r == digit:
                        count += 1
                
                print(count)
            else:
                print("Invalid input, Enter digit between 0-9.")
        else:
            print("Invalid input, Enter possitive number.")
    else:
        print("Invalid datatype as input, Enter a possitive number.")

#test case 1:
count_digit_frequency(122333,3)

#test case 2:
count_digit_frequency(10000000,0)

#test case 3:
count_digit_frequency(987654,5)

#test case 4:
try:
    a = int(input("Enter number: "))
    b = int(input("Enter digit: "))
    count_digit_frequency(a,b)
except Exception as e:
    print("Invalid datatype as input, Enter a number. ")