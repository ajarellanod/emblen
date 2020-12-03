from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.shortcuts import redirect

from functools import wraps


def requiere_roles(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        
        view_name = request.resolver_match.func.__name__

        return view_func(request, *args, **kwargs)

    return _wrapped_view