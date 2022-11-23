from django.urls import path
from .views import home_view ,about_view, qui_somme_nous_view

urlpatterns = [
    path("",home_view,name="home"),
    path("about/",about_view,name="about"),
    path("qui_somme_nous/",qui_somme_nous_view,name="qui_somme_nous")
]
