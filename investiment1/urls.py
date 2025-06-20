from django.urls import path
from investiment1.views import my_portfolio, my_status, my_newspaper

urlpatterns = [
    path("", my_portfolio),
    path("status/", my_status),
    path("newspaper/", my_newspaper),
]