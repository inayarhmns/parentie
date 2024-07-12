from django.shortcuts import render
from authentication.models import RegisteredUser
from donor.models import Donor

# Create your views here.
def get_profile(request):
    username = request.session.get("username")
    registered_user = RegisteredUser.objects.get(user__username=username)
    history = Donor.objects.filter(user__user__username=username)
    return render(request, "profile.html", {'user': registered_user, 'history': history})