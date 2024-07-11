from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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

            pengguna_baru = RegisteredUser.objects.create_user(username=username, password=password, nama = nama, peran = peran, domisili = domisili, agama = agama, umur = umur, golongan_darah = golongan_darah, kondisi_ibu = kondisi_ibu, umur_bayi = umur_bayi, jenis_kelamin_bayi = jenis_kelamin)
            
            pengguna_baru.save()
            return JsonResponse({"instance": "user Dibuat"}, status=200)
        
        except:
            return JsonResponse({"instance": "gagal Dibuat"}, status=400)
     
    return JsonResponse({"instance": "gagal Dibuat"}, status=400)

