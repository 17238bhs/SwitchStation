from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABAASE_URI'] = 'sqlite:///switch.db'
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template("home.html", page_title="HOME")

if __name__ == "__main__":
    app.run(port=3000)