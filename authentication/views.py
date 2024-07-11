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
            username = request.POST["username"]
            password = request.POST["password"]
            nama = request.POST["nama"]
            peran = request.POST["peran"]
            domisili = request.POST["domisili"]
            agama = request.POST["agama"]
            umur = request.POST["umur"]
            if umur == '':
                umur = None
            
            try: 
                golongan_darah = request.POST["golongan_darah"]
            except:
                golongan_darah = None

            try: 
                kondisi_ibu = request.POST["kondisi_ibu"]
            except:
                kondisi_ibu = None

            try: 
                umur_bayi = request.POST["umur_bayi"]
            except:
                umur_bayi = None

            try:
                jenis_kelamin = request.POST["jenis_kelamin"]
            except:
                jenis_kelamin = None

            user = User.objects.create_user(username=username, password=password)
            pengguna_baru = RegisteredUser.objects.create(user=user, nama = nama, peran = peran, domisili = domisili, agama = agama, umur = umur, golongan_darah = golongan_darah, kondisi_ibu = kondisi_ibu, umur_bayi = umur_bayi, jenis_kelamin_bayi = jenis_kelamin)
            
            pengguna_baru.save()
            return render(request, "login.html")
            return JsonResponse({"instance": "user Dibuat"}, status=200)
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    
    return render(request, "register.html")


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
                    return JsonResponse({
                    "status": True,
                    "message": "Successfully Logged In!"
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

    



@csrf_exempt
def logout(request):
	if request.user.is_authenticated or ['loggedIn']:
		if request.user.is_authenticated:
			auth_logout(request)
		return JsonResponse({"status" : "logged out"}, status=200)
	return JsonResponse({"status": "Not yet authenticated"}, status =403)


