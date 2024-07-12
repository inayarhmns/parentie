from django.urls import path
from user_profile.views import get_profile, butuh_asi, donor_asi, mark_as_done

app_name = 'user_profile'

urlpatterns = [
    path('', get_profile, name='get_profile'),
    path('/butuh_asi', butuh_asi, name='butuh_asi'),
    path('/donor_asi', donor_asi, name='donor_asi'),
    path('mark_as_done/<int:donor_id>/', mark_as_done, name='mark_as_done'),
]