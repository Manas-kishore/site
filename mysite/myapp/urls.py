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
    path("min", views.min, name="min"),
    path("login", views.loginuser, name="login"),
    path("logout", views.logoutuser, name="logout"),
    path("meterbox", views.meterbox, name="meterbox"),
    path("ubr", views.ubr, name="ubr"),
    path("wifi", views.wifi, name="wifi"),
    path("esc", views.esc, name="esc"),
    path("trans", views.trans, name="trans"),
    path("rrh", views.rrh, name="rrh"),
    path("antena", views.antena, name="antena"),
    path("mrn", views.mrn, name="mrn"),
    path("upload", views.upload, name="upload"),
]
