from django.shortcuts import render, redirect

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