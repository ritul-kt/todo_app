from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpRequest
from .models import Todo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.utils import timezone




# Create your views here.
@login_required(login_url='login_user')
def list_todo_items(request):
   todos = Todo.objects.filter(user=request.user)
   todays_date = timezone.now() - timedelta(hours=24)
   context = {
       'todo_list': todos,
       'todays_date': todays_date,
    }
   return render(request, 'todos/todo_list.html', context)


@login_required(login_url='login_user')
def insert_todo_item(request:HttpRequest):
   if request.method == "POST":
        content = request.POST.get('content')
        if content: 
            todo = Todo(content=content, user=request.user)  
            todo.save()
   return redirect('/todos/list/')

def delete_todo_item(request,todo_id):
   todo_to_delete=Todo.objects.get(id=todo_id)
   todo_to_delete.delete()
   return redirect('/todos/list/')

def update_todo_status(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.status = not todo.status 
    todo.save()
    return redirect('/todos/list/') 


def signup(request):
  print("meth",request.method)
  if request.method=="POST":
     email=request.POST.get('email')
     username=request.POST.get('username')
     password=request.POST.get('password')


     user =User.objects.create(
        email=email,
        username=username,
     )
     user.set_password(password)
     user.save()
     print(user)
     users = User.objects.all()
     print(users)
     return redirect('login_user')
  return render(request,'todos/signup.html/')

def login_user (request):
   print("method",request.method)
   if request.method =="POST":
      username= request.POST.get('username')
      userpassword=request.POST.get('password')

      print("username",username)
      print("password",userpassword)

      if User.objects.filter(username=username).exists():
         user = authenticate( username=username , password=userpassword )
         print('user',user)
         if user is not None:
            login(request,user)
            messages.success(request,'Successfully logged in')
            return redirect('list_todo_items')
         else: 
            messages.error(request,'Invalid Password')
            return redirect('login_user')
      else:      
         messages.error(request,'Invalid Username')
         return redirect('signup')
   return render(request,'todos/login.html/')

def logout_user(request):
   logout(request)
   return redirect('login_user')
