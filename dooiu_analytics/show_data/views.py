from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from show_data.models import User, Data
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Vérifiez les informations de connexion
        # et redirigez vers la page principale si les informations sont valides
        if username and password:
            user = User.objects.get(username=username)
            if user.check_password(password):
                # Sauvegarder le nom d'utilisateur dans la session
                request.session['username'] = username
                return redirect('home')

    return render(request, 'login.html')


#@login_required
def home(request):
    # Récupérer le nom d'utilisateur depuis la session
    username = request.session.get('username')

    # Vérifier si le nom d'utilisateur est présent dans la session
    if username:
        # Récupérer l'utilisateur à partir du nom d'utilisateur
        #user = User.objects.get(username=username)
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
