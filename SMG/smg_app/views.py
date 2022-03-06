from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout as logout_user
from django.contrib.auth.forms import UserCreationForm
from .models import Account


# Create your views here.

def home(request):
    return render(request, 'loginPage.html')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            messages.success(request, "Registration successful!")
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'signUp.html', {'form': form, })


def login(request):
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


def logout(request):
    logout_user(request)
    return redirect("login")


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        users = Account.objects.filter(name__contains=searched)
        return render(request, 'search.html', {'searched': searched,
                                               'users': users, })
    else:
        return render(request, 'search.html', {})


def profile(request):
    if request.method == "POST":
        user = request.POST['user']
        user_profile = Account.objects.filter(name__exact=user)
        return render(request, 'profile.html', {'user': user, 'user_profile': user_profile})
    else:
        return render(request, 'profile.html', {})
