from django.shortcuts import render, HttpResponse
from .models import User


# Create your views here.
def home(request):
    return render(request, "home.html")


def users(request):
    users = User.objects.all()
    return render(request, "users.html", {
        "users": users,
    })
