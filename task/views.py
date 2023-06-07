# from task.models import User
from task.serializers import LoginSerializer
from rest_framework import generics
from rest_framework.response  import Response
from django.contrib.auth import authenticate  
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import SubTaskResSerializer, SubTaskSerializer, TaskSerializer
from rest_framework.views  import APIView
from .models import SubTask, Task
from django.shortcuts import render 
from rest_framework import status
from django.http import JsonResponse 

class LoginApiView(APIView):
	serializer_class = LoginSerializer
	def get(self, request):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user= authenticate(request, username=serializer.data["username"], password=serializer.data["password"])
		if user is not None:
			refresh = RefreshToken.for_user(user)
			return Response(
				{"refresh":str(refresh),
				"access": str(refresh.access_token)
     }
			)
		else:
			return Response(
				{"Error","Invalid password and username"}
			)
   
#    Api for adding subtask to task
#    Api for Task

# The first endpoint we will write enables us to view all of the articles
# In order for a user to have the ability to access the endpoint we just created we need to provide a URL
# We also need to include the following URLs within the main URLs file:
# The next thing you should do is to insert the serializer in our views and then request that the view 
# serialize all of the articles

# 

class TaskApiView(APIView):

    def get(self,request):
        tasks =Task.objects.all()
        serializer=TaskSerializer(tasks,many=True)
        return Response(
            {"tasks":serializer.data})
             
             
class SubTaskApiView(APIView):

    def post(self,request):
        Task = request.data
        serializer = TaskSerializer(data=Task)
        if serializer.is_valid(raise_exception=True):
            Task_saved=serializer.save()

        return Response({"success":"Task '{}' created successfully".format(Task_saved)})
  

# class SubTaskApiView(generics.CreateAPIView):
#     serializer_class = SubTaskSerializer
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         sub_task = SubTask.objects.create(
#             title=serializer.validated_data.get('title'),
#             assigned_by=serializer.validated_data.get('assigned_by'),
#             assigned_to=serializer.validated_data.get('assigned_to'),
#             task_id=serializer.validated_data.get('task_id'),
#             description=serializer.validated_data.get('description'),
#             due_date=serializer.validated_data.get('due_date'),
#             # status=serializer.validated_data.get('completed')
#             )
#         return Response(data=SubTaskResSerializer(sub_task).data, status=201)    

        
   