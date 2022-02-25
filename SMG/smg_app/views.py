from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as login_user, logout as logout_user
from .models import Account


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fName = request.POST['fName']
        lName = request.POST['lName']
        email = request.POST['email']
        id_password = request.POST['id_password']
        con_password = request.POST['con_password']
        # user validation
        if user.object.filter(username=username):
            messages.error(request, "username already exist! please try some other user name")
            return redirect('home')
        if user.object.filter(email=email):
            messages.error(request, "Email already register please use different email")
            return redirect('home')
        if len(username) > 10:
            messages.error(request, "username must be under 10 charcters")
            return redirect('home')
        if con_password != id_password:
            messages.error(request, "passwords didn't match!")
        myuser = user.object.create_user(username, email, id_password)
        myuser.first_name = fName
        myuser.last_name = lName
        myuser.save()
        messages.success(request, "your account has been  successfully created")
        # redirect the login page
        return redirect("login")
    return render(request, 'signUp.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            login_user(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Bad Credential')
            return render(request, "loginPage.html")

    return render(request, 'loginPage.html')


def logout(request):
    logout_user(request)
    return redirect("login")

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        users = Account.objects.filter(name__contains=searched)
        return render(request, 'search.html', {'searched': searched,
                                               'users': users,})
    else:
        return render(request, 'search.html', {})
