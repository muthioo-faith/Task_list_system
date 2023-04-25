
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from task.models import Task

# from .forms import MyUserCreationForm, MyUserChangeForm
# from .forms import TaskCreationForm, TaskChangeForm




MyUser = get_user_model()

class MyUserAdmin(UserAdmin):
    # add_form = MyUserCreationForm
    # form = MyUserChangeForm
    model = MyUser
    list_display = ['username', 'phone_number', 'county','id_number','id_document_type']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('phone_number', 'county','id_number','id_document_type')}),

    )

admin.site.register(MyUser, MyUserAdmin)


class TaskAdmin(admin.ModelAdmin):
    # add_form = TaskCreationForm
    # form = TaskChangeForm
    model = Task
    list_display = ['title', 'assigned_to','assigned_by','creation_date','due_date','completed']
#     fieldsets = UserAdmin.fieldsets + (
#             (None, {'fields':('  title', 'assigned_to','creation_date','due_date','completed')
# }),

#     )

admin.site.register(Task, TaskAdmin)


