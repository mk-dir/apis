from flask import Flask
from flask_restx import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy
from configs.DbConfigs import DevelopmentConfigs
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity


app=Flask(__name__)
app.config.from_object(DevelopmentConfigs)
api=Api(app,title="TASK_MGR_API",description="a simple manager api",version="1.0")

db=SQLAlchemy(app)
ma=Marshmallow(app)
jwt=JWTManager(app)

# models/Tables
from models.tasksmodel import TaskModel
from models.usersmodel import UserModel

@app.before_first_request
def create_tables():
    db.create_all()

from resources.tasks import *
from resources.users import *
from resources.login import *

#resource: Whatever you are offering on your api   