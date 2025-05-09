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
    path('addBook/', views.add_book, name="books.addBook"),
    path('lab8/task1/', views.task1, name="books.task1"),
    path('lab8/task2/', views.task2, name="books.task2"),
    path('lab8/task3/', views.task3, name="books.task3"),
    path('lab8/task4/', views.task4, name="books.task4"),
    path('lab8/task5/', views.task5, name="books.task5"),
    path('lab9/task1/', views.lab9_1, name="books.lab9_1"),
    path('lab9/task2/', views.lab9_2, name="books.lab9_2"),
    path('lab9/task3/', views.lab9_3, name="books.lab9_3"),
    path('lab9/task4/', views.lab9_4, name="books.lab9_4"),
    path('lab10_part1/listbooks/', views.listbooksPt1, name="books.listbooksPt1"),
    path('lab10_part1/addbook/', views.addbookPt1, name="books.addbookPt1"),
    path('lab10_part1/editbook/<id>/', views.editbookPt1, name="books.editbookPt1"),
    path('lab10_part1/deletebook/<id>/', views.deletebookPt1, name="books.deletebookPt1"),
    path('lab10_part2/listbooks/', views.listbooksPt2, name="books.listbooksPt2"),
    path('lab10_part2/addbook/', views.addbookPt2, name="books.addbookPt2"),
    path('lab10_part2/editbook/<id>/', views.editbookPt2, name="books.editbookPt2"),
    path('lab10_part2/deletebook/<id>/', views.deletebookPt2, name="books.deletebookPt2"),

]

