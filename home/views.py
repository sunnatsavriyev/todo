from .models import ToDoModel
from .serializers import ToDoSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions


class ToDoApiView(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ToDoSerializer

    def get_queryset(self):
        return ToDoModel.objects.filter(worker=self.request.user)


class ToDoDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ToDoSerializer

    def get_queryset(self):
        return ToDoModel.objects.filter(worker=self.request.user)

