from django.core.paginator import Paginator
from django.db.models import Q
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
    paginator = Paginator(students,25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'allstudents.html',{"page_obj":page_obj})
def student(request, stud_id):
    studentt = Student.objects.get(pk=stud_id)
    return render(request,'student.html',{"student":studentt})


def delete(request,stud_id):
    student_to_del = get_object_or_404(Student,pk=stud_id)
    student_to_del.delete()
    return redirect('allstudents')
def search_student(request):
    search = request.GET.get('search')
    filtered = Student.objects.filter(Q(first_name__icontains=search)|Q(last_name__icontains=search))
    return render(request,'allstudents.html',{"page_obj":filtered})