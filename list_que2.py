# Question 2: Remove Duplicates from List
# Write a program that takes a list as input and removes all duplicate elements while preserving the original order of first occurrences.

# Rules:
# No in-built functions allowed (except input() and print())
# Must use loops to check and remove duplicates
# Handle edge cases (empty list, no duplicates)
# Preserve the order of first occurrence

# Test Cases:

# Test Case 1:
# Input: [1, 2, 3, 2, 4, 1, 5]
# Output: [1, 2, 3, 4, 5]

# Test Case 2:
# Input: [10, 10, 10, 10]
# Output: [10]

# Test Case 3:
# Input: [5, 4, 3, 2, 1]
# Output: [5, 4, 3, 2, 1]

def remove_duplicates(input_list):
    try:
        duplicate_list = []
        #looping through input list
        for i in input_list:
           
            #looping through unique list to check there is duplicate present
            duplicate_present = False
            for j in duplicate_list:
               if i == j:
                   duplicate_present = True
                   break
            #if unique element then add to uniquelist
            if duplicate_present == False:
               duplicate_list += [i,]
            
        print(duplicate_list)
    except TypeError as e:
        print("Invalid input data type, ",e)

#test case 1:
remove_duplicates([1, 2, 3, 2, 4, 1, 5])

#test case 2:
remove_duplicates([10, 10, 10, 10])

#test case 3:
remove_duplicates([5, 4, 3, 2, 1])

#test case 4:
try:
    input_list = []
    print("Write stop to End input.")
    while True:
        list_elements = input("Enter Element :")
        if list_elements == "stop":
            break
        input_list.append(int(list_elements))

    remove_duplicates(input_list)
except Exception:
    print("Input data type is not valid, please enter a list")
