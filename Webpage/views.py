from django.shortcuts import redirect, render
from .models import Drink

# Create your views here.

def home(request):

    to_display = {
        "drinks" : Drink.objects.all()
    }

    return render(request, 'Webpage/home.html', to_display)

def addDrink(request):

    if request.method == "POST":
        drink = Drink()
        drink.purchaser = request.POST["purchaser"]
        drink.bar = request.POST["bar"]
        drink.date = request.POST["date"]

        if len(drink.purchaser) > 0 and len(drink.bar) > 0 and len(drink.purchaser) > 0:
            drink.save()

    return redirect("home")
