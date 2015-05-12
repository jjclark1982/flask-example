import os
import sqlalchemy

databse_url = sqlalchemy.engine.url.make_url(os.environ.get("DATABASE_URL"))
databse_url.drivername = 'postgresql+pypostgresql'
engine = sqlalchemy.create_engine(databse_url)

if __name__ == '__main__':
    result = engine.execute('select 1')
    if result.first()[0] == 1:
        print("Successfully connected to database.")
    else:
        raise Exception("something went wrong")
