from rest_framework import serializers
from master . models import *


class TaskGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "name",
            "description",
            "task_type",
            "completed_at",
            "status",
            "assigned_users"
        ]

class AddUpdateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "name",
            "description",
            "task_type",
            "completed_at",
        ]

class UserGetSerializer(serializers.ModelSerializer):
    tasks = TaskGetSerializer(many=True)
    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "mobile",
            "username",
            "email", 
            "tasks"
        ]

