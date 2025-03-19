from django.urls import path, include
from apps.bookmodule import views

urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('list_books/one_book.html/', views.onebook, name="books.one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links/', views.links, name="books.links"),
    path('html5/text/formatting/', views.text, name="books.text"),
    path('html5/listing/', views.listing, name="books.listing"),
    path('html5/tables/', views.tables, name="books.tables"),
    path('search/', views.search, name="books.search"),
    path('simple/query/', views.simple_query, name="books.simpleQuery"),
    path('complex/query/', views.complex_query, name="books.complexQuery"),
    path('addBook/', views.add_book, name="books.addBook")

]

