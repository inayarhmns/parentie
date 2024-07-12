from django.shortcuts import render
from authentication.models import RegisteredUser

# Create your views here.
def get_profile(request):
    username = request.session.get("username")
    return render(request, "profile.html", {'username': username})
    # return RegisteredUser.objects.filter(username ==- request.session.get("username"))