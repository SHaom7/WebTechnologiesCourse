from django.urls import path, include
from apps.usermodule import views

urlpatterns = [
    path('lab8/task7/', views.task7, name="users.task7"),
    path('lab11/part1/list/', views.list_students, name='users.list_students'),
    path('lab11/part1/add/', views.add_student, name='users.add_student'),
    path('lab11/part1/edit/<int:id>/', views.edit_student, name='users.edit_student'),
    path('lab11/part1/delete/<int:id>/', views.delete_student, name='users.delete_student'),
    path('lab11/part2/list/', views.list_students3, name='users.list_students3'),
    path('lab11/part2/add/', views.add_student3, name='users.add_student3'),
    path('lab11/part2/edit/<int:id>/', views.edit_student3, name='users.edit_student3'),
    path('lab11/part2/delete/<int:id>/', views.delete_student3, name='users.delete_student3'),
    path('lab11/part3/products/', views.list_products, name='users.list_products'),
    path('lab11/part3/products/add/', views.add_product, name='users.add_product'),
    path('lab11/part3/products/delete/<int:id>/', views.delete_product, name='users.delete_product'),
]
