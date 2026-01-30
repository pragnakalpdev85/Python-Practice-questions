# Question 9: Inventory Management System 
# Write a program that manages product inventory stored in a file. Each line contains: product_id,name,quantity,price. Implement functions to: add product, update quantity, search by name/id, calculate total inventory value, and generate low stock report (quantity < 10).

# Rules:
# You can use file operations: open(), read(), write(), close()
# Must use loops, dictionaries, lists, conditionals, and functions
# Create separate functions for each operation
# Handle edge cases (duplicate IDs, invalid quantities)         
# Write reports to output file

# Test Cases:

# Test Case 1:
# Operation: Add product "101,Laptop,5,50000"
# Output: Product added successfully

# Test Case 2:
# Operation: Update quantity "101" to 15
# Output: Quantity updated. New stock: 15

# Test Case 3:
# Operation: Generate low stock report
# Output:
# Low Stock Products:
# 101,Laptop,5,50000
# Total Inventory Value: 250000

def string_to_lower_case(data: str) -> str:
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

def read_file(file_name: str) -> dict:
    '''
    read data and creat list of data
    
    Args:
        file_name (str): name of the input file
    Returns:
        list: list of tuples with name and marks
    '''
    data_dict = {}

    #validating file format
    flag = False
    check_word1 = ''
    for chars in file_name:
        if flag == True:
            check_word1 += chars
        if chars == '.':
            flag = True
    
    if check_word1 != 'txt':
            raise FileNotFoundError()

    with open(file_name, 'r') as file:

        for lines in file:
            line = string_to_lower_case(lines)
            data_size = 0
            #calculating length of the line
            for char in line:
                data_size += 1

            index = 0
            word = ''
            list_words = []
            count_words = 0
            for chars in line:
                #add all words in the list
                if chars == ',' or chars == '\n' or index == data_size-1:
                    if index == data_size-1 and chars != " " and chars != "\n":
                        word += chars
                
                    if word != '':
                        list_words += [word,]
                        count_words += 1
                        word = ''
                else:
                    if chars != " ":
                        word += chars
                index += 1

            #check the line has 4 word if not than data is incomplete
            if count_words != 4 and count_words != 0:
                raise ValueError()
            
            # for words in list_words:
            if count_words == 0:
                continue

            #adding product details in data dictionary
            if int(list_words[0]) > 0 and int(list_words[2]) >= 0 and float(list_words[3]) >= 0:
                data_dict[int(list_words[0])] = {'name': list_words[1],'quantity': int(list_words[2]),"price": float(list_words[3])}
            else:
                print(f"product {list_words[1]} has invalid data. Please enter valid data in file.")
        
        return data_dict

def write_file(file_name: str, data_dict: dict) :
    '''
    write given data intu file
    
    Args:
        file_name (str): name of the file to write data
        data_dict (dict): dictionary of data
    Returns:
        None
    '''
    output = ''
    index = 1
    #writing all data into text file
    for data in data_dict:
        if index == 1:
            output += f"{data},{data_dict[data]['name']},{data_dict[data]['quantity']},{data_dict[data]['price']}"
        else:
            output += f"\n{data},{data_dict[data]['name']},{data_dict[data]['quantity']},{data_dict[data]['price']}"
        index += 1

    with open(file_name,'w') as file:
        file.write(output)

def add_product(file_name: str, id: int, name: str, quantity: int, price: float) -> str:
    '''
    addes new product
    
    Args:
        file_name (str): name of the input file
        id (int): id of the product
        name (str): name of the student
        quantity (int): quantity of the product
        price (float): price of the product 
    Returns:
        str: success message
    '''
    data_dict = read_file(file_name)
    if quantity < 0 or price < 0 or id <= 0:
        return f"product {name} has invalid data. Please enter valid data."
    
    
    #adding product details in data dictionary
    for ids in data_dict:
        if id == ids:
            return f"Product with Id {id} already exist in inventory. Enter a different Id for new product."
    data_dict[id] = {'name': name,'quantity': quantity,"price": price}

    write_file(file_name, data_dict)

    return "Product added successfully"

def update_quantity(file_name: str, id: int, quantity: int) -> str:
    '''
    updates quantity of the given product id

    Args:
        file_name (str): name of the input file
        id (int): id of the product
        quantity (int): new quantity of the product
    Returns:
        str: success message
    '''

    if quantity < 0:
        return "Quantity value is invalid. quantity should be greater or equal to zero."
    
    data_dict = read_file(file_name)
    if data_dict == {}:
        return "There is no content in file."
    
    try:
        #return output if key exists
        data_dict[int(id)]['quantity'] = quantity
        write_file(file_name, data_dict)

        return f"Quantity updated. New stock: {quantity}" 
    
    except KeyError as e:
        print(f"There is no product with id {id}")
    
def search_by_name(file_name: str, name: str) -> str:
    '''
    search product with given name

    Args:
        file_name (str): name of the input file
        name (str): name of the product
    Returns:
        str: returns product details
    '''
    output = ''
    data_dict = read_file(file_name)
    if data_dict == {}:
        return "There is no content in file."
    
    #searching name in the data dictionary
    name = string_to_lower_case(name)
    for id in data_dict:
        if data_dict[id]['name'] == name:
            output += f"id: {id}, name: {data_dict[id]['name']}, "
            output += f"quantity: {data_dict[id]['quantity']}, price: {data_dict[id]['price']}\n"
    
    if output != '':
        return f'Products with name {name}:\n'+ output
    else:
        return f"There is no product with name {name}"
    
def search_by_id(file_name: str, id: int) -> str:
    '''
    search product with given name

    Args:
        file_name (str): name of the input file
        id (int): id of the product
    Returns:
        str: returns product details
    '''
    data_dict = read_file(file_name)
    if data_dict == {}:
        return "There is no content in file."
    id = int(id)
    try:
        #return output if key exists
        output = f'Product with id {id}:\n'
        output += f"id: {id}, name: {data_dict[id]['name']}, "
        output += f"quantity: {data_dict[id]['quantity']}, price: {data_dict[id]['price']}"
        return output
    except KeyError as e:
        print(f"There is no product with id {id}")

def total_inventory_value(file_name: str) -> float:
    '''
    calculate total value of all products in inventory

    Args:
        file_name (str): name of the input file
    Returns:
        float: returns total value of inventory
    '''
    data_dict = read_file(file_name)
    if data_dict == {}:
        return "There is no content in file."
    
    #calculating total value of inventory
    total_value = 0
    for id in data_dict:
        total_value += float(data_dict[id]['price'])*float(data_dict[id]['quantity'])

    return f"Total Inventory Value: {total_value}"

def low_stock_report(file_name: str) -> str:
    '''
    finds all products with stock less than 10 in inventory

    Args:
        file_name (str): name of the input file
    Returns:
        str: returns products with stock less than 10 
    '''
    data_dict = read_file(file_name)
    if data_dict == {}:
        return "There is no content in file."
    
    output = ''
    for id in data_dict:
        if int(data_dict[id]['quantity']) < 10:
            output += f"id: {id}, name: {data_dict[id]['name']}, "
            output += f"quantity: {data_dict[id]['quantity']}, price: {data_dict[id]['price']}\n"
    
    if output != '':
        return f"Low Stock Products:\n" + output + total_inventory_value(file_name)
    else:
        return "Quantity of all products is more than 10.\n" + total_inventory_value(file_name)
    
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
        print("Enter number from 1 to 6 to perform following operation:")
        print("1. Add Product.")
        print("2. Update quantity.")
        print("3. Search product by Name.")
        print("4. Search product by Id.")
        print("5. Get Total inventory value.")
        print("6. Get Low stock report.")

        operation_num = int(input("Enter number to perform operation: "))

        match operation_num:
            case 1:
                id = int(input("Enter Product id: "))
                name = input("Enter Product name: ")
                quantity = int(input("Enter Product quantity: "))
                price = float(input("Enter Product price: "))

                ans =  add_product(input_file_name,id,name,quantity,price)
                print(ans)
            case 2:
                id = int(input("Enter product Id: "))
                quantity = int(input("Enter enter quantity: "))
                ans  = update_quantity(input_file_name, id, quantity)
                print(ans)
            case 3:
                name = input("Enter name of the product:")
                ans = search_by_name(input_file_name, name)
                print(ans)
            case 4:
                id = int(input("Enter Id of the product: "))
                ans =  search_by_id(input_file_name,id)
                print(ans)
            case 5:
                ans = total_inventory_value(input_file_name)
                print(ans)
            case 6:
                ans = low_stock_report(input_file_name)
                print(ans)
            case _:
                print("Enter valid number between 1 to 6 for operation.")
    except FileNotFoundError as e:
        print("File Not Found or the given file name is incorrect, It should be a text file.")
    except OSError as e:
        print("Given File name is not defined")
    except TypeError as e:
        print("Invalid input data. Please enter valid data types in input.")
    except ValueError as e:
        print("Invalid content structure in input, Please enter valid data in input.")

if __name__ == "__main__":
    main()
