from django.urls import path
from forum_v2.views import events, get_detail_event, delete_detail_event, update_detail_event, create_detail_event, event, get_detail_discussion, get_all_discussion,add_comment,add_discussion, delete_comment,delete_discussion

app_name = ''

urlpatterns = [
    path('events/', events, name='events_v2'),
    path('event-detail/<int:id>/', get_detail_event, name='get_detail_event_v2'),
    path('event-delete/<int:id>/', delete_detail_event, name='delete_detail_event_v2'),
    path('event-update/<int:id>/', update_detail_event, name='update_detail_event_v2'),
    path('event-create/', create_detail_event, name='create_detail_event_v2'),
    path('event/<int:id>/', event, name='event_v2'),
    path('add_discussion', add_discussion, name='add_discussion_v2'),
    path('discussion', get_all_discussion, name='discussion_v2'),
    path('discussion/<str:id>', get_detail_discussion, name='get_discussion_by_id_v2'),
    path('add_comment/<str:id>', add_comment, name='add_comment_v2'),
    path('delete_comment/<str:id>', delete_comment, name='delete_comment_v2'),
    path('delete_discussion/<str:id>', delete_discussion, name='delete_discussion_v2'),
    path('', get_all_discussion, name='home')
]