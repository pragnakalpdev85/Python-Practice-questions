# Question 5: Find Symmetric Difference
# Write a program that takes two sets as input and finds their symmetric difference (elements in either set but not in both) without using any in-built symmetric difference operations.

# Rules:
# No in-built functions allowed (except input() and print())
# Must use loops to find elements in either set but not in both
# Handle edge cases (empty sets, identical sets)
# Result should contain elements unique to each set

# Test Cases:

# Test Case 1:
# Input: set1 = {1, 2, 3, 4}, set2 = {3, 4, 5, 6}
# Output: {1, 2, 5, 6}

# Test Case 2:
# Input: set1 = {10, 20, 30}, set2 = {10, 20, 30}
# Output: {}

# Test Case 3:
# Input: set1 = {'a', 'b'}, set2 = {'c', 'd'}
# Output: {'a', 'b', 'c', 'd'}

def symmetric_difference(input_set1, input_set2):
    try:
        duplicate_list = []
        ans_list = []
        #find all duplicates in list ans add unique element from set1 into answer list
        for i in input_set1:
            flag = False
            for j in input_set2:
                if i == j:
                    flag = True
                    break
            if flag == True:
                duplicate_list += [i,]
            else:
                ans_list += [i,]

        #from set2 add all unique element into answer list
        for i in input_set2:
            flag = False
            for j in duplicate_list:
                if i == j:
                    flag = True
                    break
            if flag != True:
                ans_list += [i,]

        #returning ans
        if ans_list == []:
            return {}
        else:   
            ans_set = set(ans_list)
            return ans_set

    except TypeError as e:
        print("Invalid input type, ",e)

#test case 1:
ans1 = symmetric_difference({1, 2, 3, 4}, {3, 4, 5, 6})
print(ans1)

#test case 2:
ans2 = symmetric_difference({10, 20, 30},{10, 20, 30})
print(ans2)

#test case 3:
ans3 = symmetric_difference({'a', 'b'},{'c', 'd'})
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
    ans4 = symmetric_difference(input_set1,input_set2)
    print(ans4)

except Exception:
    print("Invalid input, Enter Two sets")
