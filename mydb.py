#install Mysql on your computer
#install mysql-connector or  mysql-connector-python


import  mysql.connector

dataBase =  mysql.connector.connect(
    host = '',
    user = '',
    passwd = ''
)

#prepare a cursor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE elderco")


print("Database created")