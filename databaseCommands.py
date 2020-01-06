import mysql.connector

def databaseConnect():
    try:
        connection = mysql.connector.connect(host='45.76.124.20', database='specials', user='root', password='Cc5c8cac59')
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
            name varchar(80),\
            brand varchar(40),\
            origPrice Decimal(5,2),\
            salePrice Decimal(5,2),\
            volSize varchar(20),\
            saleType varchar(25),\
            minAmount int,\
            type varchar(25)\
            );".format(tableName)
    cursor.execute(stmt)



def addToDatabase(productDetails, connection, tableName):
        cursor = connection.cursor()
        query = "INSERT INTO `{}` (name, brand, origPrice, salePrice, volSize, saleType, minAmount, type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)".format(tableName)
        cursor.executemany(query, productDetails)
        connection.commit()
        print("added To database")
        cursor.close()


def main():
    connection = databaseConnect()
    cursor = connection.cursor()
    createTable(cursor, "21/12/19")





