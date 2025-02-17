from django.urls import path, include
from apps.bookmodule import views

urlpatterns = [
    #path('first/', views.index),
    #path('', views.index1),
    #path('index2/<int:val1>/', views.index2) 
    path('', views.index),
    path('index2/<int:val1>/', views.index2),
    path('<int:bookId>', views.viewbook)
]

