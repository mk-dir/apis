from flask import Flask
from flask_restx import Api, Resource, fields

app=Flask(__name__)
api=Api(app,title="TASK_MGR_API",description="a simple manager api",version="1.0")



from resources.tasks import *
from resources.users import *

#resource: Whatever you are offering on your api   