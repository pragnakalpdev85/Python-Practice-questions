# Problem Statement:
# We have a dataset, students_data where some keys and values are accidentally swapped.


# students_data['student_01']['personal_info'] 
# # Incorrect format: {'Vikram': 'name', 'age': 11, 'gender': 'Male'}  
# # Correct format: {'name': 'Vikram', 'age': 11, 'gender': 'Male'}

# Write a Python program that:
# Identifies all mismatched key-value pairs and lists them as comments at the top of your code.
# Swaps the mismatched keys and values back to the correct format.
# Renames the parent key (student_XX) with the student’s actual name.

# If the name already exists, append the class name.
# Example: "student_11" → "Vikram"
# If "Vikram" already exists, then rename it as "Vikram_E".
# Note: The mismatch pattern is the same across all student records.

#Corrections

# student_1['student_01']['personal_info']
#Incorrect format:  {'Vikram': 'name', 'age': 11, 'gender': 'Male'}
#Correct format:  {'name': 'Vikram', 'age': 11, 'gender': 'Male'}

# student_2['student_01']['personal_info']
#Incorrect format:  {'Ananya': 'name', 'age': 13, 'gender': 'Male'}
#Correct format:  {'name': 'Ananya', 'age': 13, 'gender': 'Male'}

# student_3['student_01']['personal_info']
#Incorrect format:  {'Vikram': 'name', 'age': 19, 'gender': 'Male'}
#Correct format:  {'name': 'Vikram', 'age': 19, 'gender': 'Male'}

# student_4['student_01']['personal_info']
#Incorrect format:  {'Rohit': 'name', 'age': 19, 'gender': 'Female'}
#Correct format:  {'name': 'Rohit', 'age': 19, 'gender': 'Female'}

# student_5['student_01']['personal_info']
#Incorrect format:  {'Priya': 'name', 'age': 17, 'gender': 'Female'}
#Correct format:  {'name': 'Priya', 'age': 17, 'gender': 'Female'}

# student_6['student_01']['personal_info']
#Incorrect format:  {'Rahul': 'name', 'age': 12, 'gender': 'Female'}
#Correct format:  {'name': 'Rahul', 'age': 12, 'gender': 'Female'}

# student_7['student_01']['personal_info']
#Incorrect format:  {'Meera': 'name', 'age': 18, 'gender': 'Male'}
#Correct format:  {'name': 'Meera', 'age': 18, 'gender': 'Male'}

# student_8['student_01']['personal_info']
#Incorrect format:  {'Meera': 'name', 'age': 15, 'gender': 'Female'}
#Correct format:  {'name': 'Meera', 'age': 15, 'gender': 'Female'}

# student_9['student_01']['personal_info']
#Incorrect format:  {'Rohit': 'name', 'age': 13, 'gender': 'Male'}
#Correct format:  {'name': 'Rohit', 'age': 13, 'gender': 'Male'}

# student_10['student_01']['personal_info']
# Incorrect format: {'Sneha': 'name', 'age': 15, 'gender': 'Female'}
# Correct format: {'name': 'Sneha', 'age': 15, 'gender': 'Female'}

# student_11['student_01']['personal_info']
# Incorrect format: {'Aarav': 'name', 'age': 16, 'gender': 'Male'}
# Correct format: {'name': 'Aarav', 'age': 16, 'gender': 'Male'}

# student_12['student_01']['personal_info']
# Incorrect format: {'Neha': 'name', 'age': 14, 'gender': 'Female'}
# Correct format: {'name': 'Neha', 'age': 14, 'gender': 'Female'}

# student_13['student_01']['personal_info']
# Incorrect format: {'Karan': 'name', 'age': 17, 'gender': 'Male'}
# Correct format: {'name': 'Karan', 'age': 17, 'gender': 'Male'}

# student_14['student_01']['personal_info']
# Incorrect format: {'Ananya': 'name', 'age': 12, 'gender': 'Female'}
# Correct format: {'name': 'Ananya', 'age': 12, 'gender': 'Female'}

# student_15['student_01']['personal_info']
# Incorrect format: {'Rohit': 'name', 'age': 15, 'gender': 'Male'}
# Correct format: {'name': 'Rohit', 'age': 15, 'gender': 'Male'}

# student_16['student_01']['personal_info']
# Incorrect format: {'Priya': 'name', 'age': 18, 'gender': 'Female'}
# Correct format: {'name': 'Priya', 'age': 18, 'gender': 'Female'}

# student_17['student_01']['personal_info']
# Incorrect format: {'Aarav': 'name', 'age': 20, 'gender': 'Male'}
# Correct format: {'name': 'Aarav', 'age': 20, 'gender': 'Male'}

# student_18['student_01']['personal_info']
# Incorrect format: {'Sneha': 'name', 'age': 19, 'gender': 'Female'}
# Correct format: {'name': 'Sneha', 'age': 19, 'gender': 'Female'}

# student_19['student_01']['personal_info']
# Incorrect format: {'Karan': 'name', 'age': 13, 'gender': 'Male'}
# Correct format: {'name': 'Karan', 'age': 13, 'gender': 'Male'}

# student_20['student_01']['personal_info']
# Incorrect format: {'Neha': 'name', 'age': 15, 'gender': 'Female'}
# Correct format: {'name': 'Neha', 'age': 15, 'gender': 'Female'}

# student_1
# Incorrect format:  {'class': 'D', 'subjects': {'Math': 64, 'Science': 71, 'English': 78, 'History': 71, 'Geography': 99}}
# Correct format:  {'class': 'D'}
# Correct format:  {'class': 'D', 'subjects': {'Math': 64, 'Science': 71, 'English': 78, 'History': 71, 'Geography': 99}}

# student_3
# Incorrect format:  {'E': 'class', 'subjects': {'Math': 71, 'Science': 52, 'English': 40, 'History': 73, 'Geography': 97}}
# Correct format:  {'class': 'E'}
# Correct format:  {'class': 'E', 'subjects': {'Math': 71, 'Science': 52, 'English': 40, 'History': 73, 'Geography': 97}}

# student_4
# Incorrect format:  {'B': 'class', 'subjects': {'Math': 77, 'Science': 48, 'English': 47, 'History': 70, 'Geography': 92}}
# Correct format:  {'class': 'B'}
# Correct format:  {'class': 'B', 'subjects': {'Math': 77, 'Science': 48, 'English': 47, 'History': 70, 'Geography': 92}}

# student_5
# Incorrect format:  {'D': 'class', 'subjects': {'Math': 43, 'Science': 56, 'English': 57, 'History': 44, 'Geography': 68}}
# Correct format:  {'class': 'D'}
# Correct format:  {'class': 'D', 'subjects': {'Math': 43, 'Science': 56, 'English': 57, 'History': 44, 'Geography': 68}}

# student_6
# Incorrect format:  {'E': 'class', 'subjects': {'Math': 80, 'Science': 92, 'English': 84, 'History': 86, 'Geography': 58}}
# Correct format:  {'class': 'E'}
# Correct format:  {'class': 'E', 'subjects': {'Math': 80, 'Science': 92, 'English': 84, 'History': 86, 'Geography': 58}}

# student_7
# Incorrect format:  {'D': 'class', 'subjects': {'Math': 60, 'Science': 73, 'English': 50, 'History': 57, 'Geography': 77}}
# Correct format:  {'class': 'D'}
# Correct format:  {'class': 'D', 'subjects': {'Math': 60, 'Science': 73, 'English': 50, 'History': 57, 'Geography': 77}}

# student_8
# Incorrect format:  {'D': 'class', 'subjects': {'Math': 89, 'Science': 57, 'English': 93, 'History': 90, 'Geography': 59}}
# Correct format:  {'class': 'D'}
# Correct format:  {'class': 'D', 'subjects': {'Math': 89, 'Science': 57, 'English': 93, 'History': 90, 'Geography': 59}}

# student_9
# Incorrect format:  {'D': 'class', 'subjects': {'Math': 61, 'Science': 40, 'English': 87, 'History': 71, 'Geography': 65}}
# Correct format:  {'class': 'D'}
# Correct format:  {'class': 'D', 'subjects': {'Math': 61, 'Science': 40, 'English': 87, 'History': 71, 'Geography': 65}}

# student_10
# Incorrect format:  {'C': 'class', 'subjects': {'Math': 69, 'Science': 95, 'English': 59, 'History': 71, 'Geography': 79}}
# Correct format:  {'class': 'C'}
# Correct format:  {'class': 'C', 'subjects': {'Math': 69, 'Science': 95, 'English': 59, 'History': 71, 'Geography': 79}}

# student_11
# Incorrect format:  {'B': 'class', 'subjects': {'Math': 55, 'Science': 62, 'English': 74, 'History': 68, 'Geography': 81}}
# Correct format:  {'class': 'B'}
# Correct format:  {'class': 'B', 'subjects': {'Math': 55, 'Science': 62, 'English': 74, 'History': 68, 'Geography': 81}}

# student_12
# Incorrect format:  {'A': 'class', 'subjects': {'Math': 92, 'Science': 88, 'English': 69, 'History': 72, 'Geography': 85}}
# Correct format:  {'class': 'A'}
# Correct format:  {'class': 'A', 'subjects': {'Math': 92, 'Science': 88, 'English': 69, 'History': 72, 'Geography': 85}}

# student_13
# Incorrect format:  {'C': 'class', 'subjects': {'Math': 66, 'Science': 73, 'English': 58, 'History': 70, 'Geography': 91}}
# Correct format:  {'class': 'C'}
# Correct format:  {'class': 'C', 'subjects': {'Math': 66, 'Science': 73, 'English': 58, 'History': 70, 'Geography': 91}}

# student_14
# Incorrect format:  {'E': 'class', 'subjects': {'Math': 74, 'Science': 61, 'English': 88, 'History': 77, 'Geography': 63}}
# Correct format:  {'class': 'E'}
# Correct format:  {'class': 'E', 'subjects': {'Math': 74, 'Science': 61, 'English': 88, 'History': 77, 'Geography': 63}}

# student_15
# Incorrect format:  {'D': 'class', 'subjects': {'Math': 85, 'Science': 67, 'English': 72, 'History': 91, 'Geography': 64}}
# Correct format:  {'class': 'D'}
# Correct format:  {'class': 'D', 'subjects': {'Math': 85, 'Science': 67, 'English': 72, 'History': 91, 'Geography': 64}}

# student_16
# Incorrect format:  {'A': 'class', 'subjects': {'Math': 90, 'Science': 84, 'English': 79, 'History': 87, 'Geography': 92}}
# Correct format:  {'class': 'A'}
# Correct format:  {'class': 'A', 'subjects': {'Math': 90, 'Science': 84, 'English': 79, 'History': 87, 'Geography': 92}}

# student_17
# Incorrect format:  {'B': 'class', 'subjects': {'Math': 77, 'Science': 68, 'English': 83, 'History': 80, 'Geography': 71}}
# Correct format:  {'class': 'B'}
# Correct format:  {'class': 'B', 'subjects': {'Math': 77, 'Science': 68, 'English': 83, 'History': 80, 'Geography': 71}}

# student_18
# Incorrect format:  {'E': 'class', 'subjects': {'Math': 64, 'Science': 72, 'English': 59, 'History': 85, 'Geography': 78}}
# Correct format:  {'class': 'E'}
# Correct format:  {'class': 'E', 'subjects': {'Math': 64, 'Science': 72, 'English': 59, 'History': 85, 'Geography': 78}}

# student_19
# Incorrect format:  {'C': 'class', 'subjects': {'Math': 71, 'Science': 74, 'English': 62, 'History': 69, 'Geography': 73}}
# Correct format:  {'class': 'C'}
# Correct format:  {'class': 'C', 'subjects': {'Math': 71, 'Science': 74, 'English': 62, 'History': 69, 'Geography': 73}}

# student_20
# Incorrect format:  {'A': 'class', 'subjects': {'Math': 88, 'Science': 91, 'English': 75, 'History': 82, 'Geography': 79}}
# Correct format:  {'class': 'A'}
# Correct format:  {'class': 'A', 'subjects': {'Math': 88, 'Science': 91, 'English': 75, 'History': 82, 'Geography': 79}}

def personal_info_correction(p_info: dict) -> dict:
    '''
    correctes personal information

    Args:
        p_info (dict): dictionary of personal information
    Returns:
        dict: corrected personal information
    '''
    temp = {}
    
    for personal_info in p_info:
        if p_info[personal_info] == 'name' or p_info[personal_info] == 'age' or p_info[personal_info] == 'gender':
            temp[p_info[personal_info]] = personal_info
        else:
            temp[personal_info] = p_info[personal_info]

    return temp

def academic_info_correction(a_info: dict) -> dict:
    '''
    correctes academic information

    Args:
        p_info (dict): dictionary of academic information
    Returns:
        dict: corrected academic information
    '''
    temp = {}
    for academic_info in a_info:
        if academic_info == 'subjects':
            subjects = ['Math', 'Science', 'English', 'History', 'Geography']
            subject_dict = {}
            for marks in a_info['subjects']:
                
                if a_info['subjects'][marks] in subjects:
                    subject_dict[a_info['subjects'][marks]] = marks
                else:
                    subject_dict[marks] = a_info['subjects'][marks]
            temp["subjects"] = subject_dict
        elif a_info[academic_info] == 'class':
            temp[a_info[academic_info]] = academic_info
        else:
            temp[academic_info] = a_info[academic_info]

    return temp

def contact_info_correction(c_info: dict) -> dict:
    '''
    correctes contact information

    Args:
        p_info (dict): dictionary of contact information
    Returns:
        dict: corrected contact information
    '''
    temp = {}
    for contact_info in c_info:
        if c_info[contact_info] == 'city' or c_info[contact_info] == 'phone':
            temp[c_info[contact_info]] = contact_info
        else:
            temp[contact_info] = c_info[contact_info]
    
    return temp

def assign_name_to_key(student_data: dict) -> dict:
    '''
    assigns student name to key of student data
    
    Args:
        student_data (dict): data of students
    Returns:
        dict: modified dictionary
    '''
    new_dict = {}
    name_list = []
    for students in student_data:
        name = student_data[students]['personal_info']['name']
        if name in name_list:
            key = f"{name}_{student_data[students]['academic_info']['class']}"
            new_dict[key] =  student_data[students]
        else:
            new_dict[name] = student_data[students]
            name_list += [name,]

    return new_dict

def correct_dictionary(students_data: dict) -> dict:
    '''
    Corrects student dictionary data
    
    Args:
        student_dict (dict): student data dictionary
    Returns:
        dict: corrected stdudent data dictionary
    '''
    for student in students_data:

        for info in students_data[student]:
            p_info = students_data[student]['personal_info']
            students_data[student]['personal_info'] = personal_info_correction(p_info)

            a_info = students_data[student]['academic_info']
            students_data[student]['academic_info'] = academic_info_correction(a_info)

            c_info = students_data[student]['contact_info']
            students_data[student]['contact_info'] = contact_info_correction(c_info)

    students_data = assign_name_to_key(students_data)
    return students_data

def main():
    students_data = {
        'student_1': {
            'personal_info': {'Vikram': 'name', 'age': 11, 'gender': 'Male'},
            'academic_info': {'D': 'class',
            'subjects': {'Math': 64, 'Science': 71, 'English': 78, 'History': 71, 'Geography': 99}},
            'contact_info': {'Chennai': 'city', 'phone': '+919899904531'}
        },
        'student_2': {
            'personal_info': {'Ananya': 'name', 'age': 13, 'gender': 'Male'},
            'academic_info': {'A': 'class',
            'subjects': {'Math': 43, 'Science': 43, 'English': 72, 'History': 97, 'Geography': 55}},
            'contact_info': {'Delhi': 'city', 'phone': '+918558171124'}
        },
        'student_3': {
            'personal_info': {'Vikram': 'name', 'age': 19, 'gender': 'Male'},
            'academic_info': {'E': 'class',
            'subjects': {'Math': 71, 'Science': 52, 'English': 40, 'History': 73, 'Geography': 97}},
            'contact_info': {'Pune': 'city', 'phone': '+918013586877'}
        },
        'student_4': {
            'personal_info': {'Rohit': 'name', 'age': 19, 'gender': 'Female'},
            'academic_info': {'B': 'class',
            'subjects': {'Math': 77, 'Science': 48, 'English': 47, 'History': 70, 'Geography': 92}},
            'contact_info': {'Chennai': 'city', 'phone': '+917178703106'}
        },
        'student_5': {
            'personal_info': {'Priya': 'name', 'age': 17, 'gender': 'Female'},
            'academic_info': {'D': 'class',
            'subjects': {'Math': 43, 'Science': 56, 'English': 57, 'History': 44, 'Geography': 68}},
            'contact_info': {'Delhi': 'city', 'phone': '+918073815247'}
        },
        'student_6': {
            'personal_info': {'Rahul': 'name', 'age': 12, 'gender': 'Female'},
            'academic_info': {'E': 'class',
            'subjects': {'Math': 80, 'Science': 92, 'English': 84, 'History': 86, 'Geography': 58}},
            'contact_info': {'Chennai': 'city', 'phone': '+919452966565'}
        },
        'student_7': {
            'personal_info': {'Meera': 'name', 'age': 18, 'gender': 'Male'},
            'academic_info': {'D': 'class',
            'subjects': {'Math': 60, 'Science': 73, 'English': 50, 'History': 57, 'Geography': 77}},
            'contact_info': {'Mumbai': 'city', 'phone': '+919871300971'}
        },
        'student_8': {
            'personal_info': {'Meera': 'name', 'age': 15, 'gender': 'Female'},
            'academic_info': {'D': 'class',
            'subjects': {'Math': 89, 'Science': 57, 'English': 93, 'History': 90, 'Geography': 59}},
            'contact_info': {'Delhi': 'city', 'phone': '+918197792902'}
        },
        'student_9': {
            'personal_info': {'Rohit': 'name', 'age': 13, 'gender': 'Male'},
            'academic_info': {'D': 'class',
            'subjects': {'Math': 61, 'Science': 40, 'English': 87, 'History': 71, 'Geography': 65}},
            'contact_info': {'Mumbai': 'city', 'phone': '+919403306259'}
        },
        'student_10': {
            'personal_info': {'Sneha': 'name', 'age': 15, 'gender': 'Female'},
            'academic_info': {'C': 'class',
            'subjects': {'Math': 69, 'Science': 95, 'English': 59, 'History': 71, 'Geography': 79}},
            'contact_info': {'Chennai': 'city', 'phone': '+919028852657'}
        },
        'student_11': {
            'personal_info': {'Aarav': 'name', 'age': 16, 'gender': 'Male'},
            'academic_info': {'B': 'class',
            'subjects': {'Math': 55, 'Science': 62, 'English': 74, 'History': 68, 'Geography': 81}},
            'contact_info': {'Pune': 'city', 'phone': '+918675421308'}
        },
        'student_12': {
            'personal_info': {'Neha': 'name', 'age': 14, 'gender': 'Female'},
            'academic_info': {'A': 'class',
            'subjects': {'Math': 92, 'Science': 88, 'English': 69, 'History': 72, 'Geography': 85}},
            'contact_info': {'Delhi': 'city', 'phone': '+919824567123'}
        },
        'student_13': {
            'personal_info': {'Karan': 'name', 'age': 17, 'gender': 'Male'},
            'academic_info': {'C': 'class',
            'subjects': {'Math': 66, 'Science': 73, 'English': 58, 'History': 70, 'Geography': 91}},
            'contact_info': {'Mumbai': 'city', 'phone': '+917456321980'}
        },
        'student_14': {
            'personal_info': {'Ananya': 'name', 'age': 12, 'gender': 'Female'},
            'academic_info': {'E': 'class',
            'subjects': {'Math': 74, 'Science': 61, 'English': 88, 'History': 77, 'Geography': 63}},
            'contact_info': {'Chennai': 'city', 'phone': '+919764310985'}
        },
        'student_15': {
            'personal_info': {'Rohit': 'name', 'age': 15, 'gender': 'Male'},
            'academic_info': {'D': 'class',
            'subjects': {'Math': 85, 'Science': 67, 'English': 72, 'History': 91, 'Geography': 64}},
            'contact_info': {'Pune': 'city', 'phone': '+918913457620'}
        },
        'student_16': {
            'personal_info': {'Priya': 'name', 'age': 18, 'gender': 'Female'},
            'academic_info': {'A': 'class',
            'subjects': {'Math': 90, 'Science': 84, 'English': 79, 'History': 87, 'Geography': 92}},
            'contact_info': {'Delhi': 'city', 'phone': '+919887654320'}
        },
        'student_17': {
            'personal_info': {'Aarav': 'name', 'age': 20, 'gender': 'Male'},
            'academic_info': {'B': 'class',
            'subjects': {'Math': 77, 'Science': 68, 'English': 83, 'History': 80, 'Geography': 71}},
            'contact_info': {'Mumbai': 'city', 'phone': '+917654309821'}
        },
        'student_18': {
            'personal_info': {'Sneha': 'name', 'age': 19, 'gender': 'Female'},
            'academic_info': {'E': 'class',
            'subjects': {'Math': 64, 'Science': 72, 'English': 59, 'History': 85, 'Geography': 78}},
            'contact_info': {'Pune': 'city', 'phone': '+918901237654'}
        },
        'student_19': {
            'personal_info': {'Karan': 'name', 'age': 13, 'gender': 'Male'},
            'academic_info': {'C': 'class',
            'subjects': {'Math': 71, 'Science': 74, 'English': 62, 'History': 69, 'Geography': 73}},
            'contact_info': {'Chennai': 'city', 'phone': '+919823456781'}
        },
        'student_20': {
            'personal_info': {'Neha': 'name', 'age': 15, 'gender': 'Female'},
            'academic_info': {'A': 'class',
            'subjects': {'Math': 88, 'Science': 91, 'English': 75, 'History': 82, 'Geography': 79}},
            'contact_info': {'Delhi': 'city', 'phone': '+919765432187'}
        }
        }
    
    ans = correct_dictionary(students_data)
    print(ans)

if __name__ == "__main__":
    main()
