from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    content=models.TextField()
    status = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)


