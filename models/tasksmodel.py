from main import db, ma
from sqlalchemy import func
# from models.usersmodel import UserModel

class TaskModel(db.Model):
    __tablename__='tasks'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(),nullable=False)
    description=db.Column(db.String(),nullable=False)
    completed=db.Column(db.String(),nullable=False,default=0)
    created_at=db.Column(db.DateTime(timezone=True),default=func.now())
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))

    def creat_record(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def fetch_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def del_task(self):
        db.session.delete(self)
        db.session.commit()

        
    




class TaskSchema(ma.Schema):
    class Meta:
        fields=("id","title","description","user_id")

task_schema=TaskSchema()
# tasks serializes a 
tasks_schema=TaskSchema(many=True) 