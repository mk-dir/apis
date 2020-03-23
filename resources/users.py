from main import api,fields,Resource

ns_users=api.namespace('users',description="Deals with User manipulations")

@ns_users.route('')
class Users(Resource):
    def get(self):
        """Fetch all users"""
        pass

    def post(self):
        """Add a user"""
        pass
    
@ns_users.route("/<int:id>") 

class User(Resource):
    def get(self,id):
        """Fetch User by id"""
        pass

    def put(self,id):
        """Edit User"""
        pass

    def delete(self,id):
        """Delete User"""
        pass    
