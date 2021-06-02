from routes import db

class Switch (db.Model):
    __tablename__ = "Switch"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())
    brand = db.Column(db.String())
    style = db.Column(db.String())
    color = db.Column(db.String())
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

# prebuilt = db.Table ('prebuilt', db.Column('sid', db.Integer, db.ForeignKey('Switch.id'), primary_key=True), db.Column('pid', db.Integer, db.ForeignKey('Prebuilt.id'), primary_key=True))
