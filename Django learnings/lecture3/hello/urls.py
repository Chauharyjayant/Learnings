from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("jayant",views.jayant, name="jayant"),
    path("<str:name>",views.input, name="input")
]
