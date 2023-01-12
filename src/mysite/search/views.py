from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def search(request):
    if request.method == "POST":
        content = request.POST.get('content')
        