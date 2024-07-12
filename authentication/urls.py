from django.urls import path
from authentication.views import register,login

app_name = 'auth'

urlpatterns = [
    # path('', tracker, name='index'),
    path('register', register, name='register'),
    # path('add_footprint', add_footprint, name='add_footprint'),
    path('login', login, name='auth_login'),

    
]