from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns = [
    path('',views.home),
    path('contact/',views.contact),
    path('customer/',views.customer)


]