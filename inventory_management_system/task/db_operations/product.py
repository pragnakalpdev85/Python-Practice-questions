
def get_product_byname(cursor: object, name: str) -> tuple:
    '''
    find product with given name 
    
    Args:
        corsor (object): object of cursor for query execution
        name (str): name of the product
    Returns:
        tuple: tuple of product details
    '''
    cursor.execute(f" SELECT * FROM products WHERE name = '{name.lower()}';")
    
    return cursor.fetchone()


def add_product(cursor: object, name: str, price: int, stock: int) -> str:
    '''
    Addes new product to database
    
    Args:
        corsor (object): object of cursor for query execution
        name (str): name of the product
        price (int): price of the product
        stock (int): stock of the product
    Returns:
        str: success or failure messages 
    '''
    product_name = get_product_byname(cursor, name)
    
    if not product_name:
        cursor.execute(f"INSERT INTO products(name, price, stock) VALUES('{name.lower()}',{price},{stock}) ON CONFLICT(name) DO UPDATE SET price = EXCLUDED.price;")
        
        return f"Product {name} is added to inventory"
    else:
        return f"Product already exists with name {name}"

    
def update_product(cursor: object,name: str, price = None, stock = None) -> str:
    '''
    updates product 
    
    Args:
        corsor (object): object of cursor for query execution
        name (str): name of the product
        price (int): price of the product
        stock (int): stock of the product
    Returns:
        str: success or failure messages 
    '''
    product_name = get_product_byname(cursor, name)
    
    if product_name:
        if stock == None:
            cursor.execute(f"UPDATE products SET price = {price} WHERE name = '{name.lower()}';")
        elif price == None:
            cursor.execute(f"UPDATE products SET stock = {stock} WHERE name = '{name.lower()}';")
        else:
            cursor.execute(f"UPDATE products SET price = {price},stock = {stock} WHERE name = '{name.lower()}';")
        
        return f"Product {name.lower()} details are updated successfully"
    else:
        return f"There is no product with name {name}"