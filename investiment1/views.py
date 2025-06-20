#from django.http import HttpResponse
from django.shortcuts import render


def my_portfolio(request):
    return render(request, "investment1/pages/my_portfolio.html")


def my_status(request):
    return render(request, "investment1/pages/my_status.html")


def my_newspaper(request):
    return render(request, "investment1/pages/my_newspaper.html")

