from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from Formpractise.forms import studentform


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = studentform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = studentform()
    form = studentform()
    return render(request,'home.html',{"form":form})
def all_students(request):
    students = Student.objects.all()
    return render(request,'allstudents.html',{"data":students})
def student(request, stud_id):
    studentt = Student.objects.get(pk=stud_id)
    return render(request,'student.html',{"student":studentt})


def delete(request,stud_id):
    student_to_del = get_object_or_404(Student,pk=stud_id)
    student_to_del.delete()
    return redirect('allstudents')