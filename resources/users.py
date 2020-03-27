from main import api,fields,Resource
from models.usersmodel import UserModel,user_schema,users_schema

ns_users=api.namespace('users',description="Deals with User manipulations")

# models
user_model = api.model('User', {
    'full_name':fields.String(),
    'email':fields.String(),
    'password':fields.String()
})  

@ns_users.route('')
class Users(Resource):
    def get(self):
        """Fetch all users"""
        wote=UserModel.fetch_all()

        print (users_schema.dump(wote))
        return users_schema.dump(wote)
   
    
@ns_users.route("/<int:id>") 

class User(Resource):
    def get(self,id):
        """Fetch User by id"""

        msee_flani=UserModel.query.filter_by(id=id).first()

        return user_schema.dump(msee_flani)
    @api.expect(user_model)
    def put(self,id):
        """Edit User"""
        data = api.payload
        msee_flani=UserModel.query.filter_by(id=id).first()
        if msee_flani:
            if u'full_name' in data:
                msee_flani.full_name=data['full_name']
            if u'email'in data:
                msee_flani.email=data['email']
            if u'password' in data:
                msee_flani.password=data['password']
            
            msee_flani.save_to_db()
            return {"message":"Fields Edited Successfully"},200
        else:
            return {"message":"User not found"},404

        


    def delete(self,id):
        """Delete User"""
        msee_flani=UserModel.query.filter_by(id=id).first()

        if msee_flani:
            msee_flani.del_user()
            return {"message":"Account Deleted"}, 200
        else:
            return {"message":"User Doesn't Exist"}, 404
        
