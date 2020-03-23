tasks=[
    {"id":1,"title":"Learn flask RestX","description":"Learn the Basics"},
    {"id":2,"title":"Learn Javascript","description":"Learn the Basics"},
    {"id":3,"title":"Learn Docker","description":"Learn the Basics"},
    {"id":4,"title":"Learn Django","description":"Learn the Basics"}]
counter=0

while counter<len(tasks):
    x=tasks[counter]
    if x["id"]==10:
        tasks.pop(counter)
        break
    else:
         pass
    
        

    counter+=1

print(tasks)