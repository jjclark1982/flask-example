import os
from sqlalchemy import create_engine

engine = create_engine(os.environ['DATABASE'])

if __name__ == '__main__':
    result = engine.execute('select 1')
    if result.first()[0] == 1:
        print("Successfully connected to database.")
    else:
        raise Exception("something went wrong")
