from django import http
from django.shortcuts import render, redirect
from datetime import datetime
from myapp.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request , "index.html")

def loginuser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request , "login.html")

    return render(request , "login.html")

def logoutuser(request):
    logout(request)
    return redirect("/login")

def about(request):
    return render(request , "about.html")

def services(request):
    return render(request , "services.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Successfully Submitted!')
    return render(request , "contact.html")

def req(request):
    return render(request , "req.html")

def vac(request):
    return render(request , "vaca.html")
def min(request):
    return render(request , "min.html")

def meterbox(request):
    return render(request , "meterbox.html")

def ubr(request):
    return render(request , "ubr.html")

def wifi(request):
    return render(request , "wifi.html")

def esc(request):
    return render(request , "esc.html")

def trans(request):
    return render(request , "trans.html")

def rrh(request):
    return render(request , "rrh.html")

def antena(request):
    return render(request , "antena.html")

def mrn(request):
    return render(request , "mrn.html")

def upload(request):
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name , uploaded_file)
        messages.success(request, 'Successfully Submitted!')
    return render(request, "upload.html")
