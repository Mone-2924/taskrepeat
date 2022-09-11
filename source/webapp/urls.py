from django.contrib import admin
from django.urls import path

from webapp.views import index_view, create_task, task_view

urlpatterns = [
    path('', index_view, name='index_view'),
    path('task/add/', create_task, name='create_task'),
    path('task/<int:pk>/', task_view, name='task_view'),

]