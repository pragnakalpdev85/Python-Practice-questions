# Question 3: Find Difference of Two Sets
# Write a program that takes two sets as input and finds the difference (set1 - set2) without using any in-built difference operations.

# Rules:
# No in-built functions allowed (except input() and print())
# Must use loops to find elements in set1 but not in set2
# Handle edge cases (empty sets, no difference)
# Result should contain elements only in set1

# Test Cases:

# Test Case 1:
# Input: set1 = {1, 2, 3, 4, 5}, set2 = {4, 5, 6, 7}
# Output: {1, 2, 3}

# Test Case 2:
# Input: set1 = {10, 20, 30}, set2 = {10, 20, 30}
# Output: {}

# Test Case 3:
# Input: set1 = {'a', 'b', 'c'}, set2 = {'d', 'e'}
# Output: {'a', 'b', 'c'}

def difference_of_two(input_set1, input_set2):
    try:
        
        ans_list = []
        
        #looping through both set and removing the duplicates
        for i in input_set1:
            flag = False
            for j in input_set2:
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
difference_of_two({1, 2, 3, 4, 5}, {4, 5, 6, 7})

#test case 2:
difference_of_two({10, 20, 30},{10, 20, 30})

#test case 3:
difference_of_two({'a', 'b', 'c'},{'d', 'e'})

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
    difference_of_two(input_set1,input_set2)

except Exception:
    print("Invalid input, Enter Two sets")
