from django.shortcuts import render, redirect
from functools import wraps


def login_and_referer_required(func):
    @wraps(func)
    def decorated_view(request, *args, **kwargs):
        if not request.session.get('user_id'):
            return redirect('login')

        referer = request.META.get('HTTP_REFERER')
        if not referer or 'http://127.0.0.1:8000/' not in referer:
            return redirect('logout')

        return func(request, *args, **kwargs)

    return decorated_view
