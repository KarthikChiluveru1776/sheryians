from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'Home.html')

def courses(request):
    return render(request,'Courses.html')

def bootcamp(request):
    return render(request,'bootcamp.html')

def requestcallback(request):
    return render(request,'RequestCallBack.html')

