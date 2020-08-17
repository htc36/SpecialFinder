import random
import time
from sqlite3 import Error

import mysql.connector

def databaseConnect():
    try:
        connection = mysql.connector.connect(host='127.0.0.1', database='specials3', user='root', password='pebble29er')
        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Connected to Mysql", db_info)
            return connection
        else:
            print("not connected")
    except Error as e:
        print("Error", e)

def createTable(cursor, tableName):
    cursor.execute("DROP TABLE IF EXISTS `{}`".format(tableName)) 
    stmt = "create table `{}` (\
            id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,\
            name varchar(80),\
            brand varchar(40),\
            origPrice Decimal(5,2),\
            salePrice Decimal(5,2),\
            volSize varchar(20),\
            saleType varchar(25),\
            minAmount int,\
            type varchar(25),\
            barcode char(13),\
            code varchar(25)\
            );".format(tableName)
    cursor.execute(stmt)



def addToDatabase(productDetails, connection, tableName):
        cursor = connection.cursor()
        query = "INSERT INTO `{}` (name, brand, origPrice, salePrice, volSize, saleType, minAmount, type, code, barcode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)".format(tableName)
        cursor.executemany(query, productDetails)
        connection.commit()
        print("added To database")
        cursor.close()
def addToDatabase2(productDataList, priceDataList, connection):
    cursor = connection.cursor()
    query = "INSERT IGNORE INTO `distinctProducts` (name, brand, volSize, type, barcode, code) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.executemany(query, productDataList)
    connection.commit()
    time.sleep(random.uniform(4,6))
    query = "INSERT IGNORE INTO `priceOnDate` (origPrice, salePrice, saleType, minAmount, barcode, date) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.executemany(query, priceDataList)
    connection.commit()
    print("added to database")
    cursor.close()

def main():
    connection = databaseConnect()
    cursor = connection.cursor()
    createTable(cursor, "21/12/19")

databaseConnect()



