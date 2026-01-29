# Question 3: Merge Two Sorted Lists
# Write a program that takes two sorted lists as input and merges them into a single sorted list without using any sorting function.

# Rules:
# No in-built functions allowed (except input() and print())
# Must use loops to merge
# Handle edge cases (one or both lists empty)
# Result must be sorted in ascending order

# Test Cases:

# Test Case 1:
# Input: list1 = [1, 3, 5, 7], list2 = [2, 4, 6, 8]
# Output: [1, 2, 3, 4, 5, 6, 7, 8]

# Test Case 2:
# Input: list1 = [1, 2, 3], list2 = [4, 5, 6]
# Output: [1, 2, 3, 4, 5, 6]

# Test Case 3:
# Input: list1 = [], list2 = [1, 2, 3]
# Output: [1, 2, 3]

def merge_sorted_list(list1, list2):
    try:
        #calculating length of the lists
        length1 = 0
        length2 = 0
        for i in list1:
            length1 += 1
        for i in list2:
            length2 += 1

        ans_list = []
        #comparing to list and aranging in sorted order in one list 
        if length1 >= 0 and length2 >= 0:
            i = 0
            j = 0
            while i < length1 and j < length2 :
                #fist list element is less than second list element
                if list1[i] < list2[j]:
                    ans_list += [list1[i],]
                    i += 1

                #second list element is less than first list element
                elif list2[j] < list1[i]:
                    ans_list += [list2[j],]
                    j += 1

                #both are same
                elif list1[i] == list2[j]:
                    ans_list += [list1[i],]
                    ans_list += [list1[i],]
                    i += 1
                    j += 1
                        

            #remaining elements in list1
            while i < length1:
                ans_list += [list1[i],]
                i += 1

            #remaining element in list2
            while j < length2:
                ans_list += [list2[j],]
                j += 1
            
            print(ans_list)
                
        else:
            print("Invalid input, List must contain atleast one value.")

    except TypeError as e:
        print("Invalid input, ",e)


#test case 1:
merge_sorted_list([1, 3, 5, 7],[2, 4, 6, 8])

#test case 2:
merge_sorted_list([1, 2, 3],[4, 5, 6])

#test case 3:
merge_sorted_list([],[1,2,3])

#test case 4:
merge_sorted_list(["a","b","d","f"],["c","e","g"])

#test case 5:
try:
    input_list1 = []
    list_size1 = int(input("Enter the size of the first list: "))
    i = 0
    while i < list_size1:
        element = input(f"Enter element {i+1}: ")
        input_list1 += [element,]
        i += 1

    input_list2 = []
    list_size2 = int(input("Enter the size of the second list: "))
    j = 0
    while j < list_size2:
        element = input(f"Enter element {j+1}: ")
        input_list2 += [element,]
        j += 1
    
    merge_sorted_list(input_list1,input_list2)

except Exception:
    print("Invalid input, Enter Two list")



