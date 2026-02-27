import psycopg2  # type: ignore
from psycopg2 import sql # type: ignore

from .env_variables import database_host,database_name,database_password,database_port,database_user

def create_if_not_exists():
    ''' 
    Check if the database exists, if not than creates one
    '''
    
    #Astablish connection with preexisting deafult database postgress
    connect = psycopg2.connect(database = 'postgres',
                            user =  database_user,
                            password =  database_password,
                            host =  database_host,
                            port =  database_port)
    
    # needed for database creation and deletion operations
    connect.autocommit = True
    
    #creating cursor for exicuting query
    cur = connect.cursor()
    
    db_name = database_name
    
    #checks database exists of not
    cur.execute(f"SELECT 1 FROM pg_database WHERE datname = '{db_name}';")
    exists = cur.fetchone()
    
    #if database does not exist than creating one
    if not exists:
        query = f"CREATE DATABASE {db_name};"
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
    connection = psycopg2.connect(database = database_name,
                            user =  database_user,
                            password =  database_password,
                            host =  database_host,
                            port =  database_port)
    print("connection in successful")
    
    connection.autocommit = True
    
    return connection
    
    