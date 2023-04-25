from collections import UserList
from django.db import models
from django.contrib.auth.models import AbstractUser
from random import choices

COUNTY_CHOICES=(
        ('kajiado','Kajiado'),

        ('embu','Embu'),

        ('meru','Meru'),
        
        ('samburu','Samburu'),

        ('uasin_gishu','Uasin Gishu'),
    )
ID_DOCUMENT=(
    ('passport','Passport'),
    ('id_number','id number')
)

class MyUser(AbstractUser):
    phone_number = models.CharField(max_length=13)
    county = models.CharField(max_length=256,choices=COUNTY_CHOICES)
    id_number = models.CharField(max_length=100)
    id_document_type=models.CharField(max_length=50,choices=ID_DOCUMENT)


   

class Task(models.Model):

   title = models.CharField(max_length=250)
   assigned_to = models.ForeignKey(MyUser,on_delete=models.CASCADE,related_name="user_assigned_to")
   assigned_by = models.ForeignKey(MyUser,on_delete=models.CASCADE,related_name="user_assigned_by",null=True)
   creation_date =models.DateField(auto_now=False)
   due_date =models.DateField(blank=True, null=True)
   completed = models.BooleanField(default=False)
