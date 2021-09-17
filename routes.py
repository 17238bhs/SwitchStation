from flask import Flask, render_template, redirect, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config) # applying all config to app
db = SQLAlchemy(app)

import models
from forms import Add_Switch, Edit_Switch # import forms being used from forms.py

@app.route('/')
def home():
    return render_template("home.html", page_title="Home")

@app.route('/learn')
def learn():
    return render_template("learn.html", page_title="learn")

@app.route('/all_switches')
def all_switches():
    results = models.Switch.query.order_by(models.Switch.id.desc()).all() # query for all switches
    return render_template ("all_switches.html", page_title="All Switches", switches = results)

@app.route('/switch/<int:id>')
def switch(id):
    switch = models.Switch.query.filter_by(id=id).first_or_404() # query for switch with specified id
    return render_template ("switch.html", page_title="Switches", switch = switch)

@app.route('/add_switch', methods=['GET', 'POST']) # page can recieve and send info
def add_switch():
    form = Add_Switch() # using the add switch form
    if request.method=='GET': # looking at the web page 
        return render_template('add_switch.html', form=form, title="Add a Switch")
    else: # POST scenario, when submitting info
        if form.validate_on_submit(): # built in validator to check if fields are filled out properly
            new_switch = models.Switch() # new switch instance
            new_switch.name = form.name.data # fields for new switch
            new_switch.manufacturer = form.manufacturer.data
            new_switch.style = form.style.data
            new_switch.color = form.color.data
            new_switch.description = form.description.data
            new_switch.cost = form.cost.data
            new_switch.actuation = form.actuation.data
            new_switch.bottomout = form.bottomout.data
            new_switch.pretravel = form.pretravel.data
            new_switch.totaltravel = form.totaltravel.data
            db.session.add(new_switch) # add to database
            db.session.commit() # commit to database
            return redirect(url_for('switch', id=new_switch.id)) # send user to new switch page
        else: # if form is not filled out properly
            return render_template('add_switch.html', form=form, title="Add a Switch")

@app.route('/all_prebuilts')
def all_prebuilts():
    results = models.Prebuilt.query.all() # query for all prebuilts
    return render_template ("all_prebuilts.html", page_title="All Prebuilts", prebuilts = results)

@app.route('/prebuilt/<int:id>')
def prebuilt(id):
    prebuilt = models.Prebuilt.query.filter_by(id=id).first_or_404() # query for prebuilt with specific id
    return render_template ("prebuilt.html", page_title="Prebuilts", prebuilt = prebuilt)

@app.route('/switch/<int:id>/edit', methods=['GET', 'POST'])
def edit_switch(id):
    form = Edit_Switch() # using the edit switch form
    if request.method=='GET': # looking at the web page 
        return render_template('edit_switch.html', form=form, title="Edit Switch")
    else: # POST scenario, when submitting info
        if form.validate_on_submit(): # built in validator to check if fields are filled out properly
            new_switch = models.Switch() # new switch instance
            new_switch.name = form.name.data # fields for new switch
            new_switch.manufacturer = form.manufacturer.data
            new_switch.style = form.style.data
            new_switch.color = form.color.data
            new_switch.description = form.description.data
            new_switch.cost = form.cost.data
            new_switch.actuation = form.actuation.data
            new_switch.bottomout = form.bottomout.data
            new_switch.pretravel = form.pretravel.data
            new_switch.totaltravel = form.totaltravel.data
            db.session.add(new_switch) # add to database
            db.session.commit() # commit to database
            return redirect(url_for('switch', id=new_switch.id)) # send user to new switch page
        else: # if form is not filled out properly
            return render_template('add_switch.html', form=form, title="Add a Switch")

@app.errorhandler(404) # 404 error handler, redirects to here when a 404 occurs
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(port=3000)