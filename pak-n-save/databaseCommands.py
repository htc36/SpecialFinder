import mysql.connector
from mysql.connector import Error

def databaseConnect():
    try:
        connection = mysql.connector.connect(host='localhost', database='pakNsave', user='root', password='pebble29er')
        #connection = mysql.connector.connect(host='localhost', database='pakNsave', user='root', password='pebble29er', port=2000)
        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Connected to Mysql", db_info)
            return connection
        else:
            print("not connected")
    except Error as e:
        print("Error", e)

def checkForDuplicate(cursor, tableName):
    stmt = "SHOW TABLES LIKE '{}'".format(tableName)
    cursor.execute(stmt)
    
    result = cursor.fetchone()
    print(result)
    if result:
        cursor.execute("DROP TABLE ")
        print("There was an existing table with the same name, so has been dropped")
    else:
        print("Unique table name")
        

    


def createTable(cursor, tableName):
    cursor.execute("DROP TABLE IF EXISTS `{}`".format(tableName)) 
    stmt = "create table `{}` (\
            id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,\
            quantityType varchar(8),\
            productId varchar(22),\
            name varchar (100),\
            weight varchar(10),\
            minAmount int,\
            price Decimal(5,2),\
            category1 varchar (40),\
            category2 varchar (40),\
            category3 varchar (40)\
            );".format(tableName)
    cursor.execute(stmt)
def eaddToDatabase(productDetails, connection, tableName):
        cursor = connection.cursor()
        query = "INSERT INTO `{}` (quantityType, productId, name, weight, minAmount, price, category1, category2) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)".format(tableName)
        cursor.executemany(query, productDetails)
        connection.commit()
        print("added To database")
        cursor.close()

def addTypes(connection, listOfTypes):
        cursor = connection.cursor()
        print(listOfTypes)
        query = "INSERT INTO Types (Type) VALUES (%s)"
        cursor.execute(query, "hi")
        query = "INSERT INTO `{}` (type) VALUES (%s)".format('Types')
        cursor.executemany(query, listOfTypes)
        connection.commit()
        print("added To database")
        cursor.close()
        

def addToDatabase(productDetails, connection, tableName):
        cursor = connection.cursor()
        query = "INSERT INTO `{}` (quantityType, productId, name, weight, minAmount, price, category1, category2, category3) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)".format(tableName)
        cursor.executemany(query, productDetails)
        connection.commit()
        print("added To database")
        cursor.close()




def main():
    connection = databaseConnect()
    cursor = connection.cursor()
#    createTable(cursor, "21/12/19")
main()





