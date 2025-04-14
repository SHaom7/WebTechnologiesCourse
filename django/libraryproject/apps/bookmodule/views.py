from django.shortcuts import render
from .models import Book
from apps.usermodule.models import Student, Student2, Card, Course, Department
from django.db.models import Q, Avg, Count, Max, Sum, Min


def index(request):
    return render(request, "bookmodule/index.html")
 
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
 
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
 
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def onebook(request):
    return render(request, 'bookmodule/one_book.html')

def links(request):
    return render(request, 'bookmodule/links.html')

def text(request):
    return render(request, 'bookmodule/text.html')

def listing(request):
    return render(request, 'bookmodule/listing.html')

def tables(request):
    return render(request, 'bookmodule/tables.html')

def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True
            
            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})
    return render(request, 'bookmodule/search.html')

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def add_book(request):
    mybook = Book.objects.create(
        title='Gaming in 2025',
        author='QU coc',
        price=55.00,
        edition=4
    )
    mybook.save()
    return render(request, 'bookmodule/add_book.html', {'message': 'Book Added Successfully!'})


def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') 
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})



def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    

def task1(request):
    mybooks = Book.objects.filter(Q(price__lte=80)) 
    if mybooks.exists():
        return render(request, 'bookmodule/task1.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    

def task2(request):
    books = Book.objects.filter(
        Q(edition__gt=3) & (Q(title__icontains='co') | Q(author__icontains='co'))
    )
    if books.exists():
        return render(request, 'bookmodule/task2.html', {'books': books})
    else:
        return render(request, 'bookmodule/index.html')
    

def task3(request):
    books = Book.objects.filter(
        Q(edition__lte=3) & ~(Q(title__icontains='co') | Q(author__icontains='co'))
    )
    if books.exists():
        return render(request, 'bookmodule/task3.html', {'books': books})
    else:
        return render(request, 'bookmodule/index.html')
    

def task4(request):
    books = Book.objects.order_by('title')
    if books.exists():
        return render(request, 'bookmodule/task4.html', {'books': books})
    else:
        return render(request, 'bookmodule/index.html')
    

def task5(request):
    vals = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        average_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price'))
    if vals:
        return render(request, 'bookmodule/task5.html', {'vals': vals})
    else:
        return render(request, 'bookmodule/index.html')
    

def task7(request):
    city_stats = Student.objects.values('address__city').annotate(student_count=Count('id')).order_by('-student_count')
    return render(request, 'usermodule/task7.html', {'city_stats': city_stats})

def lab9_1(request):
    studentNum = Student2.objects.values('department__name').annotate(student_count = Count('id')).order_by('-student_count')
    if studentNum.exists():
        return render(request, 'bookmodule/lab9_1.html', {'studentNum': studentNum})
    else:
        return render(request, 'bookmodule/index.html')
    


def lab9_2(request):
    books = Book.objects.order_by('title')
    if books.exists():
        return render(request, 'bookmodule/task4.html', {'books': books})
    else:
        return render(request, 'bookmodule/index.html')
    


def lab9_3(request):
    books = Book.objects.order_by('title')
    if books.exists():
        return render(request, 'bookmodule/task4.html', {'books': books})
    else:
        return render(request, 'bookmodule/index.html')
    


def lab9_4(request):
    books = Book.objects.order_by('title')
    if books.exists():
        return render(request, 'bookmodule/task4.html', {'books': books})
    else:
        return render(request, 'bookmodule/index.html')
    



    

