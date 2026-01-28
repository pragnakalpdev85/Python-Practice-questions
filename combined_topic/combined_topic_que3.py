# Question 3: List Operations Suite 
# Write a program that takes a list of integers from user input and provides the following operations using functions: find prime numbers, find perfect numbers, find Armstrong numbers, and store results in separate lists.

# Rules:

# No in-built functions allowed (except input() and print())
# Must create separate functions for each check
# Must use loops, conditionals, and lists
# Handle edge cases (empty list, negative numbers)
# Display all results clearly

# Test Cases:

# Test Case 1:
# Input: [1, 2, 3, 5, 6, 28, 153]
# Output:
# Prime Numbers: [2, 3, 5]
# Perfect Numbers: [6, 28]
# Armstrong Numbers: [1, 2, 3, 5, 6, 153]

# Test Case 2:
# Input: [10, 15, 20]
# Output:
# Prime Numbers: []
# Perfect Numbers: []
# Armstrong Numbers: []

# Test Case 3:
# Input: [1, 2, 3]
# Output:
# Prime Numbers: [2, 3]
# Perfect Numbers: []
# Armstrong Numbers: [1, 2, 3]

def is_prime(input_num: int) -> bool:
    '''
    checks input number is prime or not
    
    Args: 
        input_num (int): number as a input
    Returns:
        bool: True if number is prime else False
    '''
    flag = True

    #checking input is integer or not
    if type(input_num) == int and input_num >= 0:
    
        if(input_num == 1 or input_num == 0): flag = False

        #looping from 2 to input_num/2 and checking the number is completely divisible or not
        index = 2
        while index < (input_num//2)+1:
            if(input_num%index == 0):
                flag = False
                break
            index += 1

        return flag
    else:
        raise ValueError("Enter Positive Integer value as input.")

def is_armstrong(number: int) -> bool:
    '''checks input number is armstrong or not
    
    Args: 
        number (int): number as a input
    Returns:
        bool: True if number is armstrong else False
    '''
    #validating input datatype
    if type(number) == int:

        #validating integer is positive or not
        if number >= 0:

            #all single digit numbers are armstrong
            if number >= 0 and number <= 9:
                return True
            else:
                temp_num = number
                ansnum = 0 
                digitcount = 0

                #counting digit of number
                while number > 0:
                    reminder = number%10
                    number //= 10
                    digitcount += 1
                
                #calculating the sum of digit^digitcount
                number = temp_num
                for i in range(digitcount):
                    reminder = number%10
                    number //= 10
                    ansnum += reminder**digitcount
                
                if(ansnum == temp_num):
                    return True
                else:
                    return False
        else:
            raise ValueError("Enter positive number.")
    else:
        raise ValueError("Enter Integer value as input.")

def is_perfect(input_num: int) -> bool:
    '''checks input number is perfect or not
    
    Args: 
        input_num (int): number as a input
    Returns:
        bool: True if number is perfect else False
    '''
    if type(input_num) == int and input_num >= 0:

        if input_num == 0:
            return False
        
        number = 1
        sum = 0
        #adding all perfect divisors of input number to sum 
        while number < input_num:
            if input_num % number == 0:
                sum += number
            number += 1

        if sum == input_num:
            return True
        else:
            return False
        
    else:
        raise ValueError("Enter positive Integer value as input.")
    
def list_operations(input_list: list) -> str:
    '''
    separate prime numbers, armstrong numbers and perfect numbers from input list
    into 3 different lists 
    
    Args: 
        input_list (list): list of positive numbers as a input
    Returns:
        str: reurns list of prime numbers, armstrong numbers and perfect numbers
    '''
    try:
        if input_list == []:
            return "Empty list as input."
        prime_list = []
        armstrong_list = []
        perfect_list = []

        #looping through input list
        for element in input_list:

            #if element is prime and not already present in prime list then add it in prime list
            if is_prime(element):
                present = False
                for number in prime_list:
                    if element == number:
                        present = True
                        break

                if present != True:
                    prime_list += [element,]

            #if element is armstrong and not already present in armstrong list then add it in armstrong list
            if is_armstrong(element):
                present = False
                for number in armstrong_list:
                    if element == number:
                        present = True
                        break

                if present != True:
                    armstrong_list += [element,]

            #if element is perfect and not already present in perfect list then add it in perfect list
            if is_perfect(element):
                present = False
                for number in perfect_list:
                    if element == number:
                        present = True
                        break

                if present != True:
                    perfect_list += [element,]


        return f'Prime Numbers: {prime_list}\nPerfect Numbers: {perfect_list}\nArmstrong Numbers: {armstrong_list}'
    except TypeError as e:
        print("Invalid input, ",e)
    except ValueError as e:
        print("invalid value as input, ",e)

#defining main function
def main():
    try:
        input_list = []
        list_size = int(input("Enter the size of the list: "))
        i = 0
        while i < list_size:
            element = int(input(f"Enter element {i+1}: "))
            input_list += [element,]
            i += 1

        ans = list_operations(input_list)
        print(ans)
    except ValueError as e:
        print("invalid value as input, ", e)
    except TypeError as e:
        print("Invalid input, ", e)

if __name__ == '__main__':
    main()
