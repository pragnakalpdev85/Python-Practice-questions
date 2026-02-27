import psycopg2  # type: ignore
from psycopg2 import sql # type: ignore

from .env_variables import DB_NAME, DB_HOST, DB_PASSWORD, DB_PORT, DB_USER

def create_if_not_exists():
    ''' 
    Check if the database exists, if not than creates one
    '''
    
    #Astablish connection with preexisting deafult database postgress
    connect = psycopg2.connect(database = 'postgres',
                            user =  DB_USER,
                            password =  DB_PASSWORD,
                            host =  DB_HOST,
                            port =  DB_PORT)
    
    # needed for database creation and deletion operations
    connect.autocommit = True
    
    #creating cursor for exicuting query
    cur = connect.cursor()
    
    #checks database exists of not
    cur.execute(f"SELECT 1 FROM pg_database WHERE datname = '{DB_NAME}';")
    exists = cur.fetchone()
    
    #if database does not exist than creating one
    if not exists:
        query = f"CREATE DATABASE {DB_NAME};"
        cur.execute(query)
        print('database is created')
    else:
        print('database already exists')
        
    #closing connections
    cur.close()
    connect.close()

def connect_database():
    '''
    Astablish connection with the database
    '''
    
    #Astablish connection with database
    connection = psycopg2.connect(database = DB_NAME,
                            user =  DB_USER,
                            password =  DB_PASSWORD,
                            host =  DB_HOST,
                            port =  DB_PORT)
    print("connection in successful")
    
    connection.autocommit = True
    
    return connection
    
    