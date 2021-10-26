import csv
import mysql.connector


#De inloggegevens van de database staan in een apart document in de volgende vorm: 'user','password','host','naam van de database'

with open(r"C:\Users\caspe\OneDrive\Documents\GitHub\Ontime\ontime\txt\mysql.txt") as f1:
        data=csv.reader(f1,delimiter=",")
        for row in data:
            user=row[0]
            password=row[1]
            host=row[2]
            database=row[3]

    
print("enter contact first name: " )
firstname_contact = input()
print("enter contact surname: " )
surname_contact = input()
print("enter contact phone: " )
phone_contact = input()
print("enter contact mail: " )
mail_contact = input()
print("enter contact city: " )
city_contact = input()
print("enter contact street: " )
street_contact = input()
print("enter contact housenumber: " )
housenumber_contact = input()
print("enter contact postal code: " )
postalcode_contact = input()


def insert_variables_into_contact(firstname_contact, surname_contact, phone_contact, mail_contact, city_contact, street_contact, housenumber_contact, postalcode_contact):
    try:
        ontimedb = mysql.connector.connect(
                host=host,
                database=database,
                user=user,
                password=password)

        mySql_insert_query = """INSERT INTO contact (firstname_contact, surname_contact, phone_contact, mail_contact, city_contact, street_contact, housenumber_contact, postalcode_contact) 
                            VALUES ( %s, %s, %s, %s, %s, %s, %s, %s) """

        cursor = ontimedb.cursor()
        cursor.execute(mySql_insert_query,(firstname_contact, surname_contact, phone_contact, mail_contact, city_contact, street_contact, housenumber_contact, postalcode_contact,))
        ontimedb.commit()
        print(cursor.rowcount, "Record inserted successfully into contact table")
        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to insert record into contact table {}".format(error))

    finally:
        if ontimedb.is_connected():
            ontimedb.close()
            print("MySQL connection is closed")

insert_variables_into_contact(firstname_contact,surname_contact,phone_contact,mail_contact,city_contact,street_contact,housenumber_contact,postalcode_contact)