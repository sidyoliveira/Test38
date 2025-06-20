from django.http import HttpResponse


def my_portfolio(request):
    return HttpResponse("portfolio")


def my_status(request):
    return HttpResponse("status")


def my_newspaper(request):
    return HttpResponse("newspaper")

