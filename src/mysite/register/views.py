from django.shortcuts import render, redirect
from .forms import RegisterForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UpdateProfileForm, UpdateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Create your views here.
def register(response):
    if response.user.is_authenticated:
        return redirect("home")

    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")
        else:
            return render(response, "register/register.html", {'form': form})
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form":form})


def loginview(request):
    # print("user is ---------------", request.user)
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        # if request.user.is_authenticated:
        #     return redirect("home")
        # form = UserLoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/profile")
        else:
            context = {'error': 'Wrong credintials'}  # to display error?
            return render(request, 'registration/login.html', {'context': context})
    else:
        form = UserLoginForm()

    return render(request, "registration/login.html", {'form': form})

# def admin_login(request):
#     if request.user.is_authenticated:
#         return redirect(reverse("admin")) 
#     if request.method == 'POST':
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request,username = username, password = password)
#         if user is not None:
#             if(user.is_superuser):
#                 auth_login(request, user)
#                 return redirect(reverse("dashboard"))
#             else:
#                 messages.info(request, "invalid credentials")
#             return redirect(reverse("admin"))
         
#     return render(request,'login.html') 

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('/profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'mainapp/profile.html', {'user_form': user_form, 'profile_form': profile_form})