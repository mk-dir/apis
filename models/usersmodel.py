from main import db, ma
from sqlalchemy import func
from werkzeug.security import check_password_hash
# from models.tasksmodel import TaskModel

class UserModel(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    full_name=db.Column(db.String(),nullable=False)
    email=db.Column(db.String(),nullable=False)
    password=db.Column(db.String(),nullable=False,default=0)
    created_at=db.Column(db.DateTime(timezone=True),default=func.now())
    tasks=db.relationship('TaskModel',backref='user', lazy=True)
    

    def create_record(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def fetch_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def del_user(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def check_email_exist(cls,email):
        mail=cls.query.filter_by(email=email).first()
        if mail:
            return True
        else:
            return False

    @classmethod
    def validate_password(cls,email,password):
        record=cls.query.filter_by(email=email).first()

        if record and check_password_hash(record.password,password):
            return True
        else:
            return False

        
    @classmethod
    def get_user_id(cls,email):
        
        return cls.query.filter_by(email=email).first().id

    @classmethod
    def get_userby_id(cls,id):
        
        return cls.query.filter_by(id=id).first()



class UserSchema(ma.Schema):
    class Meta:
        fields=("id","full_name","email")

user_schema=UserSchema()
# tasks serializes a 
users_schema=UserSchema(many=True) 