from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignInForm, UpdateForm, ChangePasswordForm


def Home(request):
    if request.user.is_authenticated:
        return redirect("Detail")
    else:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "You are successfully Logged In")
                return redirect("Detail")
            else:
                messages.success(request, "Something went wrong Please Try again")
                return redirect("Home")
    return render(request, "Home.html", {})


def Detail(request):
    if request.user.is_authenticated:
        record = User.objects.filter(id=request.user.id)
        return render(request, "Detail.html", {"record": record.values()})
    else:
        messages.success(request, "You have to Logged In to view this Page")
        return redirect("Home")


def Register(request):
    if request.user.is_authenticated:
        return redirect("Detail")
    else:
        form = SignInForm()
        if request.method == "POST":
            form = SignInForm(request.POST)

            if form.is_valid():
                form.save()
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password1"]
                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    messages.success(request, "You are successfully Signed In")
                    return redirect("Detail")
                else:
                    messages.success(request, "Something went wrong Please Try again")
                    return redirect("Register")

        return render(request, "Register.html", {"form": form})


def Logout_user(request):
    logout(request)
    messages.success(request, "You are sucessfully Logged out")
    return redirect("Home")


def Delete(request):
    if request.user.is_authenticated:
        record = User.objects.filter(id=request.user.id)
        record.delete()
        messages.success(request, "You have successfully Delected the Account")
        return redirect("Home")
    else:
        messages.success(request, "You have to be Logged In")
        return redirect("Home")


def Update(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = UpdateForm(request.POST, instance=request.user)

            if form.is_valid():
                form.save()
                messages.success(request, "You have successfully Updated your Account")
                return redirect("Detail")
            else:
                messages.success(request, "Something went wrong Please Try again")
                return render(request, "Update.html", {"form": form})
        else:
            form = UpdateForm(instance=request.user)
            return render(request, "Update.html", {"form": form})
    else:
        messages.success(request, "You have to be Logged In")
        return redirect("Home")


def UpdatePassword(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ChangePasswordForm(data=request.POST, user=request.user)

            if form.is_valid():
                form.save()
                messages.success(request, "You have successfully Updated your Account")
                update_session_auth_hash(request, form.user)
                return redirect("Detail")
            else:
                messages.success(request, "Something went wrong Please Try again")
                return render(request, "UpdatePassword.html", {"form": form})
        else:
            form = ChangePasswordForm(user=request.user)
            return render(request, "UpdatePassword.html", {"form": form})
    else:
        messages.success(request, "You have to be Logged In")
        return redirect("Home")
