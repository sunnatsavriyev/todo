from django.urls import path
from .views import ToDoApiView, ToDoDetail

urlpatterns = [
    path('',ToDoApiView.as_view()),
    path("<int:pk>/",ToDoDetail.as_view())
]