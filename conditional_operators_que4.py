# Question 4: Triangle Validity Checker
# Write a program that takes three sides of a triangle as input and checks whether they can form a valid triangle. Also, classify the triangle as Equilateral, Isosceles, or Scalene if valid.

# Triangle Rules:
# Sum of any two sides must be greater than the third side
# Equilateral: All three sides equal
# Isosceles: Two sides equal
# Scalene: All sides different

# Rules:
# No in-built functions allowed (except input() and print())
# Must use conditional operators
# Handle edge cases (negative sides, zero sides)

# Test Cases:

# Test Case 1:
# Input: a = 5, b = 5, c = 5
# Output: Valid Triangle - Equilateral

# Test Case 2:
# Input: a = 5, b = 5, c = 8
# Output: Valid Triangle - Isosceles

# Test Case 3:
# Input: a = 1, b = 2, c = 10
# Output: Not a Valid Triangle

def validate_triangle(a, b, c):
    #checking if input is valid or not
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float) and (type(c) == int or type(c) == float) and a > 0 and b > 0 and c > 0:
        
        #checking triangle is valid or not
        if a+b > c and b+c > a and a+c > b:
            if(a == b == c):
                print("Valid Triangle - Equilateral ")
            elif(a == b or b == c or c == a):
                print("Valid Triangle - Isosceles")
            else:
                print("Valid Triagle - Scalene")
        else:
            print("Not a Valid Triangle")
    elif a < 0 or b < 0 or c < 0:
        print("Invalid input, Enter possitive values for triangle's side")
    else:
        print("Invalid datatype as input, Enter a number. ")

#test case 1:
validate_triangle(5,5,5)

#test case 2:
validate_triangle(5,5,8)

#test case 3:
validate_triangle(1,2,8)

#test case 4:
try:
    a = int(input("Enter side 1: "))
    b = int(input("Enter side 2: "))
    c = int(input("Enter side 3: "))
    validate_triangle(a, b, c)
except Exception as e:
    print("Invalid datatype as input, Enter a number. ")

