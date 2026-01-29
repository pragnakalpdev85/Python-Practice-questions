# Question 1: Find Union of Two Sets
# Write a program that takes two sets as input and finds their union without using any in-built union operations.

# Rules:
# No in-built functions allowed (except input() and print())
# Must use loops to combine sets
# Handle edge cases (empty sets, identical sets)
# Result should contain no duplicates

# Test Cases:

# Test Case 1:
# Input: set1 = {1, 2, 3}, set2 = {3, 4, 5}
# Output: {1, 2, 3, 4, 5}

# Test Case 2:
# Input: set1 = {10, 20}, set2 = {30, 40}
# Output: {10, 20, 30, 40}

# Test Case 3:
# Input: set1 = {1, 2, 3}, set2 = {}
# Output: {1, 2, 3}

def union_of_two(input_set1, input_set2):
    try:
        
        ans_list = []
        #adding first set in answer
        for i in input_set1:
            ans_list += [i,]
        
        #comparing and adding second set in answer
        for i in input_set2:
            flag = False
            for j in ans_list:
                if i == j:
                    flag = True
                    break
            if flag == False:
                ans_list += [i,]

        if ans_list == []:
            print({})
        else:   
            ans_set = set(ans_list)
            print(ans_set)
    except TypeError as e:
        print("Invalid input type, ",e)

#test case 1:
union_of_two({1, 2, 3}, {3, 4, 5})

#test case 2:
union_of_two({10, 20},{30, 40})

#test case 3:
union_of_two({1, 2, 3},{})

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
    union_of_two(input_set1,input_set2)

except Exception:
    print("Invalid input, Enter Two sets")
