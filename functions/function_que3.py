# Question 3: Check Palindrome
# Write a function is_palindrome(number) that checks whether a given integer is a palindrome or not. Return True if palindrome, False otherwise.

# Rules:
# No in-built functions allowed (except input() and print())
# Must create and use a function
# Handle edge cases (negative numbers, single digit)
# Use loops to reverse the number

# Test Cases:

# Test Case 1:
# Input: number = 12321
# Output: True

# Test Case 2:
# Input: number = 12345
# Output: False

# Test Case 3:
# Input: number = -121
# Output: False

def is_palindrome(num):
    #validating input data type
    if type(num) == int:
        number = num
        flag = False
        ans = 0

        #checking number is negative or not
        if number >= 0:
            #looping till number becomes 0
            while number > 0:
                r = number%10
                number //= 10
                ans = (ans*10) + r
            
            if(ans == num):
                flag = True
            
            print(flag)
        else:
            print(flag)
    else:
        print("Invalid datatype as input, Enter a possitive integer.")

#test case 1:
is_palindrome(12321)

#test case 2:
is_palindrome(12345)

#test case 3:
is_palindrome(-121)

try:
    a = int(input("Enter number: "))
    is_palindrome(a)
except Exception as e:
    print("Invalid datatype as input, Enter a number. ")