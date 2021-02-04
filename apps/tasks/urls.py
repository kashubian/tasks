from django.urls import path
from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.TasksListView.as_view(), name='tasks'),
    path('<uuid:pk>/', views.TaskDetailView.as_view(), name='task')
]
