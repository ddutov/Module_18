from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def games_list(request):
    return render(request, 'games.html')


def cart_view(request):
    return render(request, 'cart.html')


def main_page(request):
    return render(request, 'platform.html')
