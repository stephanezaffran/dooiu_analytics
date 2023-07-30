from django.shortcuts import redirect, render
from functools import wraps

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Vérifiez si l'utilisateur est connecté
        current_user = request.session.get('current_user')


        allowed_urls = ['/login/']

        if not current_user and request.path not in allowed_urls:

            return redirect('login')

        response = self.get_response(request)
        return response


class CheckReferrerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Obtenez l'en-tête HTTP Referer (référent) de la requête
        referrer = request.META.get('HTTP_REFERER', '')

        # Vérifiez si le référent est vide ou ne commence pas par l'URL de l'hôte
        if not referrer or not referrer.startswith(request.build_absolute_uri('/')[:-1]):
            # Si le référent est vide ou ne correspond pas à l'URL de l'hôte, redirigez l'utilisateur vers une page d'erreur ou une autre page appropriée
            return redirect('error_page')  # Remplacez 'error_page' par le nom de la vue de la page d'erreur

        response = self.get_response(request)
        return response



def login_required_with_referrer(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Vérifier si l'utilisateur est connecté
        if not request.user.is_authenticated:
            # Vérifier si le referer est valide
            if not request.META.get('HTTP_REFERER') or not request.META['HTTP_REFERER'].startswith(request.build_absolute_uri('/')):
                return redirect('login')  # Rediriger vers la page de login si le referer n'est pas valide
        return view_func(request, *args, **kwargs)
    return _wrapped_view