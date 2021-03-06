from flask import Flask, render_template, redirect, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from config import Config
import models
from forms import Add_Switch, Edit_Switch # import forms from forms.py

app = Flask(__name__)
app.config.from_object(Config) # applying all config to app
db = SQLAlchemy(app)


@app.route('/')
def home():
    return render_template("home.html", page_title="Home")


@app.route('/learn')
def learn():
    return render_template("learn.html", page_title="learn")


@app.route('/all_switches')
def all_switches():
    # query to get all switches
    results = models.Switch.query.order_by(models.Switch.id.desc()).all()
    return render_template ("all_switches.html", 
                            page_title="All Switches", 
                            switches = results)


@app.route('/switch/<int:id>')
def switch(id):
    # query for switch with specified id
    switch = models.Switch.query.filter_by(id=id).first_or_404()
    return render_template ("switch.html", 
                            page_title="Switches", 
                            switch = switch)


@app.route('/add_switch', methods=['GET', 'POST']) # page can get & send info
def add_switch():
    form = Add_Switch() # using the add switch form
    
    if request.method=='GET': # looking at the web page 
        return render_template('add_switch.html', 
                                form=form, 
                                title="Add a Switch")

    else: # POST scenario, when submitting info
        # built in validator to check if fields are filled out properly
        if form.validate_on_submit():
            new_switch = models.Switch() # new switch instance
            new_switch.name = form.name.data # fields for new switch
            new_switch.manufacturer = form.manufacturer.data
            new_switch.style = form.style.data
            new_switch.color = form.color.data
            new_switch.cost = form.cost.data

            if form.description.data == "": # if description field is empty
                new_switch.description = "-" # replace with a dash
            else:
                # otherwise, do as normal
                new_switch.description = form.description.data

            if form.actuation.data == None: # if field is left blank (None)
                new_switch.actuation = "-" # replace with a dash
            else:
                new_switch.actuation = form.actuation.data
            
            if form.bottomout.data == None:
                new_switch.bottomout = "-"
            else:
                new_switch.bottomout = form.bottomout.data

            if form.pretravel.data == None:
                new_switch.pretravel = "-"
            else:
                new_switch.pretravel = form.pretravel.data

            if form.totaltravel.data == None:
                new_switch.totaltravel = "-"
            else:
                new_switch.totaltravel = form.totaltravel.data

            db.session.add(new_switch) # add to database
            db.session.commit() # commit to database
            # redirect user to newly created switch page
            return redirect(url_for('switch', 
                                    id=new_switch.id))

        else: # if form is not filled out properly
            return render_template('add_switch.html', 
                                    form=form, 
                                    title="Add a Switch")


@app.route('/switch/<int:id>/edit', methods=['GET', 'POST'])
def edit_switch(id):

    form = Edit_Switch() # using the edit switch form
    # query to get switch to be edited
    switch = models.Switch.query.filter_by(id=id).first_or_404()

    if request.method=='GET': # if just looking at the web page 
        # Pre-populate each field with the existing switch data
        form.name.data = switch.name
        form.manufacturer.data = switch.manufacturer
        form.style.data = switch.style
        form.color.data = switch.color
        form.description.data = switch.description
        form.cost.data = switch.cost
        form.actuation.data = switch.actuation
        form.bottomout.data = switch.bottomout
        form.pretravel.data = switch.pretravel
        form.totaltravel.data = switch.totaltravel

        return render_template('edit_switch.html', 
                                form=form, 
                                title="Edit Switch")

    else: # POST scenario, when submitting info
        # built in validator checks fields are filled out properly
        if form.validate_on_submit():
            switch.name = form.name.data # change field to user input
            switch.manufacturer = form.manufacturer.data
            switch.style = form.style.data
            switch.color = form.color.data
            switch.cost = form.cost.data

            if form.description.data == "": # if description field is empty
                switch.description = "-" # replace with a dash
            else:
                # otherwise, do as normal
                switch.description = form.description.data

            if form.actuation.data == None: # if field is left blank (None)
                switch.actuation = "-" # replace with a dash
            else:
                switch.actuation = form.actuation.data
            
            if form.bottomout.data == None:
                switch.bottomout = "-"
            else:
                switch.bottomout = form.bottomout.data

            if form.pretravel.data == None:
                switch.pretravel = "-"
            else:
                switch.pretravel = form.pretravel.data

            if form.totaltravel.data == None:
                switch.totaltravel = "-"
            else:
                switch.totaltravel = form.totaltravel.data
                
            db.session.merge(switch) # Must merge before committing edits
            db.session.commit() # commit to database
            # send user to the page of the switch being edited
            return redirect(url_for('switch', 
                                    id=switch.id))

        else: # if form is not filled out properly
            return render_template('edit_switch.html', 
                                    form=form, 
                                    title="Edit a Switch")


@app.route('/all_prebuilts')
def all_prebuilts():
    results = models.Prebuilt.query.all() # query for all prebuilts
    return render_template ("all_prebuilts.html", 
                            page_title="All Prebuilts", 
                            prebuilts = results)


@app.route('/prebuilt/<int:id>')
def prebuilt(id):
    # query for prebuilt with specific id
    prebuilt = models.Prebuilt.query.filter_by(id=id).first_or_404()
    return render_template ("prebuilt.html", 
                            page_title="Prebuilts", 
                            prebuilt = prebuilt)


@app.errorhandler(404) # 404 error handler, user sent here when 404 occurs
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(port=3000)