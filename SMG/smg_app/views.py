from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect

# Create your views here.

# def home(request):
#     return render(request, 'loginPage.html')


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
        return redirect("Login_Page")
    return render(request, 'signUp.html')


def Login_Page(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            uName = user.username
            return render(request, "loginPage.html", {'uName': uName})
        else:
            # messages.error(request, 'Bad Credential')
            return redirect('signup')

    return render(request, 'loginPage.html')
