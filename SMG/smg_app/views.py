from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout as logout_user
from django.contrib.auth.models import User
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
            return redirect('loginPage')
    else:
        form = UserCreationForm()

    return render(request, 'signUp.html', {'form': form, })


def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            uName = user.username
            return render(request, "search.html", {'uName': uName})
        else:
            # messages.error(request, 'Bad Credential')
            return redirect('register')
    return render(request, 'loginPage.html')


def logout(request):
    logout_user(request)
    return redirect("loginPage")


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        users = User.objects.all().filter(username__contains=searched).filter(is_staff=0)
        return render(request, 'search.html', {'searched': searched,
                                               'users': users,})
    else:
        return render(request, 'search.html', {})


def profile (request, username):
    # If no such user exists raise 404
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404

    # Flag that determines if we should show editable elements in template
    editable = False
    # Handling non authenticated user for obvious reasons
    if request.user.is_authenticated() and request.user == user:
        editable = True

    context = locals()
    template = 'profile.html'
    return render (request, template, context)


#def profile(request):
#    if request.method == "POST":
#        user = request.POST['user']
#        user_profile = Account.objects.filter(name__exact=user)
#        return render(request, 'profile.html', {'user':user, 'user_profile': user_profile})
#    else:
#        return render(request, 'profile.html', {})
