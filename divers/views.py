from django.shortcuts import render
from .functions import multip_by_5
# Create your views here.
weekdays= [
        "lundi",
        "mardi",
        "mercredi",
        "jeudi",
        "vendredi",
        "samedi",
        "dimanche"
    ]
def home_view(request):
    
   

    context = {
        "test" : "Ceci est un test",
        "multi8":multip_by_5(55),
        "weekdays":weekdays
    
    }
    #import pudb;pu.db()

    return render(request, "divers/home_page.html",context=context)

def about_view(request):
    return render(request, "divers/about_page.html")

def qui_somme_nous_view(request):
    return render(request, "divers/qui_somme_nous_page.html")