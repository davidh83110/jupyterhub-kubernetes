import requests
import json
import pymysql

class Mysql():

    def __init__(self):
        self.connection = pymysql.connect(host='172.20.167.148',
                                             user='root',
                                             password='password',
                                             db='us_congress',
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
    
    def __init__(self):
        self.all_congress_url = 'https://theunitedstates.io/congress-legislators/legislators-current.json'

    
    def _get_infos(self, raw_data):

        name = raw_data['name']['official_full']

        latest_term_info = raw_data['terms'][len(raw_data['terms'])-1]

        party = latest_term_info.get('party')
        state = latest_term_info.get('state')
        office_address = latest_term_info.get('address')
        office_phone = latest_term_info.get('phone')
        start_date = latest_term_info.get('start')
        end_date = latest_term_info.get('end')


        return [name, party, state, office_address, office_phone, start_date, end_date]


    def handler(self):
        all_congress = requests.get(self.all_congress_url)
        json_all_congress = json.loads(all_congress.text)

        for member in json_all_congress:
            congress = self._get_infos(member)

            sql = "INSERT INTO members (`name`, `party`, `state`, `office_address`, `office_phone`, `start_date`, `end_date`) VALUES (%s, %s, %s, %s, %s, %s, %s);"
            Mysql().do_query(sql, (congress[0], congress[1], congress[2], congress[3], congress[4], congress[5], congress[6]))

        Mysql().do_query( "SELECT * FROM develop.test" )

            
if __name__ == '__main__':
    Populate().handler()