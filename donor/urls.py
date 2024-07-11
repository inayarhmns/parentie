from django.urls import path
from donor.views import get_all_donors

app_name = 'donor'

urlpatterns = [
    path('', get_all_donors, name='get_all_donors'),
]