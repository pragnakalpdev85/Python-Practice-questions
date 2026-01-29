# 100 people are standing in a circle in order of 1 to 100.

# No.1 has a sword. He kills the next person (i.e., no. 2) and passes the sword to the next (i.e., no. 3).

# All people do the same until only one survives.

# Write a Python program to find the person who survives.

#  1. The code should work for any number of people.
#  2. It should work properly if I change the number of starting person.
# for example, in a group of 100 people if number 1 starts killing then the answer will be 73 but if we start with number 5 then the answer will be 77.

def sword_game(no_of_people, starting_person):
    try:
        if no_of_people != 0 and (starting_person > 0 and starting_person <= no_of_people):
            

            list_sword_holders = []
            
            i = starting_person
            #appending people from staring person to no of people
            while i <= no_of_people:
                list_sword_holders.append(i)
                i += 1
            
            i = 1
            #appending people from 1 to starting people
            while i < starting_person:
                list_sword_holders.append(i)
                i += 1
            
            #killing the next 
            j = 0
            while len(list_sword_holders) > 1:

                #calculating next person to be killed in reduced list 
                j = (j+1) % len(list_sword_holders)

                #poping killed person from the sword holders list
                list_sword_holders.pop(j)
                
            return list_sword_holders[0]
        else:
            return "Person must be 1 or more, And starting person should not be in between 1 and total number of people."
    except TypeError as e:
        print("Invalid input, ",e)

#test case 2"
for i in range(1,101):
    ans2 = sword_game(i,1)
    print(i," : ",ans2)

