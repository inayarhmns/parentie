from django.shortcuts import render, redirect, get_object_or_404
from authentication.models import RegisteredUser
from django.contrib.auth.decorators import login_required
from donor.models import Donor
from datetime import date
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
@login_required(login_url='/auth/login')
def get_profile(request):
    username = request.session.get("username")
    registered_user = RegisteredUser.objects.get(user__username=username)
    history = Donor.objects.filter(user__user__username=username)[::-1]

    if history:
        status = history[0].tag
        status = status.upper() + " ASI"
    else:
        status = None

    return render(request, "profile.html", {'user': registered_user, 'history': history, 'status': status})

@csrf_exempt
def butuh_asi(request):
    if request.method == "POST":
        try:
            username = request.session.get("username")
            registered_user = RegisteredUser.objects.get(user__username=username)

            donor = Donor.objects.create(user=registered_user, timestamp=date.today(), tag="butuh")
            donor.save()

            return JsonResponse({'message': 'Request successful'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    

@csrf_exempt
def donor_asi(request):
    if request.method == "POST":
        try:
            username = request.session.get("username")
            registered_user = RegisteredUser.objects.get(user__username=username)
            document = request.FILES['document']
            donor = Donor.objects.create(user=registered_user, timestamp=date.today(), tag="donor", document = document)
            donor.save()

            return JsonResponse({'message': 'Request successful'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    

def mark_as_done(request, donor_id):
    donor = get_object_or_404(Donor, pk=donor_id)
    donor.mark_as_done()
    return redirect('user_profile:get_profile')

