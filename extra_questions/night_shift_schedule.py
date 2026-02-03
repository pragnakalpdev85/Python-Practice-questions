# Problem Statement:
# A company has 10 employees and needs to schedule them for night shifts.

# Rules:
# * Total shifts in a month: 30 days
# * Each employee must work exactly 3 night shifts
# * No employee can work consecutive nights
# * At least 1 employee must be on duty each night

# Employee List:
# E001,Alice
# E002,Bob
# E003,Charlie
# E004,Diana
# E005,Eve
# E006,Frank
# E007,Grace
# E008,Henry
# E009,Iris
# E010,Jack

# Expected Output:
# Total employees: 10

# Task 1: Generating Schedule
# Generated Schedule:
# --------------------------------------------------
# Day  1: E001, E005
# Day  2: E003, E008
# Day  3: E002, E007
# Day  4: E004, E009
# Day  5: E006, E010
# Day  6: E001, E003
# Day  7: E005, E008
# Day  8: E002, E004
# ...
# Day 30: E006, E009

# Task 2: Validating Schedule
#  1: Each employee has exactly 3 shifts
#  2: No consecutive shifts
#  3: Every day is covered
import re
import os

def validate_filename_input(file_name: str) -> bool:
    '''
    validates file name input
    
    Args:
        name (str): name of the file
    returns:
        bool: file formate is correct or not
    '''
    if not file_name.endswith('.txt'):
        print("File formate is incorrect, Enter file name again")
        return False
    
    #file exist of not
    if not os.path.exists(file_name):
        print("File does not exist, Enter file name again")
        return False
    
    return True

def schedule_shifts(employee_dict: dict) -> dict:
    '''
    schedules shifts of employes
    
    Args:
        employee_dict (dict):dictionary of employees
    Returns:
        dict: returns schedule of shifts 
    '''
    if len(employee_dict) != 10:
        return {}
    
    employee_list = [id for id in employee_dict]
    day = 0
    flag = True
    schedule_dict = {}
    #scheduling shifts of every employees
    while day < 30:
        index = day%5
        
        if flag == True:
            schedule_dict[day] = tuple((employee_list[index],employee_list[index+5]))
        else:
            schedule_dict[day] = tuple((employee_list[index+5],employee_list[index]))

        flag = not flag if index == 4 else flag
        day += 1

    return schedule_dict

def validate_schedule(schedule :dict) -> str:
    '''
    validates generated schedule

    Args:
        schedule (dict): schedule of shifts
    Returns:
        str: schedule is correct or incorrect
    '''
    if len(schedule) != 30:
        return "Every day of the month is not covered"
    
    prev_night_shift = ''
    shift_dict = {}
    for days in schedule:
        #counting each employee's night shifts
        temp_tuple = schedule[days]
        if temp_tuple[1] in shift_dict:
            temp = shift_dict[temp_tuple[1]] + 1
            shift_dict[temp_tuple[1]] = temp
        else:
            shift_dict[temp_tuple[1]] = 1

        #chech if employee is not working two consicutive nights
        if prev_night_shift == temp_tuple[1]:
            return f"Employee {temp_tuple[1]} is working two consecutive night shifts"

        prev_night_shift = temp_tuple[1]

    #check every employee has 3 night shifts or not
    for shifts in shift_dict:
        if shift_dict[shifts] != 3:
            return f"Employee {shifts} is not working exactly 3 nights"
        
    return "Schedule is correct"

def generate_schedule(input_file_name: str, output_file_name: str) -> str:
    '''
    Generates schedule from employee data
    
    Args:
        input_file_name (str): name of input data file
        output_file_name (str): name of the output data file
    Returns:
        str: schedule of shifts
    '''
    with open(input_file_name, 'r') as file:
        data = file.readlines()

    try: 
        emp_dict = {}
        index = 0
        for lines in data:
            if index == 0:
                index += 1
                continue

            line = lines.strip()
            name_id = re.split(r"\n|,| ",line)
            emp_dict[name_id[0]] = name_id[1]

            index += 1

        if index != 11:
            return "Invalid input data in file"
    except KeyError as e:
        return "invalid input data in file"
    except IndexError as e:
        return "invalid input data in file"

   
    
    ans = schedule_shifts(emp_dict)
    if ans == dict:
        return 
    output = "Generated Schedule:\n--------------------------------------------------"
    for days in ans:
        output += f"\nDay {days+1}: {ans[days][0]}, {ans[days][1]}"

    with open(output_file_name,'w') as file:
        file.write(output)

    return output
        
def generate_validation_message(input_file_name: str) -> str:
    '''
    Generates validation message from schedule
    
    Args:
        input_file_name (str): name of input data file
        output_file_name (str): name of the output data file
    Returns:
        str: validation message
    '''
    with open(input_file_name, 'r') as file:
        data = file.readlines()

    ans_dict = {}
    index = 0
    for lines in data:
        if index == 0 or index == 1:
            index += 1
            continue

        line = lines.strip()
        schedule = re.split(r"\n|,| ",line)
        ans_dict[index-2] = tuple((schedule[2],schedule[4]))
        index += 1

    ans = validate_schedule(ans_dict)
    return ans


def main():
    try:
        operation_index = int(input("Enter 1 for Scheduling shift or Enter 2 for validating schedule: "))
        match operation_index:
            case 1:
                flag = False
                while flag == False:
                    input_file_name = input("Enter input file name: ")
                    flag = validate_filename_input(input_file_name)

                flag = False
                while flag == False:
                    output_file_name = input("Enter output file name: ")
                    flag = validate_filename_input(output_file_name)

                ans = generate_schedule(input_file_name, output_file_name)
                print(ans)
        
            case 2:
                flag = False
                while flag == False:
                    input_file_name = input("Enter input file name: ")
                    flag = validate_filename_input(input_file_name)
                
                ans = generate_validation_message(input_file_name)
                print(ans)
            
            case _:
                print("Incorrect opetaion number enter again")

    except FileNotFoundError as e:
        print("File Not Found")
    except OSError as e:
        print("Given File name is not defined")
    except ValueError as e:
        print("Invalid input in number of files.")

if __name__ == '__main__':
    main()