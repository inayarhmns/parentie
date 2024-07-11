from django.urls import path
from forum.views import events, get_detail_event, delete_detail_event, update_detail_event, create_detail_event, event

app_name = 'forum'

urlpatterns = [
    path('events/', events, name='events'),
    path('event-detail/<int:id>/', get_detail_event, name='get_detail_event'),
    path('event-delete/<int:id>/', delete_detail_event, name='delete_detail_event'),
    path('event-update/<int:id>/', update_detail_event, name='update_detail_event'),
    path('event-create/<int:id>/', create_detail_event, name='create_detail_event'),
    path('event/<int:id>/', event, name='event')





    
]