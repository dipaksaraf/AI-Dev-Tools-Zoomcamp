from django.urls import path
from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.TodoListView.as_view(), name='todo-list'),
    path('todo/<int:pk>/', views.TodoDetailView.as_view(), name='todo-detail'),
    path('todo/add/', views.TodoCreateView.as_view(), name='todo-add'),
    path('todo/<int:pk>/edit/', views.TodoUpdateView.as_view(), name='todo-edit'),
    path('todo/<int:pk>/delete/', views.TodoDeleteView.as_view(), name='todo-delete'),
    path('todo/<int:pk>/toggle-resolved/', views.ToggleResolvedView.as_view(), name='todo-toggle-resolved'),
]
