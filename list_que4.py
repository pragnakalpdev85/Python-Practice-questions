# Question 4: Rotate List
# Write a program that takes a list and an integer k as input, and rotates the list to the right by k positions.

# Rules:
# No in-built functions allowed (except input() and print())
# Must use loops to rotate
# Handle edge cases (k = 0, k > list length, empty list)
# If k is greater than list length, rotate by k % length

# Test Cases:

# Test Case 1:
# Input: list = [1, 2, 3, 4, 5], k = 2
# Output: [4, 5, 1, 2, 3]

# Test Case 2:
# Input: list = [10, 20, 30], k = 1
# Output: [30, 10, 20]

# Test Case 3:
# Input: list = [1, 2, 3, 4], k = 6
# Output: [3, 4, 1, 2]
# Explanation: k = 6 % 4 = 2, so rotate by 2 positions

def rotate_list(input_list, k):
    try:
        #calculating size of list
        size_list = 0
        for i in input_list:
            size_list += 1

        if k >= size_list:
            k %= size_list

        print(k)
        
        output_list = []
        n = size_list
        size_list -= k
        print(n,size_list)
        #rotating list k times
        while size_list < n:
            output_list += [input_list[size_list], ]
            size_list += 1
        
        j = 0
        while j < n-k:
            output_list += [input_list[j], ]
            j += 1

        print(output_list)


    except TypeError as e:
        print("Invalid input, ",e)

#test case 1:
rotate_list([1, 2, 3, 4, 5],2)

#test case 2:
rotate_list([10, 20, 30],1)

#test case 3:
rotate_list([1, 2, 3, 4],6)

#test case 4:
try:
    input_list = []
    list_size = int(input("Enter the size of the list: "))
    i = 0
    while i < list_size:
        element = input(f"Enter element {i+1}: ")
        input_list += [element,]
        i += 1

    k = int(input("Enter Possition to rotate: "))

    rotate_list(input_list,k)
except Exception:
    print("Input data type is not valid, please enter a list")



