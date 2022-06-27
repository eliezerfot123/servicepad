from config.settings import db
from api.auth.models import Users

class Publication(db.Model):  
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(
        db.String(50), 
        unique=True, 
        nullable=False
    )   
    description = db.Column(
        db.Text 
    ) 
    priority = db.Column(db.String(50))  
    status = db.Column(db.Boolean)
    user_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, nullable=True)
    updated_at = db.Column(db.DateTime, nullable=True)


    def get_publication(_id):
        '''function to get publication using the id of the publication as parameter'''
        return [Publication.json(Publication.query.filter_by(id=_id).first())]
