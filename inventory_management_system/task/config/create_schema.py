import psycopg2   # type: ignore

def create_schema(connection: object):
    '''
    Created whole schema of the inventory management system
    
    Args:
        connection (object): object of the database connection 
    '''
    #creating cursor for query execution
    cursor = connection.cursor()

    #creating products table
    cursor.execute('CREATE TABLE IF NOT EXISTS products(product_id  SERIAL PRIMARY KEY, name TEXT UNIQUE NOT NULL, price NUMERIC(10,2), stock INT);')

    #creating suppliers table
    cursor.execute('CREATE TABLE IF NOT EXISTS suppliers(supplier_id SERIAL PRIMARY KEY, name TEXT UNIQUE NOT NULL, contact_email TEXT);')

    #creating purchases table
    cursor.execute('CREATE TABLE IF NOT EXISTS purchases(purchase_id SERIAL PRIMARY KEY, supplier_id INT, product_id INT, quantity INT, purchase_date DATE DEFAULT CURRENT_DATE, CONSTRAINT fk_supplier FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON DELETE CASCADE,CONSTRAINT fk_product FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE);')

    #creating orders table
    cursor.execute('CREATE TABLE IF NOT EXISTS orders(order_id SERIAL PRIMARY KEY, product_id INT, quantity INT, order_date DATE DEFAULT CURRENT_DATE, CONSTRAINT fk_product FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE);')
    
    print("schema created successfully")
    