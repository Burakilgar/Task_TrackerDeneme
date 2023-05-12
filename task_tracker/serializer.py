from rest_framework import serializers
from .models import Task





class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = ['number', 'first_name', 'last_name']
        fields = '__all__'
        # exclude = ['id']