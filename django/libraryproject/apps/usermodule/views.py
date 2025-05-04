from django.shortcuts import render, get_object_or_404, redirect
from apps.usermodule.models import Student, Student3, Product
from django.db.models import  Count
from .forms import StudentForm, Student3Form, ProductForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def task7(request):
    city_stats = Student.objects.values('address__city').annotate(student_count=Count('id')).order_by('-student_count')
    return render(request, 'usermodule/task7.html', {'city_stats': city_stats})

@login_required
def list_students(request):
    students = Student.objects.all()
    return render(request, 'usermodule/list_students.html', {'students': students})

@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users.list_students')
    else:
        form = StudentForm()
    return render(request, 'usermodule/add_edit_student.html', {'form': form})

@login_required
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('users.list_students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'usermodule/add_edit_student.html', {'form': form})

@login_required
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('users.list_students')


def list_students3(request):
    students = Student3.objects.all()
    return render(request, 'usermodule/list_students3.html', {'students': students})

def add_student3(request):
    if request.method == 'POST':
        form = Student3Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users.list_students3')
    else:
        form = Student3Form()
    return render(request, 'usermodule/add_edit_student2.html', {'form': form})

def edit_student3(request, id):
    student = get_object_or_404(Student3, id=id)
    if request.method == 'POST':
        form = Student3Form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('users.list_students3')
    else:
        form = Student3Form(instance=student)
    return render(request, 'usermodule/add_edit_student2.html', {'form': form})

def delete_student3(request, id):
    student = get_object_or_404(Student3, id=id)
    student.delete()
    return redirect('users.list_students3')

def list_products(request):
    products = Product.objects.all()
    return render(request, 'usermodule/list_products.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users.list_products')
    else:
        form = ProductForm()
    return render(request, 'usermodule/add_product.html', {'form': form})

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('users.list_products') 

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered!')
            return redirect('users.login')
        else:
            messages.error(request, 'Registration failed. Please check the form.')
    else:
        form = UserCreationForm()
    return render(request, 'usermodule/register.html', {'form': form})
