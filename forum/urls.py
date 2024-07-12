from django.urls import path
from forum.views import get_all_discussion, get_detail_discussion,add_comment,add_discussion

app_name = 'forum'

urlpatterns = [
    path('add_discussion', add_discussion, name='add_discussion'),
    path('discussion', get_all_discussion, name='discussion'),
    path('discussion/<str:id>', get_detail_discussion, name='get_discussion_by_id'),
    path('add_comment/<str:id>', add_comment, name='add_comment'),
    
    
]