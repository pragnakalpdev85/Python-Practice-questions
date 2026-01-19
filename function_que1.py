# Question 1: Calculate Power
# Write a function calculate_power(base, exponent) that calculates base raised to the power of exponent without using any in-built functions.

# Rules:
# No in-built functions allowed (except input() and print())
# Must create and use a function
# Handle edge cases (exponent = 0, negative exponent)
# Use loops inside the function

# Test Cases:

# Test Case 1:
# Input: base = 2, exponent = 5
# Output: 32

# Test Case 2:
# Input: base = 5, exponent = 0
# Output: 1

# Test Case 3:
# Input: base = 3, exponent = 4
# Output: 81

def cal_power(base, exponent):
    #validating input
    if (type(base) == int or type(base) == float) and type(exponent) == int and exponent >= 0:

        ans = 1
        #calculating power
        for i in range(exponent):
            ans *= base
        
        print(ans)
    elif exponent < 0:
        print("Invalid input, Enter possitive value of exponent")
    else:
        print("Invalid datatype as input, Enter a number.")

#test case 1:
cal_power(2,5)

#test case 2:
cal_power(5,0)

#test case 3:
cal_power(3,4)

#test case 4:
cal_power(-4,3)

#test case 5:
cal_power(-4,-3)

#test case 6:
try:
    a = float(input("Enter base: "))
    b = int(input("Enter exponent: "))
    cal_power(a, b)
except Exception as e:
    print("Invalid datatype as input, Enter a number. ")