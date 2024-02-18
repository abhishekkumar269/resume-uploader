from django.shortcuts import render

# Create your views here.

def Resumeform(request):
    return render(request,'myapp/home.html')