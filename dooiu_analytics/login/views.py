from dooiu_analytics.settings import BASE_DIR
from django.shortcuts import render, redirect
import logging
from django.db import connection
import pickle

from services import user_services
from show_data import views as data_views
from login.models import UserProfile


def user_login(request):
    if get_current_user(request):
        return redirect('home')

    if request.method == 'POST':

        phone_number = request.POST['phone_number']
        password = request.POST['password']

        user = user_services.custom_authenticate(phone_number=phone_number, password=password)

        if user is not None:
            user_profile = UserProfile(id=user[0], phone_number=user[3], email=user[5], country_code=user[2],
                                       user_type=user[10], first_name=user[6], last_name=user[7])

            current_user_dict = user_profile.to_dict()
            request.session['current_user'] = current_user_dict
            context = {f'user': user_profile}
            return redirect('home')
        else:
            print("user is None")
            context = {f'error_message': 'Invalid credentials. Please try again.' + phone_number + '  ' + password}
            return render(request, 'login.html', context)
    else:
        print("request.method not 'POST'")

    return render(request, 'login.html')


def get_current_user(request):
    if 'current_user' in request.session:
        current_user_dict = request.session.get('current_user')
        return UserProfile(**current_user_dict)
    return None


def user_logout(request):
    if 'current_user' in request.session:
        del request.session['current_user']
    return redirect('login')
