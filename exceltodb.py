import json
import mysql.connector
# JSON
f = open("location", encoding="utf8")
data = json.load(f)

# Database Connection
conn = mysql.connector.connect(
    database='name', user='root', password='', host='127.0.0.1', port='3306')
cursor = conn.cursor()
tableCreationSql = '''
    CREATE TABLE jobs(
        ID SERIAL PRIMARY KEY,
        JOB_NAME TEXT,
        LINK TEXT,
        LOCATION TEXT,
        PUBLISHED_ON DATE
        )
'''
cursor.execute(tableCreationSql)
conn.commit()

insertDataSql = '''
    INSERT INTO jobs (JOB_NAME, LINK, LOCATION, PUBLISHED_ON) VALUES (%s,%s,%s,%s)
'''

for item in data:
    for i in item:
        name = item[i][0]
        location = item[i][1]
        date = item[i][2]
        link = item[i][3]
        dataToInsert = (name, link, location, date)
        cursor.execute(insertDataSql, dataToInsert)
        conn.commit()
f.close()
