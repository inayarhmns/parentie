from django.urls import path
from forum.views import events, get_detail_event, delete_detail_event, update_detail_event, create_detail_event, event, get_detail_discussion, get_all_discussion,add_comment,add_discussion, delete_comment,delete_discussion

app_name = 'forum'

urlpatterns = [
    path('events/', events, name='events'),
    path('event-detail/<int:id>/', get_detail_event, name='get_detail_event'),
    path('event-delete/<int:id>/', delete_detail_event, name='delete_detail_event'),
    path('event-update/<int:id>/', update_detail_event, name='update_detail_event'),
    path('event-create/<int:id>/', create_detail_event, name='create_detail_event'),
    path('event/<int:id>/', event, name='event'),
    path('add_discussion', add_discussion, name='add_discussion'),
    path('discussion', get_all_discussion, name='discussion'),
    path('discussion/<str:id>', get_detail_discussion, name='get_discussion_by_id'),
    path('add_comment/<str:id>', add_comment, name='add_comment'),
    path('delete_comment/<str:id>', delete_comment, name='delete_comment'),
    path('delete_discussion/<str:id>', delete_discussion, name='delete_discussion')

    
    
]