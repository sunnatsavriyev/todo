from django.contrib import admin
from .models import ToDoModel
# Register your models here.

@admin.register(ToDoModel)
class ToDoAdmin(admin.ModelAdmin):
    list_display = (
        "work",
        "auther",
        "created_at", 
        "deadline",
        "completed",
        "worker"
    )

    list_filter = ["deadline", "completed"]  



