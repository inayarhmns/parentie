from django.urls import path
from forum.views import add_discussion, get_all_discussion

app_name = 'forum'

urlpatterns = [
    path('add_discussion', add_discussion, name='add_discussion'),
    path('get_all_discussion', get_all_discussion, name='get_all_discussion'),
    
]