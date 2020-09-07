from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField()
	class Meta:
		model = Task
		fields = '__all__'