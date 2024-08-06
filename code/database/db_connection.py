from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
import json

def get_connection():
    """_summary_

    Returns:
        _type_: _description_
    """
    with open('code\database\credentials.json', 'r') as file:
        creds = json.load(file)

    dialect = creds.get('dialect')
    user = creds.get('user')
    passwd = creds.get('password')
    host = creds.get('host')
    port = creds.get('port')
    db = creds.get('database')

    url = f"{dialect}://{user}:{passwd}@{host}:{port}/{db}"
    try:
        engine = create_engine(url)
        print(f'Conected successfully to database {db}!')
        return engine
    except SQLAlchemyError as e:
        print(f'Error: {e}')

get_connection()