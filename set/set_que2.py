# Question 2: Find Intersection of Two Sets
# Write a program that takes two sets as input and finds their intersection without using any in-built intersection operations.

# Rules:
# No in-built functions allowed (except input() and print())
# Must use loops to find common elements
# Handle edge cases (no common elements, empty sets)
# Result should only contain elements present in both sets

# Test Cases:

# Test Case 1:
# Input: set1 = {1, 2, 3, 4}, set2 = {3, 4, 5, 6}
# Output: {3, 4}

# Test Case 2:
# Input: set1 = {10, 20, 30}, set2 = {40, 50}
# Output: {}

# Test Case 3:
# Input: set1 = {'a', 'b', 'c'}, set2 = {'b', 'c', 'd'}
# Output: {'b', 'c'}

def intersection_of_two(input_set1, input_set2):
    try:
        duplicate_list = []
        ans_list = []
        #adding first set in duplicate list for comparision
        for i in input_set1:
            duplicate_list += [i,]
        
        #comparing and adding second set in answer
        for i in input_set2:
            flag = False
            for j in duplicate_list:
                if i == j:
                    flag = True
                    break
            if flag == True:
                ans_list += [i,]

        if ans_list == []:
            print({})
        else:   
            ans_set = set(ans_list)
            print(ans_set)
    except TypeError as e:
        print("Invalid input type, ",e)

#test case 1:
intersection_of_two({1, 2, 3, 4}, {3, 4, 5, 6})

#test case 2:
intersection_of_two({10, 20, 30},{40, 50})

#test case 3:
intersection_of_two({'a', 'b', 'c'},{'b', 'c', 'd'})

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
    intersection_of_two(input_set1,input_set2)

except Exception:
    print("Invalid input, Enter Two sets")

