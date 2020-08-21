import random
import time
from sqlite3 import Error

import mysql.connector

def databaseConnect():
    try:
        connection = mysql.connector.connect(host='127.0.0.1', database='specials4', user='root', password='pebble29er')
        # connection = mysql.connector.connect(host='127.0.0.1', database='specials4', user='root', password='pebble29er', port=2000)
        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Connected to Mysql", db_info)
            return connection
        else:
            print("not connected")
    except Error as e:
        print("Error", e)

def addToDatabase(productDetails, connection, tableName):
        cursor = connection.cursor()
        query = "INSERT INTO `{}` (name, brand, origPrice, salePrice, volSize, saleType, minAmount, type, code, barcode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)".format(tableName)
        cursor.executemany(query, productDetails)
        connection.commit()
        print("added To database")
        cursor.close()
def addToDatabase2(productDataList, priceDataList, connection):
    cursor = connection.cursor()
    query = "INSERT INTO `cdProducts` (name, brand, volSize, type, barcode, code, image) VALUES (%s, %s, %s, %s, %s, %s, %s) " \
            "ON DUPLICATE KEY UPDATE name=VALUES (name), brand=VALUES(brand), volSize=VALUES(volSize), type = VALUES(type), barcode=VALUES(barcode), image=VALUES(image)"
    cursor.executemany(query, productDataList)
    connection.commit()
    time.sleep(random.uniform(4,6))
    query = "INSERT INTO `cdPrices` (origPrice, salePrice, saleType, minAmount, code, date) VALUES (%s, %s, %s, %s, %s, %s)" \
            "ON DUPLICATE KEY UPDATE origPrice=VALUES(origPrice), salePrice=VALUES(salePrice), saleType=VALUES(saleType), minAmount=VALUES(minAmount)"
    cursor.executemany(query, priceDataList)
    connection.commit()
    print("added to database")
    cursor.close()

def main():
    connection = databaseConnect()
    cursor = connection.cursor()

databaseConnect()



