from django.urls import path
from . import views

urlpatterns=[
    path('list/',views.list_todo_items,name='list_todo_items'),
    path('insert_todo/',views.insert_todo_item,name='insert_todo_item'),
    path('delete_todo/<int:todo_id>/',views.delete_todo_item,name='delete_todo_item'),
    path('update_todo/<int:todo_id>/',views.update_todo_status,name='update_todo_item'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login_user,name='login_user'),
    path('logout/',views.logout_user,name='logout_user')
]