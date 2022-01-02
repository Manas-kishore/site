from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.index, name='myapp'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='Our Contact'),
    path("services", views.services, name='Our Services'),
    path("req", views.req, name="Our Requirements"),
    path("vacancy" , views.vac, name="Vacancy"),
    path("min", views.min, name="min")
]
