from itertools import filterfalse
from .models import ToDoModel
from .serializers import ToDoSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .prmissions import IsAuthorOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class ToDoApiView(ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    serializer_class = ToDoSerializer
    queryset = ToDoModel.objects.all()
    filter_backends = [DjangoFilterBackend,SearchFilter ]
    filterset_fields = ["auther","worker"]
    search_fields = ["auther","worker__username"]



class ToDoDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ToDoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["auther","worker"]
    search_fields = ["auther","worker__username"]

    def get_queryset(self):
        return ToDoModel.objects.filter(worker=self.request.user)

