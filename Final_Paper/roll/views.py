# roll/views.py
from django.shortcuts import render, get_object_or_404
from .models import Student

# Home page: display all students
def studentinfo(request):
    students = Student.objects.all()
    return render(request, 'roll/studentinfo.html', {'students': students})

# Welcome page
def welcome(request):
    return render(request, 'roll/welcome.html')

# Student search
def student_search(request):
    query = request.GET.get('q')
    students = Student.objects.filter(stuname__icontains=query) if query else []
    found = students.exists()
    return render(request, 'roll/student_search.html', {'students': students, 'query': query, 'found': found})

# Student individual info
def stuinformation(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'roll/student_info.html', {'student': student})
