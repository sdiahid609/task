from django.urls import path
from . import views
from task.views import task_new, task_list

urlpatterns = [
    path('', task_list.as_view(), name='task_list'),
    path('task/new/', task_new.as_view(), name='task_new'),
]