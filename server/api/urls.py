from django.urls import path,include
from .views import apiOverView
from . import views

urlpatterns = [
    path('', apiOverView, name='apiOverView'),
    path('task-list/', views.taskList, name='task-list'),
    path('task-detail/<str:pk>' ,views.taskDetail, name = 'task-detail'),
    path('task-create/', views.taskCreate, name='task-create'),
    path('task-update/<str:pk>' ,views.taskUpdate, name = 'task-update'),
    path('task-delete/<str:pk>' ,views.taskDelete, name = 'task-delete'),
]