from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList
from django.shortcuts import render
from .forms import CreateNewList
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
# from register.views import profile
from django.contrib import messages


@login_required
def index(response, id):
    ls = ToDoList.objects.get(id=id)
    if ls in response.user.todolist.all():
        if response.method == "POST":
            print(response.POST)
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c"+str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    
                    item.save()

            elif response.POST.get("newItem"):
                txt = response.POST.get("new")

                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete = False)
                else:
                    print("invalid!")

        return render(response, "mainapp/list.html", {"ls":ls})
    return render(response, "mainapp/view.html", {})

@login_required
def home(response):
    return render(response, "mainapp/home.html", {})


@login_required
def create(response):
    if response.method == "POST":
        n = response.POST.get("new-task-input")
        print(response.POST, "----------------------")
        t = ToDoList(name=n)
        t.save()
        response.user.todolist.add(t)

    return render(response, "mainapp/create.html", {})


@login_required
def view(response):
    if response.method == 'POST':
        n = response.POST.get("new-task-input")
        print(response.POST, "----------------------")
        t = ToDoList(name=n)
        t.save()
        response.user.todolist.add(t)

    # form = CreateNewList()
    return render(response, "mainapp/view.html")


# @login_required
# def profile(request):
#     return render(request, 'mainapp/profile.html')


# @login_required
class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'mainapp/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-profile')

    # def form_valid(self, form):
    #     print("success-----------------------------------")
    #     messages.success(self.request, 'Your password has been changed.')
    #     return super().form_valid(form)