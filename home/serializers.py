from .models import ToDoModel
from rest_framework import serializers


class ToDoSerializer (serializers.ModelSerializer):
    class Meta:
        model=ToDoModel
        fields = "__all__"


