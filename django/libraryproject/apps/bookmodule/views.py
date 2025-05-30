from django.shortcuts import get_object_or_404, redirect, render
from .models import Book
from apps.usermodule.models import Student, Student2, Card, Course, Department
from django.db.models import Q, Avg, Count, Max, Sum, Min
from .forms import BookForm


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
    


def lab9_1(request):
    studentNum = Student2.objects.values('department__name').annotate(student_count = Count('id'))
    if studentNum.exists():
        return render(request, 'bookmodule/lab9_1.html', {'studentNum': studentNum})
    else:
        return render(request, 'bookmodule/index.html')
    


def lab9_3(request):
    oldest_ids = Student2.objects.values('department_id').annotate(min_id=Min('id'))

    studentName = Student2.objects.filter(
        id__in=[item['min_id'] for item in oldest_ids]
    ).select_related('department')

    if studentName.exists():
        return render(request, 'bookmodule/lab9_3.html', {'studentName': studentName})
    else:
        return render(request, 'bookmodule/index.html')

    


def lab9_2(request):
    courses = Course.objects.annotate(student_count=Count('student2')).values('title', 'student_count')
    
    if courses.exists():
        return render(request, 'bookmodule/lab9_2.html', {'courses': courses})
    else:
        return render(request, 'bookmodule/index.html')
    


def lab9_4(request):
    departments = Department.objects.annotate(student_count=Count('student2')).filter(student_count__gt=2).order_by('-student_count')
    return render(request, 'bookmodule/lab9_4.html', {'departments': departments})

    
def listbooksPt1(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/listbooksPt1.html', {'books': books})


def addbookPt1(request):
    if request.method == 'POST':
        Book.objects.create(
            title=request.POST['title'],
            author=request.POST['author'],
            price=request.POST['price'],
            edition=request.POST['edition']
        )
        return redirect('books.listbooksPt1')
    return render(request, 'bookmodule/addbookPt1.html')

def editbookPt1(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.price = request.POST['price']
        book.edition = request.POST['edition']
        book.save()
        return redirect('books.listbooksPt1')
    return render(request, 'bookmodule/addbookPt1.html', {'book': book})

def deletebookPt1(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return render(request,'bookmodule/deleteBook.html', {'id':id})

def listbooksPt2(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/listbooksPt2.html', {'books': books})

def addbookPt2(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books.listbooksPt2')
    else:
        form = BookForm()
    return render(request, 'bookmodule/add_edit_bookPt2.html', {'form': form})

def editbookPt2(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books.listbooksPt2')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/add_edit_bookPt2.html', {'form': form})

def deletebookPt2(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('books.listbooksPt2')

