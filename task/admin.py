
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from task.models import Task
from task.models import SubTask,Attribute






MyUser = get_user_model()

class MyUserAdmin(UserAdmin):
 
    model = MyUser
    list_display = ['username', 'phone_number', 'county','id_number','id_document_type']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('phone_number', 'county','id_number','id_document_type')}),
    )

admin.site.register(MyUser, MyUserAdmin)

class TaskAdmin(admin.ModelAdmin):
  
    model = Task
    list_display = ['title','assigned_to','assigned_by','creation_date','due_date','completed']

admin.site.register(Task, TaskAdmin)


class SubTaskAdmin(admin.ModelAdmin):
    model = SubTask
    list_display = ['title','description','due_date','task']
admin.site.register(SubTask ,SubTaskAdmin)



class AttributeAdmin(admin.ModelAdmin):
    model = Attribute
    list_display = ['name','assigned_to']
admin.site.register(Attribute,AttributeAdmin)