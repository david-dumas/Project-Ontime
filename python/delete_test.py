import csv, flask, mysql.connector
from flask_cors import CORS
from flask import request

app = flask.Flask(__name__)
CORS(app, supports_credentials=True)
app.config["DEBUG"] = True


with open(r"./mysql.txt") as f1:
    data=csv.reader(f1,delimiter=",")
    for row in data:
            host=row[0]
            database=row[1]
            user=row[2]
            password=row[3]

ontimedb = mysql.connector.connect(
    host=host,
    database=database,
    user=user,
    password=password)


@app.route("/deleteattendant", methods = ["POST"])
def delete_attendant_detail():
    delete_attendant = request.get_json()
    id = delete_attendant["id"]
    try:
        dbcursor = ontimedb.cursor()
        sql_delete_attendant_query = """DELETE FROM attendant 
                                WHERE id = %s"""
        dbcursor.execute(sql_delete_attendant_query, (id))

        ontimedb.commit()
        return("Delete succesful")

    except mysql.connector.Error as error:
        print("Failed to delete attendant from attendant table: {}".format(error))

    finally:
        if ontimedb.is_connected():
            dbcursor.close()
            print("MySQL connection is closed")


if __name__ == "__main__":
    app.run(debug = True)