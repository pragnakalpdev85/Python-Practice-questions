from prettytable import PrettyTable # type: ignore

from .product import get_product_byname, update_product

def create_order(cursor: object, product_name: str, quantity: int) -> str:
    '''
    Created new customer order 
    
    Args:
        corsor (object): object of cursor for query execution
        product_name (str): name of the product
        quantity (int): quantity of the product
    Returns:
        str: success or failure messages 
    '''
    product = get_product_byname(cursor,product_name)
    
    if product:
        if product[3] >= quantity:
            cursor.execute(f"INSERT INTO orders(product_id, quantity) VALUES({product[0]}, {quantity});")
            update_product(cursor, product[1], product[2], product[3]- quantity)
            
            return f"Order of {quantity} {product_name} is placed."
        else:
            return f"Insufficient Stock of product {product[1]}"
    else:
        return f"There is no product with name {product_name}"
        
def daily_order_summary(cursor: object) -> str:
    '''
    Returns all order summary of current date
    
    Args:
        corsor (object): object of cursor for query execution
    Returns:
        str: order summary of current date
    '''
    cursor.execute(f"SELECT p.product_id, p.name, SUM(o.quantity), p.price FROM products p INNER JOIN orders o USING(product_id) WHERE o.order_date = CURRENT_DATE GROUP BY p.product_id;")
    
    data = cursor.fetchall()
    new_data = []
    for row in data:
        price = int(row[3])
        stock = float(row[2])

        t = tuple((row[1],row[2],row[3], price*stock))
        new_data.append(t)
    
    heading = ["Product", "Total Quantity", "Price", "Total revenue"]
    
    table = PrettyTable()
    
    table.field_names = heading
    table.add_rows(new_data)
    table.align = 'l'
    
    return table

def clear_old_orders(cursor: object) -> int:
    '''
    deletes all orders older than 30 days
    
    Args:
        corsor (object): object of cursor for query execution
    Returns:
        int: number of records deleted
    '''
    cursor.execute(f"DELETE FROM orders WHERE order_date < (select CURRENT_DATE - INTERVAL '30 day');")

    return cursor.rowcount
