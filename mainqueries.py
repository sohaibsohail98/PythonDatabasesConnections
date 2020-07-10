import pyodbc

from OOP_connection import Connection

class Queries:

    def fetch_information(self):

        user_input = int(input("Please enter the number for the operation you want to execute:"
                                   "\n 1. Fetch one row \n 2. Fetch many rows \n 3. Fetch All rows \n 4. Average Unit Price\n"))
        x = [1,2,3,4]
        if user_input not in x:
                print("Sorry you entered the wrong input")
        else:
            if user_input == 1:
                self.city_name()
            elif user_input == 2:
                self.product_query()
            elif user_input == 3:
                self.unitsinstock()
            elif user_input == 4:
                self.averageunitprice()

    def product_query(self):
        object = Connection() #Calling a class from a previous file
        cursor = object.databaseconnection()
        cursor.execute("SELECT ProductID, ProductName FROM Products")
        row = cursor.fetchmany(5)
        if row:
            print(row)

    def city_name(self):
        object = Connection()  # Calling a class from a previous file
        cursor = object.databaseconnection()
        cursor.execute("SELECT * FROM Customers WHERE City = 'Paris'")
        cities = cursor.fetchone()
        for city in cities:
            print(city)

    def unitsinstock(self):
        object = Connection()  # Calling a class from a previous file
        cursor = object.databaseconnection()
        cursor.execute("SELECT p.ProductName, p.UnitPrice FROM Products p WHERE UnitsInStock > 0 AND UnitPrice > 29.99")
        units = cursor.fetchall()
        for unit in units:
            print(unit.ProductName)

    def averageunitprice(self):
        object = Connection()
        cursor = object.databaseconnection()
        cursor.execute("SELECT AVG(UnitPrice) FROM Products")
        avg_unitprice = cursor.fetchall()
        for avg_unit in avg_unitprice:
            print(avg_unit)

