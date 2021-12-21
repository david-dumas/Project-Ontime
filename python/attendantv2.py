import csv, flask, mysql.connector
from flask_cors import CORS

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
def get_attendant_v2():
    def formatrecord(columns,record):
        number = len(columns)
        res = []
        for i in range(number):
          res.append((columns[i],record[i]))
        return res

    def nextid(query):
        resultset = executequery(query)
        maxid = resultset[0][0]
        resultset = resultset[1:]
        for record in resultset:
          if (record[0] > maxid):
            maxid = record[0]
        return (maxid+1)

    def executequery(query):
        ontimecursor = ontimedb.cursor()
        resultset = []
        columns = []
        if (query == "attendant"):
          sql = "SELECT * FROM attendant;"
        elif (query == "meta"):
          sql = "DESCRIBE attendant;"
        else:
          query = "can be extended but never reached, use elif"
        ontimecursor.execute(sql)
        for (record) in ontimecursor:
          columns.append(record[0])
        ontimecursor.execute("SELECT * FROM attendant")
        for record in ontimecursor:
          resultset.append(formatrecord(columns,record))
        return resultset


if __name__ == "__main__":
    app.run(debug = True)