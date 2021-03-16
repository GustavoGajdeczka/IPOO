import mysql.connector

cnx = mysql.connector.connect(user = 'root', password = '', host = '127.0.0.1')

mycursor = cnx.cursor()
mycursor.execute("CREATE DATABASE escolaPython")