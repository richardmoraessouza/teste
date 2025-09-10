
from . import views
from django.urls import path

urlpatterns = [
    path("", views.lista , name='lista'),
    path('api/tarefas/', views.api_tarefas, name='api_tarefas')
]