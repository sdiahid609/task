from django.urls import path
from . import views
from task.views import task_new, task_list, task_details, task_edit

urlpatterns = [
    path('', task_list.as_view(), name='task_list'),
    path('task/new/', task_new.as_view(), name='task_new'),
    path('task/<int:pk>/', task_details.as_view(), name='task_details'),
    path('task/edit/<int:pk>', task_edit.as_view(), name='task_edit'),

]