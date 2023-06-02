# from django.http import JsonResponse
# from task.serializers import TaskSerializer


# def post(self,request):
#     task= request.data.get('task')
#     serializer = TaskSerializer(data=task)
#     if serializer.is_valid(raise_exception=True):
        # task_saved=serializer.save()
#         return JsonResponse({'status': 'error', 'message': 'Invalid request method'})   