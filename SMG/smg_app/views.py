from datetime import datetime
from json import loads

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as logout_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import Http404, HttpResponseNotFound, HttpResponseNotAllowed, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import ensure_csrf_cookie

from .connection_weight import connections
from .forms import (
    ExtendedUserCreationForm, UpdateProfileForm, UpdateUserForm,
    UserProfileForm,
)
from .models import Friend, FriendRequest, Message


# Create your views here.


# def home(request):
#     return render(request, 'loginPage.html')


def register(request):
    if request.method == "POST":
        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        print("test")
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.role = 0
            print(profile)
            profile.save()

            friend = Friend(current_user=user)
            friend.save()

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect("connection_page")
    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()

    context = {"form": form, "profile_form": profile_form}
    return render(request, "signUp.html", context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect("user_profile")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            uName = user.username
            return redirect("profile", username=uName)
        else:
            # messages.error(request, 'Bad Credential')
            return redirect("register")
    return render(request, "loginPage.html")


@login_required()
def logout(request):
    logout_user(request)
    return redirect("login")


@login_required()
def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        users = User.objects.all().filter(username__contains=searched).filter(is_staff=0)
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()
        return render(
            request, "search.html", {
                "searched": searched, "users": users,
                "current_user": request.user, "friends": friends,
            },
        )
    else:
        return render(request, "search.html", {"current_user": request.user})


@login_required()
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
    view_user = User.objects.get(username=user.username)
    friend = Friend.objects.get(current_user=view_user)
    friends = friend.users.all()
    # Flag that determines if we should show editable elements in template
    # Handling non authenticated user for obvious reasons
    if request.user.is_authenticated and request.user == user:
        pass

    context = {"user": user, "friends": friends, "current_user": current_user}
    template = "profile.html"
    return render(request, template, context)


@login_required()
def profile_update(request):
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, instance=request.user.account)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("profile", username=request.user.username)
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.account)

    context = {"user_form": user_form, "profile_form": profile_form, "user": request.user}

    return render(request, "editProfile.html", context)


@login_required()
def change_friend(request, operation, username):
    friend = User.objects.get(username=username)
    if operation == "add":
        f_request = FriendRequest.objects.get(sender=friend, receiver=request.user)
        Friend.add_friend(request.user, friend)
        Friend.add_friend(friend, request.user)
        f_request.delete()
        return redirect("friendPage", username=request.user)
    elif operation == "remove":
        Friend.remove_friend(request.user, friend)
        Friend.remove_friend(friend, request.user)
        return redirect("friendPage", username=request.user)

    return redirect("login")


@login_required()
def connection_page(request):
    possible_friends = connections(request.user)

    page = request.GET.get("page", 1)

    paginator = Paginator(possible_friends, 4)
    try:
        display_friends = paginator.page(page)
    except PageNotAnInteger:
        display_friends = paginator.page(1)
    except EmptyPage:
        display_friends = paginator.page(paginator.num_pages)

    return render(
        request, "connectionsPage.html",
        {"possible_friends": display_friends, "user": request.user},
    )


@login_required()
def friend_request(request, username):
    request.user
    recipient = User.objects.get(username=username)
    model = FriendRequest.objects.get_or_create(sender=request.user, receiver=recipient)

    possible_friends = connections(request.user)
    page = request.GET.get("page", 1)
    paginator = Paginator(possible_friends, 4)
    try:
        display_friends = paginator.page(page)
    except PageNotAnInteger:
        display_friends = paginator.page(1)
    except EmptyPage:
        display_friends = paginator.page(paginator.num_pages)

    return render(
        request, "connectionsPage.html",
        {"possible_friends": display_friends, "user": request.user},
    )


@login_required()
def delete_request(request, operation, username):
    p_friend = User.objects.get(username=username)
    if operation == "Sender_deleting":
        f_request1 = FriendRequest.objects.get(sender=request.user, receiver=p_friend)
        f_request1.delete()
    elif operation == "Receiver_deleting":
        f_request2 = FriendRequest.objects.get(sender=p_friend, receiver=request.user)
        f_request2.delete()
        return redirect("friendPage", username=request.user)

    return redirect("friendPage", username=request.user)


@login_required()
def friendPage(request, username=None):
    try:
        if username:
            user = User.objects.get(username=username)
        else:
            user = request.user
    except:
        raise Http404

    friend = Friend.objects.get(current_user=user)
    friends = friend.users.all()
    f_requests = FriendRequest.objects.filter(receiver=user)
    req_outgoing = FriendRequest.objects.filter(sender=user)

    context = {"user": user, "friends": friends, "requests": f_requests, "outgoing": req_outgoing}
    template = "friendPage.html"
    return render(request, template, context)


@login_required()
@ensure_csrf_cookie
def message(request, username: str):
    try:
        User.objects.get(username=username)
    except User.DoesNotExist:
        return HttpResponseNotFound()

    usernames = [request.user.username, username]
    ctx = {
        "username": username,
        "messages": Message.objects.filter(
            sender__username__in=usernames,
            receiver__username__in=usernames,
        ).order_by('-time'),
    }

    return render(request, "message.html", ctx)


@login_required()
def send_message(request):
    if request.method != "POST":
        return HttpResponseNotAllowed()

    body = loads(request.body)
    username = body.get("username", "")
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return HttpResponseNotFound()
    contents = body.get("contents", "uh oh!")
    message = Message(
        sender=request.user,
        receiver=user,
        contents=contents,
        time=datetime.now(),
    )
    message.save()

    return HttpResponse(status=200)
