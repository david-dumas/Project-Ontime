import csv, flask, mysql.connector, jwt, datetime
from flask_login import LoginManager, UserMixin
from flask_cors import CORS
from flask import request, jsonify, session

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

@app.route("/getattendantv2", methods = ["GET"])
global mydb
global mycursor

def formatrecord(columns,record):
  number = len(columns)
  res = []
  for i in range(number):
    res.append((columns[i],record[i]))
  return res


def dbconnect():
  global mydb, mycursor
  mydb = mysql.connector.connect(host='145.89.192.95', user='dbuser', passwd='Dbuser123!', database='ontime')
  mycursor = mydb.cursor(prepared=True)

def dbclose():
  global mydb, mycursor
  mycursor.close()
  mydb.close()

def dbcommit():
  global mydb
  mydb.commit()

def nextid(query):
  resultset = executequery(query)
  maxid = resultset[0][0]
  resultset = resultset[1:]
  for record in resultset:
    if (record[0] > maxid):
      maxid = record[0]
  return (maxid+1)

def executequery(query):
  global mycursor
  dbconnect()
  resultset = []
  columns = []
  if (query == 'client'):
    sql = 'SELECT * FROM client;'
  elif (query == 'meta'):
    #metadata 'show fields from <tablename>;'
    #sql = 'show columns from tablename;'
    sql = 'describe client;'
  else:
    query = 'can be extended but never reached, use elif'
  mycursor.execute(sql)
  for (record) in mycursor:
    columns.append(record[0])
  mycursor.execute('select * from client')
  for record in mycursor:
    resultset.append(formatrecord(columns,record))
  return resultset

def insert(record):
  global mycursor
  dbconnect()
  sql = """ INSERT INTO people VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
  idplusone = nextid('people')
  # tuple to insert at placeholder
  tuple1 = (idplusone,record[0],record[1], record[2],record[3],record[4],record[5],record[6],record[7],record[8])
  mycursor.execute(sql, tuple1)
  dbcommit()
  dbclose()
  return("Data inserted successfully into employee table using the prepared statement")

def delete(id):
  global mycursor
  dbconnect()
  sql_Delete_query = """Delete from people where id = %s"""
  mycursor.execute(sql_Delete_query, (id,))
  dbcommit()
  dbclose()
  print("Record Deleted successfully using Parameterized query")



if __name__ == "__main__":
    app.run(debug = True)