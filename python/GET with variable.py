import csv
import mysql.connector


#De inloggegevens van de database staan in een apart document in de volgende vorm: 'user','password','host','naam van de database'

with open(r"C:\Users\caspe\OneDrive\Documents\GitHub\Project-Ontime\txt\mysql.txt") as f1:
    data=csv.reader(f1,delimiter=",")
    for row in data:
            user=row[0]
            password=row[1]
            host=row[2]
            database=row[3]

print("enter client id: " )
x = input()

def get_client_detail(id):
    try:
        ontimedb = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password)

        cursor = ontimedb.cursor()
        sql_select_query = """SELECT * FROM client WHERE client_id = %s"""
        cursor.execute(sql_select_query, (id,))
        record = cursor.fetchall()
        print(record)

    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        if ontimedb.is_connected():
            cursor.close()
            ontimedb.close()
            print("MySQL connection is closed")

get_client_detail(x)