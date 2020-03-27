from main import api,fields,Resource, create_access_token
from models.usersmodel import UserModel,user_schema,users_schema
from werkzeug.security import generate_password_hash 

#Creating Namespaces
ns_registration=api.namespace('signup',description="signup Handler")
ns_userLogin=api.namespace('login',description="Login Handler")


#Models

# Sign up model
signup_model=api.model('signup',{
    "full_name":fields.String(),
    "email":fields.String(),
    "password":fields.String()
})
# Sign in model
login_model=api.model('loginCredentials',{
"email":fields.String(),
"password":fields.String()})

@ns_userLogin.route('')
class login(Resource):
# pass ...
    @api.expect(login_model)
    def post(self):
        """Use this to authenticate users"""
        data=api.payload
        if UserModel.check_email_exist(data["email"]):
            if UserModel.validate_password(data["email"],data["password"]):
                # After login successful
                uid=UserModel.get_user_id(data["email"])
                token=create_access_token(identity=uid)
                return {"token":token}
    
            else:
                return {"message":"incorrect Login Credentials"}
        else:
            
            return {"Message":"Incorrect Login credentials"}


@ns_registration.route('')
class signup(Resource):
# api.expect decorator takes in the model you create above as an arguement
    @api.expect(signup_model)
    def post(self):
        """Add a user"""
        data=api.payload
        user=UserModel(full_name=data["full_name"],email=data["email"],password=
        generate_password_hash(data["password"]))
        user.save_to_db()

        
        return {"message":"Successfully signed Up"},201