# from django.shortcuts import render

from django.shortcuts import render
from . models import Place
# Create your views here.


def demo(request):
    obj = Place.objects.all()
    return render(request, "index.html", {"result": obj})


# def addition(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     result = x+y
#     multiplication = x * y
#     division = x/y
#     subtraction = x-y
#     return render(request, "about.html", {"res": result, "mul": multiplication, "div": division, "sub": subtraction})
