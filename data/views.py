from django.shortcuts import render

from .models import Student, Teacher

def view_data(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    return render(request, 'data_visualization/data_view.html', {'students': students, 'teachers': teachers})

# Create your views here.
