from django.shortcuts import render
from django.shortcuts import render,redirect
from app.models import Baby

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def team(request):
    return render(request,'team.html')


def why(request):
    return render(request,'why.html')

def login(request):
    return render(request,'login.html')


def adminlogin(request):
    return render(request,'adminlogin.html')

def testmonial(request):
  return render(request,'testmonial.html')

def add(request):
    a = request.POST['Name']
    b = request.POST['Email']
    c = request.POST['Password']
    d = request.POST['ConfirmPassword']
    e = Baby(Name=a,Email=b,Password=e,ConfirmPassword=d)
    return render(request,'index.html')
   
