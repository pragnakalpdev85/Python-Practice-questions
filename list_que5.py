# Question 5: Find All Pairs with Given Sum
# Write a program that takes a list of integers and a target sum as input, and finds all unique pairs of elements that add up to the target sum.

# Rules:
# No in-built functions allowed (except input() and print())
# Must use nested loops to find pairs
# Handle edge cases (empty list, no pairs found)
# Each pair should be printed only once
# Do not use the same element twice

# Test Cases:

# Test Case 1:
# Input: list = [1, 2, 3, 4, 5], target = 6
# Output: [(1, 5), (2, 4)]

# Test Case 2:
# Input: list = [2, 4, 3, 5, 7, 8], target = 10
# Output: [(2, 8), (3, 7)]

# Test Case 3:
# Input: list = [1, 1, 1, 1], target = 2
# Output: [(1, 1)]

def find_sum_pair(input_list, target):
    try:
        #calculating size of list
        size_list = 0
        for i in input_list:
            size_list += 1

        i = 0
        output_list = []
        while i < size_list:
            #number that sums with i totals targer
            temp = target - input_list[i]
            j = 0
            #find the number in list
            while j < size_list:

                #if present add tuple in list
                if input_list[j] == temp and i != j :
                    already_present = False

                    #check the tuple is already present in the list or not
                    for k in output_list:
                        if k == (input_list[i],input_list[j]) or k == (input_list[j],input_list[i]):
                            already_present = True
                            break
                    if already_present == False:
                        output_list += [tuple((input_list[i],input_list[j])),]

                j += 1
                
            i+=1

        print(output_list)

    except TypeError as e:
        print("Invalid input, ",e)

#test case 1:
find_sum_pair([1, 2, 3, 4, 5],6)

#test case 2:
find_sum_pair([2, 4, 3, 5, 7, 8],10)

#test case 3:
find_sum_pair([1, 1, 1, 1],2)

#test case 4:
try:
    input_list = []
    list_size = int(input("Enter the size of the list: "))
    i = 0
    while i < list_size:
        element = float(input(f"Enter element {i+1}: "))
        input_list += [element,]
        i += 1

    target = int(input("Enter target sum: "))

    find_sum_pair(input_list,target)
except Exception:
    print("Input data type is not valid, please enter a list")

