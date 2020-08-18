import time

import mysql.connector
from mysql.connector import Error

def databaseConnect():
    try:
        connection = mysql.connector.connect(host='localhost', database='pakNsave', user='root', password='pebble29er')
        # connection = mysql.connector.connect(host='localhost', database='pakNsave', user='root', password='pebble29er', port=2000)
        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Connected to Mysql", db_info)
            return connection
        else:
            print("not connected")
    except Error as e:
        print("Error", e)


def addTypes(connection, listOfTypes):
        cursor = connection.cursor()
        query = "INSERT INTO Types (Type) VALUES (%s)"
        cursor.execute(query, "hi")
        query = "INSERT INTO `{}` (type) VALUES (%s)".format('Types')
        cursor.executemany(query, listOfTypes)
        connection.commit()
        cursor.close()
        

def addToDatabase(productList, priceList, connection):
        cursor = connection.cursor()
        query = "INSERT IGNORE INTO distinctProducts (productId, quantityType, name, weight, category1, category2) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.executemany(query, productList)
        connection.commit()

        time.sleep(2)

        query = "INSERT IGNORE INTO priceOnDate (productId, minAmount, price, store, date) VALUES (%s, %s, %s, %s, %s)"
        cursor.executemany(query, priceList)
        connection.commit()
        print("added To database")
        cursor.close()


def main():
    connection = databaseConnect()
    cursor = connection.cursor()
#    createTable(cursor, "21/12/19")
main()





