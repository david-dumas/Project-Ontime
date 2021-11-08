import csv
import mysql.connector
import flask
from flask_cors import CORS


#De inloggegevens van de database staan in een apart document in de volgende vorm: 'user','password','host','naam van de database'

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

with open(r"C:\Users\caspe\OneDrive\Documents\GitHub\Project-Ontime\txt\mysql.txt") as f1:
        data=csv.reader(f1,delimiter=",")
        for row in data:
            user=row[0]
            password=row[1]
            host=row[2]
            database=row[3]

@app.route("/addcontact", methods=["POST"])
def addcontact():    
    print("enter contact first name: " )
    firstname = input()
    print("enter contact surname: " )
    surname = input()
    print("enter contact phone: " )
    phone = input()
    print("enter contact mail: " )
    mail = input()
    print("enter contact city: " )
    city = input()
    print("enter contact street: " )
    street = input()
    print("enter contact housenumber: " )
    housenumber = input()
    print("enter contact postal code: " )
    postalcode = input()


    def insert_variables_into_contact(firstname, surname, phone, mail, city, street, housenumber, postalcode):
        try:
            ontimedb = mysql.connector.connect(
                    host=host,
                    database=database,
                    user=user,
                    password=password)

            mySql_insert_query = """INSERT INTO contact (firstname, surname, phone, mail, city, street, housenumber, postalcode) 
                                VALUES ( %s, %s, %s, %s, %s, %s, %s, %s) """

            cursor = ontimedb.cursor()
            cursor.execute(mySql_insert_query,(firstname, surname, phone, mail, city, street, housenumber, postalcode,))
            ontimedb.commit()
            print(cursor.rowcount, "Record inserted successfully into contact table")
            cursor.close()

        except mysql.connector.Error as error:
            print("Failed to insert record into contact table {}".format(error))

        finally:
            if ontimedb.is_connected():
                ontimedb.close()
                print("MySQL connection is closed")

    insert_variables_into_contact(firstname,surname,phone,mail,city,street,housenumber,postalcode)