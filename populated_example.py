import requests
import json
import pymysql

class Mysql():

    def __init__(self):
        self.connection = pymysql.connect(host='172.20.167.148',
                                             user='root',
                                             password='password',
                                             db='develop',
                                             charset='utf8mb4',
                                             cursorclass=pymysql.cursors.DictCursor)
        
    def do_query(self, sql_string, data=None):
        cursor = self.connection.cursor()
        result_list = []

        if 'select' in sql_string or 'SELECT' in sql_string:
            cursor.execute(sql_string)
            
            for r in cursor:
                result_list.append(r)

            print(result_list)

        
        elif 'insert' in sql_string or 'INSERT' in sql_string:
            cursor.execute(sql_string, data)
            self.connection.commit()
            
        else:
            return 'Query Method not Allowed'
        
        cursor.close()
        self.connection.close()

        
        
class Populate():

    def handler(self):
        sql = "INSERT INTO test (`name`, `gender`) VALUES (%s, %s);"
        Mysql().do_query(sql, ('david', 'Male'))
        Mysql().do_query( "SELECT * FROM develop.test" )

            
if __name__ == '__main__':
    Populate().handler()