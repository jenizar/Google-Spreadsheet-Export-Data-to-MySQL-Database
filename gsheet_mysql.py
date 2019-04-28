from flask import Flask, request, jsonify, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#Create your Database URI, get the username, database name and hostname from the Database tab page.
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="yourname",
    password="yourpassword",
    hostname="yourname.db.pythonanywhere-services.com",
    databasename="dbname",
)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class modb(db.Model):
    __tablename__ = "mtmast"
    matnr = db.Column(db.String(7), primary_key=True)
    maktx = db.Column(db.String(25))
    matkl = db.Column(db.String(9))
    mtart = db.Column(db.String(4))
    meins = db.Column(db.String(4))
    laeda = db.Column(db.String(10))

@app.route('/processjson', methods = ['POST'])
def processjson():
    #data = request.get_json()
    matnr = request.json['matnr']
    maktx = request.json['maktx']
    matkl = request.json['matkl']
    mtart = request.json['mtart']
    meins = request.json['meins']
    laeda = request.json['laeda']
    var1 = modb(matnr=matnr, maktx=maktx, matkl=matkl, mtart=mtart, meins=meins, laeda=laeda)

    db.session.add(var1)
    db.session.commit()
    return jsonify({'result' : 'Success!', 'matnr' : matnr, 'maktx' : maktx, 'matkl' : matkl, 'mtart' : mtart, 'meins' : meins, 'laeda' : laeda})

if __name__ == '__main__':
   app.run(debug = True)

