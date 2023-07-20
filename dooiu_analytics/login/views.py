
from dooiu_analytics.settings import BASE_DIR
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from login.models import User
import logging

from login.backends import NoLastLoginBackend



from django.db import connection
logger = logging.getLogger(__name__)

def login(request):
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        password = request.POST['password']

        logger.debug(f"phone_number: {phone_number}, password: {password}")
        user = authenticate(request, phone_number=phone_number, password=password)

        try:
            with connection.cursor() as cursor:
                print(f"select * from user where phoneNumber = '{phone_number}' and password = '{password}';")
                cursor.execute(f"select * FROM user where phoneNumber = '{phone_number}' and password = '{password}';")
                result = cursor.fetchone()
                if result:
                    print(f"Database connection successful. {result}")
                else:
                    print("Database connection failed.")
        except Exception as e:
            print("Database connection error:", e)

        if user is not None:
            # If the user is valid, log them in and redirect to the home page or any other desired page.
            login(request, user)
            return redirect('home')  # Replace 'home' with the name of your home page URL pattern.
        else:
            # If the user is not valid, display an error message on the login page.
            context = {f'error_message': 'Invalid credentials. Please try again.'+ phone_number + '  ' + password}
            return render(request, 'login.html', context)



    else:
        print("request.method not 'POST'")
    return render(request, 'login.html')
