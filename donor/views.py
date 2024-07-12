from django.shortcuts import render
from donor.models import Donor
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from chat.models import Thread
from authentication.models import RegisteredUser
from django.db.models import Q
import os
from django.conf import settings

# Create your views here.

@login_required(login_url='/auth/login')
def get_all_donors(request):
    tag_filter = request.GET.get('tag')
    domisili_filter = request.GET.get('domisili')
    username = request.session.get("username")
    registered_user = RegisteredUser.objects.get(user__username=username)

    json_file_path = os.path.join(settings.BASE_DIR, 'static/json/kota.json')

    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        cities = [item['text'] for item in data['result']]

    if tag_filter:
        if domisili_filter:
            donors = Donor.objects.filter(user__domisili=domisili_filter, tag=tag_filter, selesai=False).exclude(user=registered_user)
        else:
            donors = Donor.objects.filter(tag=tag_filter, selesai=False).exclude(user=registered_user)
    elif domisili_filter:
        donors = Donor.objects.filter(user__domisili=domisili_filter, selesai=False).exclude(user=registered_user)
    else:
        donors = Donor.objects.filter(selesai=False).exclude(user=registered_user)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('donor_cards.html', {'donors': donors[::-1]})
        return JsonResponse({'html': html})

    return render(request, 'donor.html', {'donors': donors[::-1], 'tag_filter': tag_filter, 'domisili_filter': domisili_filter, 'cities': cities})


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