# myapp/decorators.py

from functools import wraps
from django.shortcuts import redirect

def lawyer_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_lawyer:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('client_dashboard')  # Redirect to the client dashboard if not a lawyer
    return _wrapped_view

def client_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and not request.user.is_lawyer:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('lawyer_dashboard')  # Redirect to the lawyer dashboard if not a client
    return _wrapped_view
