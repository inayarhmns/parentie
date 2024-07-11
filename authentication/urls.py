from django.urls import path
from authentication.views import register,login

app_name = 'auth'

urlpatterns = [
    path('register', register, name='register'),
    # path('add_footprint', add_footprint, name='add_footprint'),
    path('login', login, name='login'),

    
]