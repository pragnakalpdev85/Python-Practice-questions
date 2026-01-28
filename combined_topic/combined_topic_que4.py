# Question 4: Contact Book Manager 
# Write a program that manages a contact book stored in a file. Each line in the file contains: name:phone:email. Implement functions to: add contact, search by name, delete contact, and display all contacts.

# Rules:
# You can use file operations: open(), read(), write(), close()
# Must use loops, conditionals, strings, and lists
# Create separate functions for each operation
# Handle edge cases (duplicate names, contact not found)
# Proper error handling required

# Test Cases:
# Test Case 1:
# Operation: Add contact "John:1234567890:john@email.com"
# Output: Contact added successfully

# Test Case 2:
# Operation: Search "John"
# Output: Name: John, Phone: 1234567890, Email: john@email.com

# Test Case 3:
# Operation: Delete "John"
# Output: Contact deleted successfully

def to_lower_case(data: str) -> str:
    '''
    converts string into lowercase

    Args:
        data (str): data to be converted into lowercase
    Returns:
        str: converted data 
    '''

    name_size = 0
    for char in data:
        name_size += 1

    upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_alpha = "abcdefghijklmnopqrstuvwxyz"

    index = 0
    lower_data = ''
    #manually converting upercase to lower case
    while index < name_size:
        character = data[index]

        if character == " ":
            index += 1
            continue

        #converting uppercase to lower case
        if data[index] >= "A" and data[index] <= "Z":
            index2 = 0
            for j in upper_alpha:
                if(data[index] == j):
                    break
                index2 += 1
            character = lower_alpha[index2]
            lower_data += character
        else:
            lower_data += character
        index += 1

    return lower_data
    
def data_to_dict(file_data: str) -> dict:
    '''
    converts data from input file to dictionary.

    Args:
        file_data (str): input data from file
    Returns:
        dict: dictionary of persons contacts
    '''
    try: 
        ans_dict = {}
        data_size = 0
        for char in file_data:
            data_size += 1

        file_data = to_lower_case(file_data)

        list_words = []

        index = 0
        word = ''
        for chars in file_data:
            #add all words in the list
            if chars == ':' or chars == '\n' or index == data_size-1:
                if index == data_size-1:
                    word += chars
            
                if word != '':
                    list_words += [word,]
                    word = ''
            else:
                word += chars
            index += 1

        index_count = 0
        temp_dict = {}
        
        contact_count = 1
        #puting all words in answer dictionary
        for element in list_words:
            if index_count == 0:
                temp_dict['name'] = element
                person = element
            elif index_count == 1:
                temp_dict['phone'] = element
            elif index_count == 2:
                temp_dict['email'] = element
                ans_dict[contact_count] = temp_dict
                temp_dict = {}
                contact_count += 1
        
            index_count = (index_count+1)%3

        return ans_dict
    except KeyError as e:
        print("Input data in file is incomplete,",e)

def display_contacts(file_name: str) -> str:
    '''
    returns all contacts in file

    Args:
        file_name (str): name of the input file
    Returns: 
        returns all contacts as string
    '''
    try:
        data =  read_file(file_name)
        if data == '':
            return "There is no content in file."
        contact_dict = data_to_dict(data)

        output = 'All Contacts:'
        #adding all contacts to output string
        for key in contact_dict:
            output += f"\nName: {contact_dict[key]['name']}, Phone: {contact_dict[key]['phone']}, Email: {contact_dict[key]['email']}"

        return output
    except KeyError as e:
        print("Input data in file is incomplete,",e)

def add_contact(file_name: str, new_contact: str) -> dict:
    '''
    add new contact to the file

    Args:
        file_name (str): name of the input file
        new_contact (str): new contact
    return:
        str: msg for successfull update 
    '''
    try:
        data =  read_file(file_name)
        contact_dict = data_to_dict(data)

        lower = to_lower_case(new_contact)
        new_dict = data_to_dict(lower)

        print(new_dict)
        present = False
        size_dict = 0
        for key in contact_dict:
            if contact_dict[key] == new_dict[1]:
                present = True
            size_dict += 1
            
        if present != True:
            contact_dict[size_dict+1] = new_dict[1]
            write_file(file_name, contact_dict)
            return "Contact added successfully"
        else:
            return "Contact already exists."
        
    except KeyError as e:
        print("Input data in data is incomplete,",e)

def search_contact(file_name: str, name: str) -> str:
    '''
    search contact from name

    Args:
        file_name (str): name of the input file
        name (str): name of the contact
    Returns:
        str: contact with given name
    
    '''
    data = read_file(file_name)
    if data == '':
        return "There is no content in file."
    contact_dict = data_to_dict(data)

    #converting name to lower case
    lower_name = to_lower_case(name)
    
    #finding name and returning contact
    for key in contact_dict:
        temp_dict = contact_dict[key]
        if temp_dict['name'] == lower_name:
            return f"Name: {temp_dict['name']}, Phone: {temp_dict['phone']}, Email: {temp_dict['email']}"
    
    return f"There no Contact with name {name}"

def delete_contact(file_name: str, name: str) -> dict:
    '''
    add new contact to the file

    Args:
        file_name (str): name of the external file
        name (str): name of the contact
        
    return:
        dict: contact dictionary with new contact 
    '''
    try:
        data = read_file(file_name)
        if data == '':
            return "There is no content in file."
        contact_dict = data_to_dict(data)

        name =  to_lower_case(name)
        ans_dict = {}
        
        #deleting contact with given name 
        #adding all contacts except the contact with given name
        flag = False
        for key in contact_dict:
            temp_dict = contact_dict[key]
            if temp_dict['name'] == name:
                flag =  True
                continue
            ans_dict[key] = contact_dict[key]

        if flag == False:
            return f"There no Contact with name {name}"
        else:
            write_file(file_name, ans_dict)
            return "Contact deleted successfully"
    
    except KeyError as e:
        print("Input data in data is incomplete,",e)

def read_file(file_name: str) -> str:
    try:   
        with open(file_name,'r') as file:
            data = file.read()
        
        return data
    except FileNotFoundError as e:
        print("File Not Found: ",e)
    except OSError as e:
        print("Given File name is not defined: ",e)

def write_file(file_name: str, contact_dict: dict):
    try: 
        data = ''
        index = 0
        for keys in contact_dict:
            if index == 0:
                data += f"{contact_dict[keys]['name']}:{contact_dict[keys]['phone']}:{contact_dict[keys]['email']}"
            else:
                data += f"\n{contact_dict[keys]['name']}:{contact_dict[keys]['phone']}:{contact_dict[keys]['email']}"
            index += 1

        with open(file_name,'w') as file:
            file.write(data)
        
    except FileNotFoundError as e:
        print("File Not Found: ",e)
    except OSError as e:
        print("Given File name is not defined: ",e)


def main():
    try:
        flag = False
        while flag == False:
            input_file_name = input("Enter input file name: ")
            try:
                with open(input_file_name,'r') as f:
                    flag = True
            except FileNotFoundError:
                print("File not found Enter name again")
        print("Enter number from 1 to 4 to perform following operation:")
        print("1. Display all contacts.")
        print("2. Search contact by name.")
        print("3. Add contact.")
        print("4. Delete contact.")

        operation_num = int(input("Enter number to perform operation: "))

        match operation_num:
            case 1:
                ans =  display_contacts(input_file_name)
                print(ans)
            case 2:
                name = input("Enter name of contact: ")
                ans  = search_contact(input_file_name, name)
                print(ans)
            case 3:
                contact = input("Enter contact:")
                ans = add_contact(input_file_name, contact)
                print(ans)
            case 4:
                name = input("Enter name of contact: ")
                ans =  delete_contact(input_file_name,name)
                print(ans)
            case _:
                print("Enter valid number between 1 to 4 for operation.")

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
