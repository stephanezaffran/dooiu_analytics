from django.shortcuts import render
from dooiu_analytics.settings import BASE_DIR
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Data
from login.models import User
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')


# @login_required
def home(request):
    # Récupérer le nom d'utilisateur depuis la session
    username = request.session.get('username')

    # Vérifier si le nom d'utilisateur est présent dans la session
    if username:
        # Récupérer l'utilisateur à partir du nom d'utilisateur
        user = User.objects.get(username=username)
        context = {
            'user': user
        }
        return render(request, 'home.html', context)
    else:
        # Gérer le cas où le nom d'utilisateur n'est pas présent dans la session
        return redirect('login')


def graph(request):
    # Récupérez les données pour le graphique en fonction de la durée sélectionnée
    # Utilisez une librairie JavaScript pour générer les graphiques
    data = {
        'labels': ['Label 1', 'Label 2', 'Label 3'],
        'values': [10, 20, 30]
    }
    return JsonResponse(data)
