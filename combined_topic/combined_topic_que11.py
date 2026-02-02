# Question 11: Shopping Cart Calculator 
# Write a program that reads shopping cart data from a file where each line contains: item_name,quantity,price_per_unit,discount_percentage. Calculate subtotal, apply discounts, add tax (18%), and generate detailed bill with itemized breakdown.

# Rules:
# You can use file operations: open(), read(), write(), close()
# Must use loops, lists, dictionaries, and functions
# Create functions for calculations
# Handle edge cases (zero quantity, invalid discount)
# Write formatted bill to output file

# Test Cases:

# Test Case 1:
# Input: "Laptop,1,50000,10"
# Output:
# Item: Laptop
# Quantity: 1
# Price: 50000
# Discount (10%): -5000
# Subtotal: 45000
# Tax (18%): 8100
# Total: 53100

# Test Case 2:
# Input: "Mouse,2,500,5" and "Keyboard,1,1500,0"
# Output:
# Item: Mouse
# Quantity: 2
# Price: 1000
# Discount (5%): -50
# Subtotal: 950
# Item: Keyboard
# Quantity: 1
# Price: 1500
# Discount (0%): 0
# Subtotal: 1500
# Grand Total: 2450
# Tax (18%): 441
# Final Total: 2891

# Test Case 3:
# Input: "Book,3,200,15"
# Output:
# Item: Book
# Quantity: 3
# Price: 600
# Discount (15%): -90
# Subtotal: 510
# Tax (18%): 91.8
# Total: 601.8
import os

def read_line(line: str) -> list:
    '''
    reads each word of line

    Args:
        line (str): line of text
    Returns:
        list: returns list of words
    '''

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
        print(f"Invalid in input of product '{list_words[0]}' in file, Please enter valid data in input file.")
        return []
    
    # for words in list_words:
    if count_words == 0:
        return []
    
    return list_words

def validate_product_details(list_details: list) -> dict:
    '''
    validates product quantity price and discount

    Args:
        list_details (list): list of product name,quantity,price and discount
    Returns:
        dict: dictionary of product details
    '''
    try:
        product = {}

        if int(list_details[1]) < 0:
            print(f"Invalid quantity of product '{list_details[0]}' in file, quantity should be positive")
        elif float(list_details[2]) < 0:
            print(f"Invalid price of product '{list_details[0]}' in file, price should be positive")
        elif float(list_details[3]) < 0 or float(list_details[3]) > 100:
            print(f"Invalid discount of product '{list_details[0]}' in file, discount should be positive and between 0 to 100")
        else:
            product = {'name': list_details[0],'quantity': int(list_details[1]),"price": float(list_details[2]),'discount': float(list_details[3])}
    except ValueError as e:
        print("hii")
        print(f"Invalid in input of product '{list_details[0]}' in file, Please enter valid data in input file.")
        
    return product

def validate_filename_input(file_name: str) -> bool:
    '''
    validates file name input
    
    Args:
        name (str): name of the file
    returns:
        bool: file formate is correct or not
    '''
    #validating file formate
    flag = False
    check_word1 = ''

    for chars in file_name:
        if flag == True:
            check_word1 += chars
        if chars == '.':
            flag = True

    if check_word1 != 'txt':
        print("File formate is incorrect, Enter file name again")
        return False
    
    #file exist of not
    if not os.path.exists(file_name):
        print("File does not exist, Enter file name again")
        return False
    
    return True
    
def convert_data_to_dict(data: list) -> dict:
    '''
    read data and creat list of data
    
    Args:
        data (list): data from text file
    Returns:
        dict: dictionary of shopping cart products
    '''
    data_dict = {}

    index_count = 0
    for line in data:

        list_words = read_line(line)
        if list_words == []:
            continue
        #validating the product price, quantity and discount
        #and adding the product to data dictionary
        temp_dict = validate_product_details(list_words)
        if temp_dict != {}:
            data_dict[index_count] = temp_dict
            index_count += 1 

    return data_dict

def generate_bill(input_file_name: str, output_file_name: str) -> str:
    '''
    Generates detailed bill shopping cart data

    Args:
        input_file_name (str): name of the input file
        output_file_name (str): name of the output file
    Returns:
        str: generated bill of shopping cart
    '''
    try:
        #reading file data line by line
        with open(input_file_name, 'r') as file:
            data = file.readlines()
            if data == []:
                return "There is no content in file"
            
        data_dict = convert_data_to_dict(data)
        if data_dict == {}:
            return 
        
        output = ''
        grand_total = 0
        count_products = 0
        #calculating total bill with taxes
        for product in data_dict:
            temp_dict = data_dict[product]

            price = temp_dict['quantity']*temp_dict['price']
            output += f"Item: {temp_dict['name']}\nQuantity: {temp_dict['quantity']}\nPrice: {price}\n"

            discount = price*(temp_dict['discount']/100)
            if discount == 0:
                output += f"Discount ({temp_dict['discount']}%): {discount}\n"
            else:
                output += f"Discount ({temp_dict['discount']}%): -{discount}\n"

            subtotal = price-discount
            grand_total += subtotal
            output += f"Subtotal: {subtotal}\n"
            count_products += 1
        
        #adding total bill and final total with taxes in output
        
        output += f"Grand Total: {grand_total}\n" if count_products != 1 else ""
        output += f"Tax (18%): {grand_total*(0.18)}\n"
        output += f"Final Total: {grand_total + grand_total*(0.18)}"

        #writing output in file
        with open(output_file_name,'w') as file:
            file.write(output)

        return output
    
    except FileNotFoundError as e:
        print("File Not Found or the given file name is incorrect, It should be a text file.")
    except OSError as e:
        print("Given File name is not defined")
    except TypeError as e:
        print("Invalid input data. Please enter valid data types in input file.")
    except ValueError as e:
        print("Invalid content structure in input file, Please enter valid data in input file.")

#defining main function
def main():
    try:
        input_file_name = ''
        output_file_name = ''

        flag = False
        while flag == False:
            input_file_name = input("Enter input file name: ")
            flag = validate_filename_input(input_file_name)

        flag = False
        while flag == False:
            output_file_name = input("Enter input file name: ")
            flag = validate_filename_input(output_file_name)

        ans = generate_bill(input_file_name, output_file_name)
        print(ans)
        
    except FileNotFoundError as e:
        print("File Not Found.")
    except OSError as e:
        print("Given File name is not defined.")

if __name__ == "__main__":
    main()