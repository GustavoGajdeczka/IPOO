import mysql.connector
class sqlConnect:
    def __init__(self):
        self.user = 'root'
        self.password = ''
        self.database = 'escolapython'
        self.host = '127.0.0.1'
        self.db_info = None
        self.cnx = mysql.connector.connect(user = self.user, password = self.password, database = self.database, host = self.host)

    def testConnection(self):
        if self.cnx.is_connected():
            self.db_info = self.cnx.get_server_info()
            cursor = self.cnx.cursor()
            cursor.execute("select database();")
            linha = cursor.fetchone()
            print("Conectado ao banco de dados ",linha)

    def select(self, table):
        cursor = self.cnx.cursor()
        cursor.execute("SELECT * from " +  table)
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)

