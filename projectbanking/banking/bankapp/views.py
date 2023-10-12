from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
def index(request):
    return render(request,'index.html')

def login(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('login')
            else:
                return redirect('newpage')

        return render(request, "login.html")

def register(request):

    if request.method =='POST':
        username = request.POST['username']
        password= request.POST['password']
        cpassword = request.POST['password1']
        user = User.objects.create_user(username=username,password=password)
        user.save();
        return redirect('login')

    return render(request, "register.html")

def newpage(request):
    if request.GET.get('Submit')=='Submit':
        return redirect('form')

    return render (request,'newpage.html')
def form(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        user = User.objects.create_user(username=username,email=email)
        user.save();
        messages.info(request,"Application submitted successfully")
    return render (request,'form.html')



















