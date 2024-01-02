from django.urls import path

from . import views

urlpatterns = [
    path('', views.getData),
      path('<str:task_id>/', views.check_task_status, name='check_task_status'),
]