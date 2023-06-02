from rest_framework import serializers
from .models import SubTask, Task

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()


class TaskSerializer(serializers.Serializer):
    title=serializers.CharField(max_length=120)
    description=serializers.CharField()
    due_date=serializers.DateField()
    # status=serializers.CharField()
    assigned_to=serializers.CharField()
    assigned_by=serializers.CharField()
    # subtask_id=serializers.IntegerField()

    
    
    
    def create (self,validated_data):
        return Task.objects.create(**validated_data)
    
class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ('task_id', 'assigned_to', 'assigned_by', 'description', 'title', 'due_date')
        
        
class SubTaskResSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'




