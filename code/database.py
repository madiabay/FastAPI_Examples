import sqlalchemy
import databases

DATABASE_URL = "postgresql://postgres:postgres@localhost:1234/postgres"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
