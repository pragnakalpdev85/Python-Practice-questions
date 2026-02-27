import logging
import re

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

def choice() -> int:
    '''
    Takes user input choice of the user
    
    Returns:
        Int: Number of operation
    '''
    while True:
        try:
            choice = int(input("Enter your choice (1 to 10): "))
            
            if choice > 10 or choice < 1:
                raise Exception()
            
            return choice
        
        except:
            print("Invalid Choice enter your choice between 1 to 10.")
            
def quantity_input_validation() -> int:
    '''
    Validated quantity input
    
    Returns:
        int: returns quantity
    ''' 
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            
            if quantity < 1:
                raise Exception()
            
            return quantity
        
        except:
            print("Invalid Quantity, Quantity Should be greater than 0.")

def price_input_validation() -> float:
    '''
    Validated price input
    
    Returns:
        float: returns price
    ''' 
    while True:
        try:
            price = int(input("Enter price: "))
            
            if price < 1:
                raise Exception()
            
            return price
        
        except:
            print("Invalid price, price Should be greater than 0.")
            
def stock_input_validation() -> int:
    '''
    Validated stock input
    
    Returns:
        int: returns stock
    ''' 
    while True:
        try:
            quantity = int(input("Enter stock: "))
            
            if quantity < 0:
                raise Exception()
            
            return quantity
        
        except:
            print("Invalid stock, stock Should be greater or equal to 0.")
 
def name_input_validation(title) -> str:
    '''
    validated input name
    
    Returns:
        name: name of product or supplier
    '''
    while True:
        name = input(f"Enter {title} Name: ")
        name = name.strip()
        
        if name == '':
            print("Invalid name Enter Again.")
            continue
        
        return name

def validate_email() -> str:
    '''
    validated email input
    
    Returns:
        str: varified email
    '''
    while True:
        email = input("Enter email of supplier: ")
        check = re.fullmatch(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
        if email == '' or check == None:
            print("Invalid email, Enter email again.")
            continue
        
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
            operation = choice()
            
            try:
                match operation:
                    case 1:
                        print('==============================================')
                        name = name_input_validation('product')
                        price = price_input_validation()
                        stock = stock_input_validation()
                        
                        ans = add_product(cursor, name, price, stock)
                        print(ans)
                        
                    case 2:
                        print('==============================================')
                        name = name_input_validation('product')
                        price = price_input_validation()
                        
                        ans = update_product(cursor, name, price, stock = None)
                        print(ans)
                        
                    case 3:
                        print('==============================================')
                        name = name_input_validation('product')
                        stock = stock_input_validation()
                        
                        ans = update_product(cursor, name, None, stock)
                        print(ans)
                        
                    case 4:
                        print('==============================================')
                        name = name_input_validation('Supplier')
                        email = validate_email()
                        
                        ans = add_supplier(cursor, name, email)
                        print(ans)
                        
                    case 5:
                        print('==============================================')
                        product_name = name_input_validation('product')
                        supplier_name = name_input_validation('supplier')
                        quantity = quantity_input_validation()
                        
                        ans = purchase_products(cursor, product_name, supplier_name, quantity)
                        print(ans)
                        
                    case 6:
                        print('==============================================')
                        name = name_input_validation('product')
                        quantity = quantity_input_validation()
                        
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
                    
            except Exception as err:
                logging.exception(err)
                    
        connection.close()
        
    except Exception as err:
        print("Database Connection Error")
        logging.exception(err)
   
    
if __name__ == '__main__':
    main()
