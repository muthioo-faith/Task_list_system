from django.urls import path
from task import views
from .views import TaskApiView




app_name="task"

urlpatterns=[
        path('login/',views.LoginApiView.as_view(), name='login'),
        path('task/',views.TaskApiView.as_view(),name='task'),
        path('subtask/',views.SubTaskApiView.as_view(),name='subtask'),

        
        ]
