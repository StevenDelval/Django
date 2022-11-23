from django.shortcuts import render
from .functions import multip_by_5
# Create your views here.

def home_view(request):
    
    weekdays= [
        "lundi",
        "mardi",
        "mercredi",
        "jeudi",
        "vendredi",
        "samedi",
        "dimanche"
    ]

    context = {
        "test" : "Ceci est un test",
        "multi8":multip_by_5(55),
        "weekdays":weekdays
    
    }

    return render(request, "divers/home_page.html",context=context)