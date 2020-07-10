import pyodbc
#What - we are trying to establish a connection and read data from the database in the python console

#pyodbc - python library helps to connect to the database
#why - helps us to showcase data in the console, which would display in real time on the front end.

#ODBC connection - open database connectivity - API used for connecting to microsoft applications

server = 'databases2.spartaglobal.academy'
#databases2.spartaglobal.academy
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
connections = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE=' + database +';UID='+ username +';PWD='+ password)
cursor = connections.cursor()
print(connections)
print(cursor)

prodquery_result = cursor.execute('SELECT * FROM Products')
print("Printing query_result object:", prodquery_result)

#fetchone row - fetchone(), fetch many rows - fetchmany(), fetch all rows - fetchall()
rows = prodquery_result.fetchone()
print(type(rows))
print(rows[1]) #Second column of rows - columns start from 0th index
print(rows.ProductName)

rows = prodquery_result.fetchone() #maintaining its state.
print(type(rows))
print(rows[1]) #Second column of rows - columns start from 0th index
print(rows.ProductName)

rows = prodquery_result.fetchmany(30)
for row in rows:
        print(row)

rows = prodquery_result.fetchall()
for row in rows:
        print(row)

