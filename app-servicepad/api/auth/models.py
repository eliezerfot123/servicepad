from config.settings import db

class Users(db.Model):  
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)  
    fullname = db.Column(db.String(50))
    email = db.Column(db.String(50),unique=True)
    password = db.Column(db.String(200))
    images = db.Column(db.String(100))
    
  