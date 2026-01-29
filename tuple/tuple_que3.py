# Question 3: Concatenate Multiple Tuples
# Write a program that takes multiple tuples as input and concatenates them into a single tuple without using the + operator or any in-built functions.

# Rules:
# No in-built functions allowed (except input() and print())
# Must use loops to build the new tuple
# Handle edge cases (empty tuples, single tuple)
# Create a new tuple with all elements

# Test Cases:

# Test Case 1:
# Input: tuple1 = (1, 2, 3), tuple2 = (4, 5, 6)
# Output: (1, 2, 3, 4, 5, 6)

# Test Case 2:
# Input: tuple1 = ('a', 'b'), tuple2 = ('c',), tuple3 = ('d', 'e')
# Output: ('a', 'b', 'c', 'd', 'e')

# Test Case 3:
# Input: tuple1 = (10,), tuple2 = ()
# Output: (10,)

def concatinate_tuples(*input_tuple):
    try:
        #concatinating multiple tuples
        ans_tuple = tuple(j for i in input_tuple for j in i)
        print(ans_tuple)
    except TypeError as e:
        print("Invalid input type, ",e)

#test case 1:
concatinate_tuples((1, 2, 3),(4, 5, 6))

#test case 2:
concatinate_tuples(('a', 'b'),('c',),('d', 'e'))

#test case 3:
concatinate_tuples((10,),())

#test case 4:
concatinate_tuples((),())

#test case 5:
concatinate_tuples((1,),('a','a','b','c'))

