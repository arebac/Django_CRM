import psycopg2

import psycopg2

# Connect to the default 'postgres' database
dataBase = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="Capstone",
    host="localhost",
    port="5432"
)

# Set the connection to autocommit mode
dataBase.autocommit = True

cursorObject = dataBase.cursor()

# Try to create the new database 'CRMbase'
try:
    cursorObject.execute("CREATE DATABASE CRMbase")
    print("All Done!")
except psycopg2.errors.DuplicateDatabase:
    print("Database 'CRMbase' already exists!")
