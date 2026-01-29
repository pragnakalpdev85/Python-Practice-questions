# Question 5: Armstrong Number Checker
# Write a function is_armstrong(number) that checks whether a given positive integer is an Armstrong number or not. An Armstrong number is a number that equals the sum of its digits each raised to the power of the number of digits.

# Example: 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153

# Rules:
# No in-built functions allowed (except input() and print())
# Must create and use a function
# You can create helper functions if needed
# Handle edge cases (single digit numbers, negative numbers)
# Use loops for all operations

# Test Cases:

# Test Case 1:
# Input: number = 153
# Output: True

# Test Case 2:
# Input: number = 9474
# Output: True
# Explanation: 9⁴ + 4⁴ + 7⁴ + 4⁴ = 6561 + 256 + 2401 + 256 = 9474

# Test Case 3:
# Input: number = 123
# Output: False

def is_armstrong(number):
    #validating input datatype
    if type(number) == int:

        #validating integer is positive or not
        if number >= 0:

            #all single digit numbers are armstrong
            if number >= 0 and number <= 9:
                print(True)
            else:
                n = number
                ansnum = 0 
                digitcount = 0

                #counting digit of number
                while number > 0:
                    r = number%10
                    number //= 10
                    digitcount += 1
                
                #calculating the sum of digit^digitcount
                number = n
                for i in range(digitcount):
                    r = number%10
                    number //= 10
                    ansnum += r**digitcount
                
                if(ansnum == n):
                    print(True)
                else:
                    print(False)
        else:
            print("Invalid input, Enter possitive Integer.")
    else:
        print("Invalid datatype as input, Enter a possitive number.")

#test case 1:
is_armstrong(153)

#test case 2:
is_armstrong(9474)

#test case 3:
is_armstrong(123)

#test case 4:
is_armstrong(0)

#test case 5:
is_armstrong(-1)

#test case 6:
try:
    a = int(input("Enter number: "))
    is_armstrong(a)
except Exception as e:
    print("Invalid datatype as input, Enter a possitive number. ")

