from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config) # applying all config to app
db = SQLAlchemy(app)

import models

@app.route('/')
def home():
    return render_template("home.html", page_title="Home")

@app.route('/learn')
def learn():
    return render_template("learn.html", page_title="learn")

@app.route('/all_switches')
def all_switches():
    results = models.Switch.query.all()
    return render_template ("all_switches.html", page_title="All Switches", switches = results)

@app.route('/switch/<int:id>')
def switch(id):
    switch = models.Switch.query.filter_by(id=id).first_or_404()
    return render_template ("switch.html", page_title="Switches", switch = switch)

if __name__ == "__main__":
    app.run(port=3000)