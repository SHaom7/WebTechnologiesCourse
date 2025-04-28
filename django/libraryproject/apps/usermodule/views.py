from django.shortcuts import render, get_object_or_404, redirect
from apps.usermodule.models import Student, Address, Student3
from django.db.models import Q, Avg, Count, Max, Sum, Min
from .forms import StudentForm, AddressForm, Student3Form

# Create your views here.

def task7(request):
    city_stats = Student.objects.values('address__city').annotate(student_count=Count('id')).order_by('-student_count')
    return render(request, 'usermodule/task7.html', {'city_stats': city_stats})


def list_students(request):
    students = Student.objects.all()
    return render(request, 'usermodule/list_students.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users.list_students')
    else:
        form = StudentForm()
    return render(request, 'usermodule/add_edit_student.html', {'form': form})

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

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('users.list_students')

# CRUD for Student3

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
    return render(request, 'usermodule/add_edit_student.html', {'form': form})

def edit_student3(request, id):
    student = get_object_or_404(Student3, id=id)
    if request.method == 'POST':
        form = Student3Form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('users.list_students3')
    else:
        form = Student3Form(instance=student)
    return render(request, 'usermodule/add_edit_student.html', {'form': form})

def delete_student3(request, id):
    student = get_object_or_404(Student3, id=id)
    student.delete()
    return redirect('users.list_students3')

