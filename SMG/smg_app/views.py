from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout as logout_user
from django.contrib.auth.models import User
from .models import Friend
from .forms import ExtendedUserCreationForm, UserProfileForm, UpdateProfileForm, UpdateUserForm
from .connection_weight import connections

# Create your views here.


# def home(request):
#     return render(request, 'loginPage.html')


def register(request):
    if request.method == "POST":
        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            friend = Friend(current_user=user)
            friend.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            messages.success(request, "Registration successful!")
            return redirect('LoginPage')
    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()

    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'signUp.html', context)


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
    return redirect("LoginPage")


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        users = User.objects.all().filter(username__contains=searched).filter(is_staff=0)
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()
        return render(request, 'search.html', {'searched': searched, 'users': users,
                                               'current_user': request.user, 'friends': friends})
    else:
        return render(request, 'search.html', {})


def profile(request, username=None):

    # If no such user exists raise 404
    try:
        if username:
            user = User.objects.get(username=username)
        else:
            user = request.user
    except:
        raise Http404

    current_user = request.user
    view_user = User.objects.get(username=username)
    friend = Friend.objects.get(current_user=view_user)
    friends = friend.users.all()
    # Flag that determines if we should show editable elements in template
    editable = False
    # Handling non authenticated user for obvious reasons
    if request.user.is_authenticated and request.user == user:
        editable = True

    context = {'user': user, 'friends': friends, 'current_user': current_user}
    template = 'profile.html'
    return render(request, template, context)


def profile_update(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, instance=request.user.account)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile', username=request.user.username)
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.account)

    context = {'user_form': user_form, 'profile_form': profile_form, 'user': request.user}

    return render(request, 'editProfile.html', context)

def change_friend(request, operation, username):
    friend = User.objects.get(username=username)
    if operation == 'add':
        Friend.add_friend(request.user, friend)
        Friend.add_friend(friend, request.user)
        return redirect("search")
    elif operation == 'remove':
        Friend.remove_friend(request.user, friend)
        Friend.remove_friend(friend, request.user)
        return redirect("profile", username=friend)

    return redirect("LoginPage")


def connection_page(request):
    possible_friends = connections(request.user)
    return render(request, 'connectionsPage.html', {'possible_friends' : possible_friends, 'user': request.user})

