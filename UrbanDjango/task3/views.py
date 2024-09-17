from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
# def games_list(request):
#     return render(request, 'games.html')

def games_list(request):
    game_1 = 'Atomic Heart '
    game_2 = 'Cyberpunk 2077 '
    game_3 = 'PayDay 2 '
    context = {
        'game_1': game_1,
        'game_2': game_2,
        'game_3': game_3,
    }
    return render(request, 'games.html', context)



def cart_view(request):
    return render(request, 'cart.html')


def main_page(request):
    return render(request, 'platform.html')
