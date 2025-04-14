from django.urls import path, include
from apps.usermodule import views

urlpatterns = [
    path('lab8/task7/', views.task7, name="users.task7"),

]
