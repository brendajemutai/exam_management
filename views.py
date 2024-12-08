from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Student, Result, Parent
def home(request):
    return render(request, 'exam/home.html')

def teacher_dashboard(request):
    return render(request, 'exam/teacher.html')

def student_dashboard(request):
    return render(request, 'exam/student.html')

def parent_dashboard(request):
    return render(request, 'exam/parent.html')

def index(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})

def teacher(request):
    if request.method == 'POST':
        student_id = request.POST['student_id']
        subject = request.POST['subject']
        score = request.POST['score']
        student, created = Student.objects.get_or_create(id=student_id)
        Result.objects.create(student=student, subject=subject, score=score)
        return redirect('teacher')
    students = Student.objects.all()
    return render(request, 'teacher.html', {'students': students})

def student(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'student.html', {'student': student})

def parent(request, student_id):
    student = Student.objects.get(id=student_id)
    parent = student.parent if hasattr(student, 'parent') else None
    return render(request, 'parent.html', {'student': student, 'parent': parent})
