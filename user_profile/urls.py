from django.urls import path
from user_profile.views import get_profile

app_name = 'user_profile'

urlpatterns = [
    path('', get_profile, name='get_profile'),
]