from django.shortcuts import render
from authentication.models import RegisteredUser

# Create your views here.
def get_profile(request):
    return
    # return RegisteredUser.objects.filter(username ==- request.session.get("username"))