# Specifying the ODBC driver, server name, database, etc. directly

from Classwork.OOP_database import database_OOP
server = 'databases2.spartaglobal.academy'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

## OOP part
user_input = int(input("Please enter the number for the operation you want to execute:"
                       "\n 1. Fetch one row \n 2. Fetch many rows \n 3. Fetch All rows \n"))

data_oop = database_OOP(server, database, username, password)
oop_connection = data_oop.establishing_connection()
data_oop.execute_sql('SELECT * FROM Products', oop_connection, user_input)

# data_oop.execute_sql("'SELECT ProductId, ProductName FROM Products w'"