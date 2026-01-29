# Question 3: Prime Number Checker
# Write a program that checks whether a given positive integer is prime or not.

# Rules:
# No in-built functions allowed (except input() and print())
# Must use loops for checking divisibility
# Handle edge cases (numbers ≤ 1)

# Test Cases:
# Test Case 1:
# Input: 17
# Output: Prime

# Test Case 2:
# Input: 24
# Output: Not Prime

# Test Case 3:
# Input: 1
# Output: Not Prime

def prime_number(input_num):
    flag = True

    #checking input is integer or not
    if type(input_num) == int:
        if(input_num == 1 or input_num <= 0): flag = False

        #looping from 2 to input_num/2 and checking the number is completely divisible or not
        for i in range(2,(input_num//2)+1):
            if(input_num%i == 0):
                flag = False
                break

        if(flag == True):
            print("Prime")
        else:
            print("Not Prime")
    else:
        print("Enter valid number")

#test case 1:
prime_number(17)

#test case 2:
prime_number(1)

#test case 3:
prime_number(24)

#test case 4:
prime_number(-2)


