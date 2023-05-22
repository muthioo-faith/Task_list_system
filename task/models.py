# from collections import UserList
# # import select
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



STATUS_CHOICES=(
   ('backlog','BackLog'),
   ('inprogress','Inprogress'),
   ('complete','Complete')
)

# # ASSIGNED_CHOICES=(
# #    ('ahmed','Ahmed'),
# #    ('munyagah','Munyagah')
# )

class MyUser(AbstractUser):
    phone_number = models.CharField(max_length=13)
    county = models.CharField(max_length=256,choices=COUNTY_CHOICES)
    id_number = models.CharField(max_length=100)
    id_document_type=models.CharField(max_length=50,choices=ID_DOCUMENT)

class TimestampModel(models.Model):
   created_at = models.DateTimeField(auto_now=True)
   updated_at = models.DateTimeField(auto_now=True)
   deleted_at = models.DateTimeField(auto_now=True)


class BaseTaskModel(TimestampModel):
   title = models.CharField(max_length=250)
   assigned_to = models.CharField(default=True)
   assigned_by = models.CharField(default=True)
   creation_date =models.DateField(default=True)
   description = models.TextField(max_length=250,default=True)
   due_date= models.DateField(max_length=250)
   status = models.CharField(max_length=100,choices=STATUS_CHOICES,default=True)

   class Meta:
      abstract = True

class Task(BaseTaskModel):
   class Meta:
      ordering = ["due_date"]
   

class SubTask(BaseTaskModel):
   class Meta:
      ordering = ["due_date"]


class Attribute(models.Model):
    title = models.CharField(max_length = 100)
    assigned_to = models.ForeignKey(MyUser, on_delete = models.CASCADE)