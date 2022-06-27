from distutils.command.config import config
from flask import Flask, request, jsonify, current_app
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger, swag_from
from config.swagger import swagger_config, template
import jwt

app = Flask(__name__) 
Swagger(
    app, config=swagger_config, template=template
)
SECRET_KEY = 'JUaZYfFml7'
app.config['SECRET_KEY'] = SECRET_KEY

#app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.db' 
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://eliox:1234@localhost/servicepad'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


