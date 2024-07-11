from django.shortcuts import render
from donor.models import Donor
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/auth/login')
def get_all_donors(request):
    user_domisili = request.user.domisili  # Assuming 'domisili' is an attribute of your user model
    
    tag_filter = request.GET.get('tag', None)  # Get the 'tag' parameter from GET request
    
    if tag_filter:
        donors = Donor.objects.filter(user__domisili=user_domisili, tag=tag_filter)
    else:
        donors = Donor.objects.filter(user__domisili=user_domisili)
    
    return render(request, 'donor.html', {'donors': donors, 'tag_filter': tag_filter})

def filter_donors(request):
    tag = request.GET.get('tag', '')
    user_location = request.user.lokasi if hasattr(request.user, 'domisili') else None
    
    if user_location:
        donors = Donor.objects.filter(tag=tag, user__lokasi=user_location)
    else:
        donors = Donor.objects.filter(tag=tag)
    
    return render(request, 'donor.html', {'donors': donors, 'tag': tag})