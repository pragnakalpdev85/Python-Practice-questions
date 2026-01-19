# Question 5: Electricity Bill Calculator
# Write a program that calculates the electricity bill based on units consumed. The rate structure is:

# First 100 units: ₹5 per unit
# Next 100 units (101-200): ₹7 per unit
# Next 100 units (201-300): ₹10 per unit
# Above 300 units: ₹15 per unit

# Rules:
# No in-built functions allowed (except input() and print())
# Must use conditional operators
# Handle edge cases (negative units, zero units)
# Display total bill amount

# Test Cases:

# Test Case 1:
# Input: units = 150
# Output: 850
# Explanation: (100 × 5) + (50 × 7) = 500 + 350 = 850

# Test Case 2:
# Input: units = 320
# Output: 2500
# Explanation: (100 × 5) + (100 × 7) + (100 × 10) + (20 × 15) = 500 + 700 + 1000 + 300 = 2500

# Test Case 3:
# Input: units = 75
# Output: 375
# Explanation: 75 × 5 = 375

def e_bill_calculator(units):
    #Validating input vlue
    if (type(units) == int or type(units) == float) and units > 0:
        bill_total = 0

        #calculating bill total
        if units <= 100:
            bill_total = units*5
        elif units > 100 and units <= 200:
            bill_total = (100*5) + (units-100)*7
        elif units > 200 and units <= 300:
            bill_total = (100*5) + (100*7) + (units-200)*10
        else:
            bill_total = (100*5) + (100*7) + (100*10) + (units-300)*15
        
        print(bill_total)

    elif units <= 0:
        print("Invalid input, Enter possitive value of unit.")    
    else:
        print("Invalid datatype as input, Enter a number.")

#test case 1:
e_bill_calculator(150)

#test case 2:
e_bill_calculator(320)

#test case 3:
e_bill_calculator(75)

#test case 4:
try:
    a = int(input("Enter units: "))
    e_bill_calculator(a)
except Exception as e:
    print("Invalid datatype as input, Enter a number. ")

