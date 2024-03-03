from django.urls import path

from todo import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('add_task/', views.TaskCreateView.as_view(), name='add_task'),
    path('tasks/<int:task_id>/', views.TaskDetailView.as_view(), name='detail_task'),
    path('tasks/<int:task_id>/edit/', views.TaskUpdateView.as_view(), name='edit_task'),
]
