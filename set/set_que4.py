# Question 4: Check Subset
# Write a program that takes two sets as input and checks whether the first set is a subset of the second set without using any in-built subset operations.

# Rules:

# No in-built functions allowed (except input() and print())
# Must use loops to check if all elements of set1 are in set2
# Handle edge cases (empty sets, identical sets)
# Return True if set1 is subset of set2, False otherwise

# Test Cases:

# Test Case 1:
# Input: set1 = {1, 2}, set2 = {1, 2, 3, 4, 5}
# Output: True

# Test Case 2:
# Input: set1 = {1, 2, 6}, set2 = {1, 2, 3, 4, 5}
# Output: False

# Test Case 3:
# Input: set1 = {}, set2 = {1, 2, 3}
# Output: True

def check_subset(input_set1, input_set2):
    try:
        is_subset = True

        for i in input_set1:
            flag = False
            for j in input_set2:
                if i == j:
                    flag = True
                    break
                
            if flag != True:
                return False
        
        return is_subset

    except TypeError as e:
        print("Invalid input type, ",e)

#test case 1:
ans1 = check_subset({1, 2}, {1, 2, 3, 4, 5})
print(ans1)

#test case 2:
ans2 = check_subset({1, 2, 6},{1, 2, 3, 4, 5})
print(ans2)

#test case 3:
ans3 = check_subset({},{1, 2, 3})
print(ans3)

#test case 4:
try:
    input_set1 = []
    set_size1 = int(input("Enter the size of the first set: "))
    i = 0
    while i < set_size1:
        element = input(f"Enter element {i+1}: ")
        input_set1 += [element,]
        i += 1

    input_set2 = []
    set_size2 = int(input("Enter the size of the second set: "))
    j = 0
    while j < set_size2:
        element = input(f"Enter element {j+1}: ")
        input_set2 += [element,]
        j += 1

    input_set1 = set(input_set1)    
    input_set2 = set(input_set2)
    ans4 = check_subset(input_set1,input_set2)
    print(ans4)

except Exception:
    print("Invalid input, Enter Two sets")

