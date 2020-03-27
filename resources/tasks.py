from main import api,fields,Resource, jwt_required,get_jwt_identity
from models.tasksmodel import TaskModel,task_schema,tasks_schema
from models.usersmodel import UserModel


ns_tasks=api.namespace('tasks',description="All Task Operations")


# models Documenting the nature of your Payload
task_model = api.model('Task', {
    'title':fields.String(),
    'description':fields.String(),
    'completed':fields.String()
})    

@ns_tasks.route('')
class Tasks (Resource):
    @jwt_required
    def get(self):
        """Use this Endpoint to get all Tasks"""
        uid=get_jwt_identity()
        user=UserModel.get_userby_id(uid)
        user_tasks=user.tasks
        
        return tasks_schema.dump(user_tasks),200

    
    @api.expect(task_model)
    @jwt_required
    def post(self):
        """Use this Endpoint to add all Tasks"""
        data=api.payload
        task=TaskModel(title=data["title"],description=data["description"],user_id=get_jwt_identity())
        task.save_to_db()

        return task_schema.dump(task),201



    
        

@ns_tasks.route('/<int:id>')
class Task(Resource):
    @jwt_required
    def get(self,id):
        task_flani=TaskModel.query.filter_by(id=id).first()
        return task_schema.dump(task_flani)

        """Fetch Task by id"""
        """for each in tasks:
            if each["id"]==id:
                return each
            else:
                return "Record unavailable" """
    
    @api.expect(task_model)
    @jwt_required
    def put(self,id):
        """Edit Task"""
        
        
        uid=get_jwt_identity()
        tasks=TaskModel.query.filter_by(user_id=uid).all()
        task_to_edit=None
        for each in tasks:
            if each.id==id:
                task_to_edit=each
                break
        
        

        
        data = api.payload
        
        if task_to_edit:
            if u'title' in data:
                task_to_edit.title=data['title']
            if u'description'in data:
                task_to_edit.description=data['description']
            if u'completed'in data:
                task_to_edit.completed=data['completed']

            task_to_edit.save_to_db()
            return {"message":"Task Edited Successfully"},200
        else:
            return {"message":"Task not found"},404
    

        
    @jwt_required
    def delete(self,id):
        """Delete Task"""
        uid=get_jwt_identity()

        task=TaskModel.query.filter_by(user_id=uid).all()
        task_to_del=None

        for each in task:
            if each.id==id:
                task_to_del=each

        if task_to_del:
            task_to_del.del_task()
            return {"Message":"Task Deleted Successfully"},200
        else:
            return {"message":"record not found"}, 404

        


            
                 