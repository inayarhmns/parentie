from django.urls import path
from authentication.views import register,login, user_logout

app_name = 'auth'

urlpatterns = [
    path('register', register, name='register'),
    path('login', login, name='auth_login'),
    path('logout', user_logout, name='logout'),
]