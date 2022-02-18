from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


# Create your views here.

def home(request):
    return render(request, 'loginPage.html')


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
        messagess.success(request, "your account has been  successfully created")
        # redirect the login page
        return redirect("login")
    return render(request, 'signUp.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            fName = user.first_name
            return render(request, "loginPage.html", {'fName': fName})
        else:
            messagess.error(request, 'Bad Credential')
            return redirect('home')

    return render(request, 'loginPage.html')
