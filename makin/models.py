from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
class Task(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    complete=models.BooleanField(default=False)
    create=models.DateTimeField(auto_now_add=True)
    def __str__(self):
          return self.title
    class Meta:
        ordering=['complete']

class Feedback(models.Model):
    customer_name = models.CharField(max_length=120)
    email = models.EmailField()
    product = models.ForeignKey(Task,on_delete=models.CASCADE,null=True,blank=True)
    details = models.TextField()
    happy = models.BooleanField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.customer_name 
