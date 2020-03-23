from main import api,fields,Resource

ns_tasks=api.namespace('tasks',description="All Task Operations")

tasks=[
    {"id":1,"title":"Learn flask RestX","description":"Learn the Basics"},
    {"id":2,"title":"Learn Javascript","description":"Learn the Basics"},
    {"id":3,"title":"Learn Docker","description":"Learn the Basics"},
    {"id":4,"title":"Learn Django","description":"Learn the Basics"}]

# models
task_model = api.model('Task', {
    'title':fields.String(),
    'description':fields.String()
})    

@ns_tasks.route('')
class Tasks (Resource):
    def get(self):
        """Use this Endpoint to get all Tasks"""
        return tasks,200

    @api.expect(task_model)
    def post(self):
        """Use this Endpoint to add all Tasks"""
        data=api.payload
        data["id"]=len(tasks)+1
        tasks.append(data)
        return data,201

@ns_tasks.route('/<int:id>')
class Task(Resource):
    def get(self,id):
        """Fetch Task by id"""
        for each in tasks:
            if each["id"]==id:
                return each
            else:
                return "Record unavailable"

    @api.expect(task_model)
    def put(self,id):
        """Edit Task"""
        data = api.payload
        task=next(filter(lambda x: x['id']==id,tasks),None)

        if task:
            if u'title' in data:
                task['title']=data['title']
            if u'description'in data:
                task['description']=data['description']
            return tasks,200
        else:
            return {"message":"Task not found"},404

        

    def delete(self,id):
        """Delete Task"""
        counter=0

        while counter<len(tasks):
            x=tasks[counter]
            if x["id"]==id:
                tasks.pop(counter)
                return {"message":"Item Deleted Successfully"},200
                
            
            return {"message":"Task does not Exist"},404



            counter+=1
                 