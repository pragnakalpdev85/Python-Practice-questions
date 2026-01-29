# 100 people are standing in a circle in order of 1 to 100.

# No.1 has a sword. He kills the next person (i.e., no. 2) and passes the sword to the next (i.e., no. 3).

# All people do the same until only one survives.

# Write a Python program to find the person who survives.

#  1. The code should work for any number of people.
#  2. It should work properly if I change the number of starting person.
# for example, in a group of 100 people if number 1 starts killing then the answer will be 73 but if we start with number 5 then the answer will be 77.

#Approach:
#no_of_people : index of ans.
# 1  :  1           
# 2  :  1           
# 3  :  3           
# 4  :  1         
# 5  :  3           
# 6  :  5        
# 7  :  7
# 8  :  1
# 9  :  3
# 10  :  5
# 11  :  7
# 12  :  9
# 13  :  11
# 14  :  13
# 15  :  15
# 16  :  1
# 17  :  3
# 18  :  5
# 19  :  7
# 20  :  9
#the no_of_people and index of answer output is given above


#For every no_of_people The index of the person who remain alive is same

#To find that index

#These indexes are in series of odd numbers
#we have to find the output odd number where the no_of_people and index of ans is same 
# example: 3:3, 7:7, 15:15

#Every time when no_of_people and index of ans is same the odd number series start again from 1,3,5...

#To find the maximum in index of answer series where the no_of_people and the index of ans become same 
# eaxmple for no_of_people = 100 the maximum index of ans is 63

#this numbers are in series - 3, 7, 15, 31, 63 ,.... for this series if we want to find nth term, we need to use equation 2^n - 1

#to find appropriate value of n which results 2^n-1 be less than no_of_people
# n = floor( log2( no_of_people ) )

#then calculate the nth term
#subtract the nth term from number of people
#which results us for nth odd term as index answer
#for nth odd term equation = 2n - 1

#then returning index-1 from list 

import math

def sword_game(no_of_people, starting_person):
    try:
        if no_of_people > 0 and (starting_person > 0 and starting_person <= no_of_people):

            sword_holders = list(range(starting_person,no_of_people+1))
            sword_holders += list(range(1,starting_person))

            n = math.floor(math.log2(no_of_people))

            odd_term = no_of_people - ((2**n)-1)
            
            index_of_ans = 2*odd_term - 1

            return sword_holders[index_of_ans-1]
    
        else:
            return "Person must be 1 or more, And starting person should not be in between 1 and total number of people."
    except TypeError as e:
        print("Invalid input, ",e)

ans = sword_game(100,101)
print(ans)
