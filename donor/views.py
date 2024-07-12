from django.shortcuts import render
from donor.models import Donor
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from authentication.models import User
from chat.models import Thread
from authentication.models import RegisteredUser
from django.db.models import Q

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




@csrf_exempt
@login_required
def start_chat(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        target_user_id = data.get('target_user_id')
        
        try:
            target_user = RegisteredUser.objects.get(id=target_user_id).user
            current_user = request.user

            # Attempt to find an existing thread between the users
            thread = Thread.objects.filter(
                Q(first_person=current_user, second_person=target_user) |
                Q(first_person=target_user, second_person=current_user)
            ).first()

            # If no thread exists, create a new one
            if not thread:
                thread = Thread.objects.create(
                    first_person=current_user,
                    second_person=target_user
                )

            return JsonResponse({
                'success': True,
                'thread_id': thread.id
            })
        
        except RegisteredUser.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'User does not exist'}, status=404)
        
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=400)