from django.urls import path
from donor.views import get_all_donors, start_chat

app_name = 'donor'

urlpatterns = [
    path('', get_all_donors, name='get_all_donors'),
    path('start-chat/', start_chat, name='start_chat'),

]