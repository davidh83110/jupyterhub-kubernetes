import requests
import json
import pymysql


all_congress = requests.get('https://theunitedstates.io/congress-legislators/legislators-current.json')


def get_infos(raw_data):
    name = raw_data['name']['official_full']

    for info in raw_data['terms']:
        pass

    party = info.get('party')
    state = info.get('state')
    office_address = info.get('address')
    office_phone = info.get('phone')
    start_date = info.get('start')
    end_date = info.get('end')

    
    return [name, party, state, office_address, office_phone, start_date, end_date]



def handler():
    json_all_congress = json.loads(all_congress.text)

    for member in json_all_congress:
        result = get_infos(member)
        
        connection = pymysql.connect(host='172.20.167.148',
                                 user='root',
                                 password='password',
                                 db='us_congress',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

        cursor = connection.cursor()


        sql = "INSERT INTO members (`name`, `party`, `state`, `office_address`, `office_phone`, `start_date`, `end_date`)  \
        VALUES (%s, %s, %s, %s, %s, %s, %s);"
        cursor.execute(sql, (result[0], result[1], result[2], result[3], result[4], result[5], result[6]))
        connection.commit()

        cursor.execute( "SELECT * FROM congress.members" )
        for r in cursor:
            print(r)
        cursor.close()
        connection.close()

if __name__ == '__main__':
    handler()
    
