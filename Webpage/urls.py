from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_drink', views.addDrink, name="add_drink")
]