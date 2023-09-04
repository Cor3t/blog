from django.shortcuts import render

def home(request):
    return render(request, 'Home.html')

def CSS(request):
  return render(request,'base_layout.html')