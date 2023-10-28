import  mysql.connector


class DBconnection():
    def __init__(self):
        self.mydb = mysql.connector.connect(host="localhost", user="jamie", password="t3g7i", database="drumstickNation")
        self.mycursor = self.mydb.cursor()

    def execute_sql(self, sql_string):
        self.mycursor.execute(sql_string)
        self.mydb.commit()

    def close_connection(self):
        self.mycursor.close()
        self.mydb.close()

