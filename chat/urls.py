from django.urls import path
from . import views
urlpatterns = [
    path('', views.messages_page),
    path('<int:thread_id>/', views.messages_page, name='messages_page'),

]