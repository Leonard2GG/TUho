from django.shortcuts import redirect

def admin_required(function):
    def wrap(request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('Inicio')
        return function(request, *args, **kwargs)
    return wrap