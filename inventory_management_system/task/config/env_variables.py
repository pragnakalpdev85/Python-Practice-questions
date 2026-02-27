import os
from dotenv import load_dotenv  # type: ignore

load_dotenv()

database_name = os.getenv('DB_NAME')
database_user = os.getenv("DB_USER")
database_password = os.getenv("DB_PASS")
database_host = os.getenv("DB_HOST")
database_port =  os.getenv("DB_PORT")