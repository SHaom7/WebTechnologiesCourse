from django.shortcuts import render
from apps.usermodule.models import Student, Address
from django.db.models import Q, Avg, Count, Max, Sum, Min
# Create your views here.

def task7(request):
    city_stats = Student.objects.values('address__city').annotate(student_count=Count('id')).order_by('-student_count')
    return render(request, 'usermodule/task7.html', {'city_stats': city_stats})