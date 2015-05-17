import os
import sqlalchemy

error = None
engine = None

# Connect to the database specified by the DATABASE_URL environment variable.
try:
    databse_url = sqlalchemy.engine.url.make_url(os.environ['DATABASE_URL'])
    if databse_url.drivername == 'postgresql':
        databse_url.drivername = 'postgresql+pg8000'
    engine = sqlalchemy.create_engine(databse_url)
    engine.connect()

# If anything went wrong with connection, store the error for later inspection.
except Exception as e:
    error = e


# Verify the configuration and connection by executing an actual query.
if __name__ == '__main__':
    if error:
        raise error
    result = engine.execute('select 1')
    assert result.first()[0] == 1
    print('Successfully connected to database.')
