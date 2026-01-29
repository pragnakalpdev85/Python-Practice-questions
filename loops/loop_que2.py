# Question 2: Reverse a Number
# Write a program that takes an integer as input and prints its reverse using loops.

# Rules:
# No in-built functions allowed (except input() and print())
# Must use loops only
# Handle negative numbers

# Test Cases:

# Test Case 1:
# Input: 12345
# Output: 54321

# Test Case 2:
# Input: -9876
# Output: -6789

# Test Case 3:
# Input: 100
# Output: 1

def reverse_number(input_num):
    ans = 0
    possitive = True

    #checking the entered input is number or not
    if type(input_num) == int:

        #checking number possitive or nagetive 
        if input_num < 0:
            possitive = False

            #converting negative to possitive for further operation
            temp = str(input_num)
            input_num = int(temp[1:])

        while input_num > 0:
            tempnum = input_num%10
            input_num //= 10
            ans = (ans*10) + tempnum

        if possitive == True:
            print(ans)
        else:
            #converting input number back to negative after operation
            temp = f"-{ans}"
            ans = int(temp)
            print(ans)
    else:
        print("Enter an integer.")
        

#test case 1:
reverse_number(12345)

#test case 2:
reverse_number(-9876)

#test case 3:
reverse_number(100)

#test case 4:
reverse_number(0)


