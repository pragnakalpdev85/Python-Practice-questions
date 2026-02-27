
def get_supplier_byname(cursor: object, name: str) -> tuple:
    '''
    Retrieves supplier from database by name
    
    Args:
        corsor (object): object of cursor for query execution
        name (str): name of the supplier
    Returns:
        tuple: tuple of supplier data 
    '''

    cursor.execute(f"SELECT supplier_id,name FROM suppliers WHERE name = '{name.lower()}';")
    
    return cursor.fetchone()

def add_supplier(cursor: object, name: str, mail = None) -> str:
    '''
    Addes new supplier to database
    
    Args:
        corsor (object): object of cursor for query execution
        name (str): name of the supplier
        mail (int): email of the supplier
    Returns:
        str: success or failure messages 
    '''
    cursor.execute(f"SELECT name from suppliers WHERE name = '{name.lower()}';")
    supplier = cursor.fetchone()
    
    cursor.execute(f"SELECT * FROM suppliers WHERE contact_email = '{mail}';")
    email = cursor.fetchone()

    if supplier:
        return f'Supplier Already exists with name {name}'
    elif email:
        return f'Supplier with email {mail} already exists.'
    else:
        if mail == None:
            mail = 'null'
            cursor.execute(f"INSERT INTO suppliers(name, contact_email) VALUES('{name.lower()}', {mail});")
        else: 
            cursor.execute(f"INSERT INTO suppliers(name, contact_email) VALUES('{name.lower()}', '{mail}');")
            
        return f"New suppier is added"