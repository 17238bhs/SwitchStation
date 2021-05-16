from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABAASE_URI'] = 'sqlite:///switch.db'
db = SQLAlchemy(app)

class Switches (db.Model):
    __tablename__ = "Switches"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())
    brand = db.Column(db.String())
    style = db.Column(db.String())
    color = db.Column(db.String())
    spring = db.Column(db.String())
    description = db.Column(db.String())

class Prebuilts (db.Model):
    __tablename__ = "Prebuilts"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())
    layout = db.Column(db.String())
    brand = db.Column(db.String())
    hotswap = db.Column(db.Boolean())
    rgb = db.Column(db.Boolean())
    description = db.Column(db.String())

@app.route('/')
def home():
    return render_template("home.html", page_title="Home")

@app.route('/prebuilts')
def prebuilts():
    return render_template("prebuilts.html", page_title="Prebuilts")

if __name__ == "__main__":
    app.run(port=3000)