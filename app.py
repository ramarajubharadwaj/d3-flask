import random

from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'charts'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
db = mysql.connect()
cursor = db.cursor()


@app.route('/')
def basic():
    return "Welcome Flask!"


@app.route('/random-data-read')
def data_read():
    randx = random.randint(1,10)
    randy = random.randint(1,100)
    cursor.execute("INSERT INTO chart1 (x_val,y_val) VALUES (" + str(randx) + "," + str(randy) + ")")
    db.commit()
    cursor.execute("SELECT x_val,y_val FROM (SELECT * FROM chart1 ORDER BY uid DESC LIMIT 100) res ORDER BY res.uid ASC")
    data = cursor.fetchall()
    return json.dumps({'msg':'ok','cdata':data})


@app.route("/data-save", methods=['POST'])
def data_save():
    cursor.execute("DELETE FROM chart2 WHERE 1")
    res = json.loads(request.data);
    for point in res['data']:
        cursor.execute("INSERT INTO chart2 (x_val,y_val) VALUES ('" + str(point[0]) + "','" +str(point[1]) + "')")  
    db.commit()
    return request.data


@app.route("/saved-data-read")
def saved_data_read():
    cursor.execute("SELECT x_val,y_val FROM chart2 WHERE 1")
    data = cursor.fetchall()
    return json.dumps({'msg':'ok','cdata':data})


if __name__=="__main__":
    app.debug = True
    app.run()
    app.run(debug = True)
