from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from authentication.models import RegisteredUser


@csrf_exempt
def register(request):
    if (request.method == "POST"):
        try:
            username = request.POST.get("username")
            password = request.POST.get("password")
            nama = request.POST.get("nama")
            peran = request.POST.get("peran")
            domisili = request.POST.get("domisili")
            agama = request.POST.get("agama")
            umur = request.POST.get("umur")
            golongan_darah = request.POST.get("golongan_darah")
            kondisi_ibu = request.POST.get("kondisi_ibu")
            umur_bayi = request.POST.get("umur_bayi")
            jenis_kelamin = request.POST.get("jenis_kelamin")

            user = User.objects.create_user(username=username, password=password)
            pengguna_baru = RegisteredUser.objects.create(user=user, nama = nama, peran = peran, domisili = domisili, agama = agama, umur = umur, golongan_darah = golongan_darah, kondisi_ibu = kondisi_ibu, umur_bayi = umur_bayi, jenis_kelamin_bayi = jenis_kelamin)
            
            pengguna_baru.save()
            return JsonResponse({"instance": "user Dibuat"}, status=200)
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
     
    return JsonResponse({"instance": "gagal Dibuat"}, status=400)


from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


@csrf_exempt
def login(request):
    if (request.method == "POST"):
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    # Redirect to a success page.
                    request.session['username'] = username
                    request.session['user_id'] = user.id
                    
                    return JsonResponse({
                    "status": True,
                    "message": "Successfully Logged In!",
                    "session": get_session(request),
                    }, status=200)
                else:
                    return JsonResponse({
                    "status": False,
                    "message": "Failed to Login, Account Disabled."
                    }, status=401)

            else:
                return JsonResponse({
                "status": False,
                "message": "Failed to Login, check your email/password."
                }, status=401)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
     
    return render(request, 'login.html')

    

from django.contrib.auth.decorators import login_required

@login_required
def get_session(request):
    # Access the session data
    username = request.session.get('username')
    user_id = request.session.get('user_id')

    if username and user_id:
        return username
    else:
        return "no session data found!"



@csrf_exempt
def logout(request):
	if request.user.is_authenticated or ['loggedIn']:
		if request.user.is_authenticated:
			auth_logout(request)
		return JsonResponse({"status" : "logged out"}, status=200)
	return JsonResponse({"status": "Not yet authenticated"}, status =403)


