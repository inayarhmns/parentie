from django.shortcuts import render
from donor.models import Donor
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string

# Create your views here.

@login_required(login_url='/auth/login')
def get_all_donors(request):
    domisili = request.session.get('domisili')
    tag_filter = request.GET.get('tag', None)  # Get the 'tag' parameter from GET request
    
    if tag_filter:
        donors = Donor.objects.filter(user__domisili="Bandung", tag=tag_filter)
    else:
        donors = Donor.objects.filter(user__domisili="Bandung")
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('donor_cards.html', {'donors': donors})
        return JsonResponse({'html': html})
    
    
    return render(request, 'donor.html', {'donors': donors, 'tag_filter': tag_filter})