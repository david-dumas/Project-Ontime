import mysql.connector

print("enter people id: " )
x = input()

def get_client_detail(id):
    try:
        ontimedb = mysql.connector.connect(
            host="145.89.192.95",
            database="ontime",
            user="dbuser",
            password="Dbuser123!")

        cursor = ontimedb.cursor()
        sql_select_query = """SELECT * FROM people WHERE id = %s"""
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