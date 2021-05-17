from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///switch.db'
db = SQLAlchemy(app)

class Switch (db.Model):
    __tablename__ = "Switch"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())
    brand = db.Column(db.String())
    style = db.Column(db.String())
    color = db.Column(db.String())
    spring = db.Column(db.Integer())
    description = db.Column(db.String())

class Prebuilt (db.Model):
    __tablename__ = "Prebuilt"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())
    layout = db.Column(db.String())
    brand = db.Column(db.String())
    hotswap = db.Column(db.Boolean())
    rgb = db.Column(db.Boolean())
    description = db.Column(db.String())

prebuilt = db.Table ('prebuilt', db.Column('sid', db.Integer, db.ForeignKey('Switch.id'), primary_key=True), db.Column('pid', db.Integer, db.ForeignKey('Prebuilt.id'), primary_key=True))

@app.route('/')
def home():
    return render_template("home.html", page_title="Home")

@app.route('/switch/<int:id>')
def switch(id):
    switch = Switch.query.filter_by(id=id).first_or_404()
    return render_template ("switch.html", page_title="Switches", switch = switch)

#@app.route('/prebuilt/<int:id>')
#def prebuilt(id):
#    prebuilt = Prebuilt.query.filter_by(id=id).first_or_404()
#    return render_template("prebuilts.html", page_title="Prebuilts", prebuilt = prebuilt)

if __name__ == "__main__":
    app.run(port=3000)