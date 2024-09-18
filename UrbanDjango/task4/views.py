from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def games_list(request):
    context = {
        'games': ['Atomic Heart ', 'Cyberpunk 2077 ', 'PayDay 2 '],
    }
    return render(request, 'games.html', context)


def cart_view(request):
    return render(request, 'cart.html')


def main_page(request):
    name = 'Главная страница'

    return render(request, 'platform.html')
