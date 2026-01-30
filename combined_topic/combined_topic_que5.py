# Question 5: Data Statistics Calculator 
# Write a program that reads numeric data from a file (one number per line) and calculates: mean, median, mode, range, and standard deviation. Store results in a dictionary and write to output file.

# Rules:
# You can use file operations: open(), read(), write(), close()
# Must use loops, lists, dictionaries, and functions
# Create separate functions for each statistical measure
# Handle edge cases (empty file, single number)
# No statistical libraries allowed

# Test Cases:

# Test Case 1:
# Input file: 10, 20, 30, 40, 50
# Output file:
# Mean: 30.0
# Median: 30
# Mode: No mode (all unique)
# Range: 40
# Standard Deviation: 14.14

# Test Case 2:
# Input file: 5, 5, 5, 5
# Output file:
# Mean: 5.0
# Median: 5
# Mode: 5
# Range: 0
# Standard Deviation: 0.0

# Test Case 3:
# Input file: 1, 2, 3, 2, 1
# Output file:
# Mean: 1.8
# Median: 2
# Mode: 1, 2
# Range: 2
# Standard Deviation: 0.75

def sort_numbers(num_list: list) -> list:
    '''
    sort list elements
    
    Args:
        num_list (list): list of numbers
    Returns:
        list: sorted list
    '''
    size_list = 0
    for elements in num_list:
        size_list += 1

    index1 = 0
    while index1 < size_list:
        index2 = 0
        while index2 < size_list-index1-1:
            if num_list[index2] > num_list[index2+1]:
                temp = num_list[index2+1]
                num_list[index2+1] = num_list[index2]
                num_list[index2] = temp
            index2 += 1
        index1 += 1

    return num_list

def mean(num_list: list) -> float:
    '''
    calculates mean of numbers
    
    Args:
        num_list (list): list of numbers
    Returns:
        float: mean of numbers
    '''
    sum = 0
    number = 0
    for nums in num_list:
        sum += nums
        number += 1

    return sum/number

def median(num_list: list) -> float:
    '''
    calculates median of numbers
    
    Args:
        num_list (list): list of numbers
    Returns:
        float: median of numbers
    '''
    num_list = sort_numbers(num_list)
    numbers = 0
    for nums in num_list:
        numbers += 1

    if numbers%2 == 0:
        ans = (num_list[(numbers//2)-1] + num_list[(numbers//2)]) / 2
    else:
        ans = num_list[((numbers+1)//2) - 1]
        
    return ans

def mode(num_list: list) -> list:
    '''
    calculates mode of numbers
    
    Args:
        num_list (list): list of numbers
    Returns:
        list: mode of numbers
    '''
    duplicate_dict = {}
    duplicate_list = []
    numbers = 0
    for nums in num_list:
        numbers += 1

    #adding frequency to the dictionary
    for nums in num_list:
        flag = False
        for number in duplicate_list:
            if number == nums:
                flag = True
                break
        if flag == True:
            temp = duplicate_dict[nums]+1
            duplicate_dict[nums] = temp
        else:
            duplicate_dict[nums] = 1
            duplicate_list += [nums,]
    
    #finding max occurance
    max = float('-inf')
    for keys in duplicate_dict:
        if duplicate_dict[keys] > max:
            max = duplicate_dict[keys]
    
    if max == 1:
        return []
    
    #finding values with maximum occurence
    ans_list = []
    for elements in duplicate_list:
        if duplicate_dict[elements] == max:
            ans_list += [elements]
        
    return ans_list

def range(num_list: list) -> float:
    '''
    calculates range of numbers
    
    Args:
        num_list (list): list of numbers
    Returns:
        float: range of numbers
    '''
    numbers = 0
    for nums in num_list:
        numbers += 1
    #calculating range
    sorted_list = sort_numbers(num_list)
    return sorted_list[numbers-1] - sorted_list[0]

def standard_deviation(num_list: list) -> float:
    '''
    calculates standard deviation of numbers
    
    Args:
        num_list (list): list of numbers
    Returns:
        float: standard deviation of numbers
    '''
    mean_of_numbers = mean(num_list)

    numbers = 0
    for nums in num_list:
        numbers += 1

    #calculating variance
    sum = 0
    for nums in num_list:
        sum += (nums-mean_of_numbers)**2

    #calculating standard deviation
    variance = sum/numbers
    return variance**0.5

def data_statistic_calculator(input_file_name: str, output_file_name: str) -> str:
    '''
    reads file and calculate mean, median, mode, range and standard deviation

    Args:
        file_name (str): name of the input file
    
    Returns:
        str: output data as input
    '''
    try:
        flag = False
        check_word1 = ''
        for chars in input_file_name:
            if flag == True:
                check_word1 += chars
            if chars == '.':
                flag = True
            
        flag = False
        check_word2 = ''
        for chars in input_file_name:
            if flag == True:
                check_word2 += chars
            if chars == '.':
                flag = True
        
        if check_word1 != 'txt' and check_word2 != 'txt':
            raise FileNotFoundError("File Should be .txt format.")

        with open(input_file_name,'r') as file:
            data = file.read()

        if data == '':
            return "File is Empty"

        data_size = 0
        for index in data:
            data_size += 1
        
        number_list = []
        word = ''
        index = 0
        #seprating and puting all number into number list
        for char in data:
            if char == ' ' or char == '\n' or index == data_size-1:
                if index == data_size-1 and char != ' ':
                    word += char

                if (char == '\n' or index == data_size-1) and word != '':
                    if word != "\n" and word != " ":
                        number_list += [float(word),]
                        word = ''
            else:
                word += char
            index += 1

        ans_dict = {}
        ans_dict['mean'] = mean(number_list)
        ans_dict['median'] = median(number_list)
        #verifying mode
        mode_list = mode(number_list)
        if mode_list == []:
            ans_dict['mode'] = "No Mode"
        else:
            ans_dict['mode'] = mode_list

        ans_dict['range'] = range(number_list)
        ans_dict['standard_deviation'] = standard_deviation(number_list)

        output_data = f"Mean: {ans_dict['mean'] : 0.2f}\nMedian: {ans_dict['median'] : 0.2f}\nMode:"

        #calculting mode list length
        if mode_list != []:
            numbers = 0
            for index in mode_list:
                if numbers == 0:
                    output_data += f" {index}"
                else:
                    output_data += f", {index}"
                numbers += 1
        else:
            output_data += f"{mode_list}"
        output_data += f"\nRange: {ans_dict['range']}\nStandard Deviation: {ans_dict['standard_deviation']: 0.2f}"

        with open(output_file_name,'w') as file:
            file.write(output_data)

        return output_data

    except FileNotFoundError as e:
        print("File Not Found: ",e)
    except OSError as e:
        print("Given File name is not defined: ",e)
    except TypeError as e:
        print("Invalid input data. Please enter valid data types in input file: ",e)
    except ValueError as e:
        print("Invalid values as input, Please enter valid data in input file: ",e)

def main():
    try:
        flag = False
        input_file_name = ''
        while flag == False:
            input_file_name = input("Enter input file name: ")
            try:
                with open(input_file_name,'r') as f:
                    flag = True
            except FileNotFoundError:
                print("File not found Enter name again")

        flag = False
        output_file_name = ''
        while flag == False:
            output_file_name = input("Enter output file name: ")
            try:
                with open(input_file_name,'r') as f:
                    flag = True
            except FileNotFoundError:
                print("File not found Enter name again")

        ans = data_statistic_calculator(input_file_name,output_file_name)
        print(ans)

    except FileNotFoundError as e:
        print("File Not Found: ",e)
    except OSError as e:
        print("Given File name is not defined: ",e)
    except TypeError as e:
        print("Invalid input, ",e)
    except ValueError as e:
        print("Invalid input, ",e)

if __name__ == "__main__":
    main()
