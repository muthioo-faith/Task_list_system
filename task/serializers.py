from rest_framework import serializers
from .models import SubTask, Task

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = "__all__"

class TaskSerializer(serializers.ModelSerializer):
    parent_task=SubTaskSerializer(many=True,read_only=True,source="task")
    class Meta:
        model = SubTask
        fields = '__all__'

    
    
    
    def create (self,validated_data):
        return Task.objects.create(**validated_data)
    

        
        
class SubTaskResSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'



