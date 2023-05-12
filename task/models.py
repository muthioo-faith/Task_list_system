from collections import UserList
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



# STATUS_CHOICES=(
#    ('done','Done'),
#    ('rejected','Rejected')
# )

# # ASSIGNED_CHOICES=(
# #    ('ahmed','Ahmed'),
# #    ('munyagah','Munyagah')
# )

class MyUser(AbstractUser):
    phone_number = models.CharField(max_length=13)
    county = models.CharField(max_length=256,choices=COUNTY_CHOICES)
    id_number = models.CharField(max_length=100)
    id_document_type=models.CharField(max_length=50,choices=ID_DOCUMENT)

class Task(models.Model):
   title = models.CharField(max_length=250)
   assigned_to = models.ForeignKey(MyUser,on_delete=models.CASCADE,related_name='user_assigned_to',default=True)
   assigned_by = models.ForeignKey(MyUser,on_delete=models.CASCADE,related_name='user_assigned_by',default=True)
   creation_date =models.DateField(auto_now=False)
   due_date= models.DateField(blank=True, null=True)
   completed = models.BooleanField(default=False)
   #status=models.CharField(choices=STATUS_CHOICES)


class SubTask(models.Model):
    title =models.CharField(max_length=256)
    description=models.TextField(default=True)
    due_date = models.DateField(blank=True,null=True)
    # assigned_to = models.ForeignKey(MyUser,on_delete=models.CASCADE,related_name='user_assigned_by',default=True)
    # assigned_by = models.ForeignKey(MyUser,on_delete=models.CASCADE,related_name='user_assigned_by',default=True)
    # task = models.ForeignKey(MyUser,on_delete=models.CASCADE,related_name='_task')
    task = models.ForeignKey(Task, on_delete=models.CASCADE)



class Attribute(models.Model):
    name = models.CharField(max_length=100)
    assigned_to = models.ForeignKey(MyUser,on_delete=models.CASCADE,related_name='_assigned_to')

 