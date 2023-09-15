# myapp/urls.py

from django.urls import path
from myapp import views

urlpatterns = [
    # Registration URLs
    path('lawyer/signup/', views.lawyer_signup, name='lawyer_signup'),
    path('client/signup/', views.client_signup, name='client_signup'),
    
    # Login URLs
    path('lawyer/login/', views.lawyer_login, name='lawyer_login'),
    path('client/login/', views.client_login, name='client_login'),

    # Dashboard URLs
    path('lawyer/dashboard/', views.lawyer_dashboard, name='lawyer_dashboard'),
    path('client/dashboard/', views.client_dashboard, name='client_dashboard'),
    
    # Add other URLs as needed for your application
]
