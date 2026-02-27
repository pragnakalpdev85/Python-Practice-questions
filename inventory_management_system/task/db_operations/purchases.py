from prettytable import PrettyTable # type: ignore

from .product import get_product_byname
from .suppliers import get_supplier_byname

def purchase_products(cursor: object, product_name: str, supplier_name: str, quantity: int) -> str:
    '''
    Records purchases 
    
    Args:
        corsor (object): object of cursor for query execution
        product_name (str): name of the product
        supplier_name (str): name of the supplier
        quantity (int): quantity of the product
    Returns:
        str: success or failure messages 
    '''
    product = get_product_byname(cursor, product_name)
    supplier = get_supplier_byname(cursor, supplier_name)
    
    if product and supplier:
        cursor.execute(f"INSERT INTO purchases(product_id, supplier_id, quantity) VALUES({product[0]}, {supplier[0]}, {quantity});")
        cursor.execute(f"UPDATE products SET stock = {product[3] + quantity}  WHERE product_id = {product[0]};")
        return f"Purchase of product {product_name} is recorded"
    elif product:
        return f"There is no supplier with name {supplier_name}"
    elif supplier:
        return f"There is no product with name {product_name}"
    else:
        return f"There is no supplier with name {supplier_name} and no product with name {product_name}"
        
def purchase_summary(cursor: object) -> list:
    '''
    Retrieves all purchase summary from database
    
    Args:
        corsor (object): object of cursor for query execution
    Returns:
        list: all data of purchase grouped by supplier
    '''
    cursor.execute(f"SELECT s.supplier_id, s.name, COUNT(*) as supply_count, SUM(p.quantity) FROM purchases p INNER JOIN suppliers s USING(supplier_id) GROUP BY s.supplier_id;")
    
    data = cursor.fetchall()
    new_data = []
    for row in data:
        new_data.append(tuple((row[1],row[2],row[3])))
    
    heading = ["Supplier Name", "Supplies", "Total quantity"]
    
    table = PrettyTable()
    
    table.field_names = heading
    table.add_rows(new_data)
    table.align = 'l'
    
    return table