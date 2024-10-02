from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view # type: ignore
from rest_framework.response import Response # type: ignore
from apiapp.models import user_cred
from apiapp.models import todo_data


@api_view(["POST"])
def login(request, format=None):
   username = request.data.get("username")
   password = request.data.get('password')
   try:
      user_get = user_cred.objects.get(username = username)
   except:
      return Response({"message":"User doesn't exist!"})
   if check_password(password, user_get.password):
       return Response({"message": " Loginned successful"})
   else:
        return Response({"message": "wrong credentials"})
   
@api_view(["POST"])
def create_user(request, format=None):
    user =  request.data["username"]
    password = request.data.get("password")
    enc_pass = make_password(password)
    obj = user_cred(
           username = user,
           password = enc_pass
    )
    obj.save()
    return Response({
        " message":" user created successfully"})


@api_view(["POST"])
def create_todo(request,formate=None):
      title_input = request.data["title"]
      description_input = request.data["description"]
      sataus_input = ["In progress"]

      obj = todo_data (
                      title = title_input,
                      description = description_input,
                      status = sataus_input
                      )
      obj.save()
      return Response({"message":"sended successfully"})


@api_view(["GET"])
def initial_call(request,formate=None):
    all = todo_data.objects.all().values().count()
    completed =todo_data.objects.filter(status = "completed").values().count()
    in_progress =todo_data.objects.filter(status = "in_progess").values().count()
    archive =todo_data.objects.filter(status = "archived").values().count()
    stat = [{
             'lable':"All",
             'Value' :all 
            },
            {
             'lable':"completed",
             'Value' :completed
            },
            {
             'lable':"in_progress",
             'Value': in_progress
            },
            {
             'lable':"Archived",
             'Value' :archive 
            },
    ]

    todo = todo_data.objects.exclude(status = 'archived').all().values('id','title','description','status')
    return Response({
                    "message":" successful",
                    "stats": stat,
                    "todo_data":todo,
                    })

@api_view(["GET"])
def completed(request,formate=None):
    obj = todo_data.objects.filter(status="completed").values('id','title','description','status')

    return Response({
                    "message":"successful",
                    'todo_data':obj,
                    })

@api_view(["GET"])
def in_progress(request, format=None):
    obj = todo_data.objects.filter(status="in_progress").values('id', 'title', 'description', 'status')
    return Response({"message": "successful", 'todo_data': obj})


@api_view(["GET"])
def archived(request,formate=None):
    obj = todo_data.objects.filter(status="archived").values('id','title','description','status')
    
    return Response({
                    "message":"successful",
                    'todo_data':obj,
                    })

@api_view(["POST"])
def complete_task(request,formate=None):
    task_id = request.data['id']
    obj = todo_data.objects.filter(id = task_id).update(status = 'completed')
   
    all = todo_data.objects.all().values().count()
    completed =todo_data.objects.filter(status = "completed").values().count()
    in_progress =todo_data.objects.filter(status = "in_progess").values().count()
    archive =todo_data.objects.filter(status = "archived").values().count()
    stat = [{
             'lable':"All",
             'Value' :all 
            },
            {
             'lable':"completed",
             'Value' :completed
            },
            {
             'lable':"in_progress",
             'Value': in_progress
            },
            {
             'lable':"Archived",
             'Value' :archive 
            },
    ]

    todo = todo_data.objects.exclude(status = 'archived').all().values('id','title','description','status')
    return Response({
                    "message":" successful",
                    "stats": stat,
                    "todo_data":todo,
                    })

@api_view(["POST"])
def archived_task(request,formate=None):
    task_id = request.data['id']
    obj = todo_data.objects.filter(id = task_id).update(status = 'archived')
   
    all = todo_data.objects.all().values().count()
    completed =todo_data.objects.filter(status = "completed").values().count()
    in_progress =todo_data.objects.filter(status = "in_progess").values().count()
    archive =todo_data.objects.filter(status = "archived").values().count()
    stat = [{
             'lable':"All",
             'Value' :all 
            },
            {
             'lable':"completed",
             'Value' :completed
            },
            {
             'lable':"in_progress",
             'Value': in_progress
            },
            {
             'lable':"Archived",
             'Value' :archive 
            },
    ]

    todo = todo_data.objects.exclude(status = 'archived').all().values('id','title','description','status')
    return Response({
                    "message":" successful",
                    "stats": stat,
                    "todo_data":todo,
                    })

@api_view(["DELETE"])
def delete_task(request,formate=None):
    task_id = request.data['id']
    obj = todo_data.objects.filter(id = task_id).delete()

    all = todo_data.objects.all().values().count()
    completed =todo_data.objects.filter(status = "completed").values().count()
    in_progress =todo_data.objects.filter(status = "in_progess").values().count()
    archive =todo_data.objects.filter(status = "archived").values().count()
    stat = [{
             'lable':"All",
             'Value' :all 
            },
            {
             'lable':"completed",
             'Value' :completed
            },
            {
             'lable':"in_progress",
             'Value': in_progress
            },
            {
             'lable':"Archived",
             'Value' :archive 
            },
    ]

    todo = todo_data.objects.exclude(status = 'archived').all().values('id','title','description','status')
    return Response({
                    "message":" successful",
                    "stats": stat,
                    "todo_data":todo,
                    })


@api_view(["PUT"])
def update_task(request,formate=None):
     task_id = request.data['id']
     task_title =request.data['title']
     task_description =request.data['description']
     obj = todo_data.objects.filter(id = task_id).update(title = task_title,description = task_description)
     
     all = todo_data.objects.all().values().count()
     completed =todo_data.objects.filter(status = "completed").values().count()
     in_progress =todo_data.objects.filter(status = "in_progess").values().count()
     archive =todo_data.objects.filter(status = "archived").values().count()
     stat = [{
             'lable':"All",
             'Value' :all 
             },
             {
             'lable':"completed",
             'Value' :completed
             },
             {
             'lable':"in_progress",
             'Value': in_progress
             },
             {
             'lable':"Archived",
             'Value' :archive 
             },
            ]

     todo = todo_data.objects.exclude(status = 'archived').all().values('id','title','description','status')
     return Response({
                    "message":" successful",
                    "stats": stat,
                    "todo_data":todo,
                    })
   