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
     
    return JsonResponse({"instance": "not Dibuat"}, status=400)

