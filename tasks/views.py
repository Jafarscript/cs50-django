from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
tasks = ['buy car', 'marry', 'buy house']

# def index(request):
#     return HttpResponse("Hello Jafar!")


def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    return render(request, "tasks/add.html")