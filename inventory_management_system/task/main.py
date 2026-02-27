import logging
import re
from typing import Optional, Union

from config.db_config import create_if_not_exists, connect_database
from config.create_schema import create_schema
from db_operations.product import add_product, update_product
from db_operations.suppliers import add_supplier
from db_operations.purchases import purchase_products, purchase_summary
from db_operations.orders import create_order, daily_order_summary, clear_old_orders

logging.basicConfig(
    filename='db_errors.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def validate(func) -> Optional[Union[int, float, str]]:
    
    index = 0
    while index < 3:
        value = func()
        
        if value != None:
            return value
        index += 1
        
    return None

def choice() -> Union[int,str]:
    '''
    Takes user input choice of the user
    
    Returns:
        Int: Number of operation
    ''' 
    user_choice = input("Enter your choice (1 to 10): ")
    if user_choice.isdigit() and int(user_choice) < 11 and int(user_choice) > 0:
        return int(user_choice)
    else:
        print("Invalid choice, Enter choice between 1 to 10.")
        return None  
            
def quantity_input_validation() -> Optional[int]:
    '''
    Validated quantity input
    
    Returns:
        int: returns quantity
    '''     
    quantity = input("Enter quantity: ")
    if quantity.isdigit() and quantity > '0':
        return int(quantity)
    else:
        print("Invalid Quantity, Quantity Should be greater than 0.")
        return None

def price_input_validation() -> Optional[float]:
    '''
    Validated price input
    
    Returns:
        float: returns price
    '''     
    price = input("Enter price: ")
    if price.isdigit() and price > '0':
        return float(price)
    else:
        print("Invalid price, price Should be greater than 0.")
        return None
            
def stock_input_validation() -> Optional[int]:
    '''
    Validated stock input
    
    Returns:
        int: returns stock
    ''' 
    
    stock = input("Enter stock: ")
    if stock.isdigit() and stock >= '0':
        return int(stock)
    else:
        print("Invalid stock, stock Should be greater or equal to 0.")
        return None

def product_name_input_validation() -> Optional[str]:
    '''
    validated input name
    
    Returns:
        name: name of product or supplier
    '''
    name = input(f"Enter product Name: ")
    name = name.strip()
    
    if name == '':
        print("Invalid name Enter Again.")
        return None
    else:
        return name
 
def supplier_name_input_validation() -> Optional[str]:
    '''
    validated input name
    
    Returns:
        name: name of Supplier or supplier
    '''
    name = input(f"Enter Supplier Name: ")
    name = name.strip()
    
    if name == '':
        print("Invalid name Enter Again.")
        return None
    else:
        return name

def validate_email() -> Optional[str]:
    '''
    validated email input
    
    Returns:
        str: varified email
    '''
    email = input("Enter email of supplier: ")
    check = re.fullmatch(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
    if email == '' or check == None:
        print("Invalid email, Enter email again.")
        return None
    else:
        return email

def main():
    try: 
        create_if_not_exists()
        connection = connect_database()
        create_schema(connection)
        
        cursor = connection.cursor()
        
        while True:
            print('==============================================')
            print('1. Add New Product.')
            print('2. Update Product price.')
            print('3. Update Product stock.')
            print('4. Add New Supplier.')
            print('5. Record Inventory Purchases.')
            print('6. Create Customer Orders.')
            print('7. Todays Order Summary.')
            print('8. Purchase Summary.')
            print('9. Clean Up Old Orders.')
            print('10. Exit.')
            operation = validate(choice)
            
            try:
                match operation:
                    case 1:
                        print('==============================================')
                        name = validate(product_name_input_validation)
                        if name == None:            
                            print("You have entered invalid product name Three times.\nOperation will be closed.")
                            continue
                        
                        price = validate(price_input_validation)
                        if price == None:            
                            print("You have entered invalid price Three times.\nOperation will be closed. ")
                            continue
                        
                        stock = validate(stock_input_validation)
                        if stock == None:            
                            print("You have entered invalid stock Three times.\nOperation will be closed.")
                            continue
                        
                        ans = add_product(cursor, name, price, stock)
                        print(ans)
                        
                    case 2:
                        print('==============================================')
                        name = validate(product_name_input_validation)
                        if name == None:            
                            print("You have entered invalid product name Three times.\nOperation will be closed. ")
                            continue
                        
                        price = validate(price_input_validation)
                        if price == None:            
                            print("You have entered invalid price Three times.\nOperation will be closed . ")
                            continue
                        
                        ans = update_product(cursor, name, price, stock = None)
                        print(ans)
                        
                    case 3:
                        print('==============================================')
                        name = validate(product_name_input_validation)
                        if name == None:            
                            print("You have entered invalid product name Three times.\nOperation will be closed. ")
                            continue
                        
                        stock = validate(stock_input_validation)
                        if stock == None:            
                            print("You have entered invalid stock Three times.\nOperation will be closed. ")
                            continue
                        
                        ans = update_product(cursor, name, None, stock)
                        print(ans)
                        
                    case 4:
                        print('==============================================')
                        name = validate(supplier_name_input_validation)
                        if name == None:            
                            print("You have entered invalid supplier name Three times.\nOperation will be closed.")
                            continue
                        
                        email = validate(validate_email)
                        if email == None:            
                            print("You have entered invalid email Three times.\nOperation will be closed. ")
                            continue
                        
                        ans = add_supplier(cursor, name, email)
                        print(ans)
                        
                    case 5:
                        print('==============================================')
                        product_name = validate(product_name_input_validation)
                        if product_name == None:            
                            print("You have entered invalid product name Three times.\nOperation will be closed.")
                            continue
                        
                        supplier_name = validate(supplier_name_input_validation)
                        if supplier_name == None:            
                            print("You have entered invalid supplier name Three times.\nOperation will be closed. ")
                            continue
                        
                        quantity = validate(quantity_input_validation)
                        if quantity == None:            
                            print("You have entered invalid quantity Three times.\nOperation will be closed. ")
                            continue
                        
                        ans = purchase_products(cursor, product_name, supplier_name, quantity)
                        print(ans)
                        
                    case 6:
                        print('==============================================')
                        name = validate(product_name_input_validation)
                        if name == None:            
                            print("You have entered invalid product name Three times.\nOperation will be closed. ")
                            continue
                        
                        quantity = validate(quantity_input_validation)
                        if quantity == None:            
                            print("You have entered invalid quantity Three times.\nOperation will be closed. ")
                            continue
                        
                        ans = create_order(cursor, name, quantity)
                        print(ans)
                        
                    case 7:
                        print('==============================================')
                        ans = daily_order_summary(cursor)
                        print(ans)
                        
                    case 8:
                        print('==============================================')
                        ans = purchase_summary(cursor)
                        print(ans)
                    case 9:
                        print('==============================================')
                        ans = clear_old_orders(cursor)
                        print(ans," Records are deleted.")
                        
                    case 10:
                        print('==============================================')
                        break
                    
                    case _:
                        if operation == None:
                            print('You have entered wrong choices Three times.')
                        break
                    
            except Exception as err:
                logging.exception(err)
        connection.close()
        
    except Exception as err:
        print("Database Connection Error")
        logging.exception(err)
    
if __name__ == '__main__':
    main()
