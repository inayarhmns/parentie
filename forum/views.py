from django.shortcuts import render
from forum.models import Event
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json



# Create your views here.
def event(request, id):
    context = get_detail_event(id)
    return render(request, 'detail_event.html', context)


def events(request):
    if(request.method == 'GET'):
        data = Event.objects.all()
        print(data)
        return JsonResponse({"error": "user Dibuat"}, status=200)

    
def get_detail_event(id):
    data = Event.objects.filter(id=id)
    data_serialized = list(data.values())
    return data_serialized[0]

    
@csrf_exempt
def create_detail_event(request, id):
    try:
        if(request.method == "POST"):
            user = request.POST.get('user')
            judul = request.POST.get('judul')
            detail = request.POST.get('detail')
            penyelenggara = request.POST.get('penyelenggara')
            lokasi = request.POST.get('lokasi')
            tanggal_waktu_mulai = request.POST.get('tanggal_waktu_mulai')
            tanggal_waktu_selesai = request.POST.get('tanggal_waktu_selesai')
            link_event = request.POST.get('link_event')
            nama_contact_person = request.POST.get('nama_contact_person')
            nomor_contact_person = request.POST.get('nomor_contact_person')

            event = Event(user, judul,detail, penyelenggara, lokasi, tanggal_waktu_mulai, tanggal_waktu_selesai, link_event, nama_contact_person, nomor_contact_person)
            event.save()

            return JsonResponse({"success": "Event added successfully"}, status=200)
    except:
        return JsonResponse({"error": "Error adding data"}, status=500)

    
@csrf_exempt
def update_detail_event(request, id):
    try:
        if request.method == "PUT":
            data = Event.objects.filter(id=id).first()
            if not data:
                return JsonResponse({"error": "Event not found"}, status=404)
            
            body = json.loads(request.body)
            user = body.get('user', data.user)
            judul = body.get('judul', data.judul)
            detail = body.get('detail', data.detail)
            penyelenggara = body.get('penyelenggara', data.penyelenggara)
            lokasi = body.get('lokasi', data.lokasi)
            tanggal_waktu_mulai = body.get('tanggal_waktu_mulai', data.tanggal_waktu_mulai)
            tanggal_waktu_selesai = body.get('tanggal_waktu_selesai', data.tanggal_waktu_selesai)
            link_event = body.get('link_event', data.link_event)
            nama_contact_person = body.get('nama_contact_person', data.nama_contact_person)
            nomor_contact_person = body.get('nomor_contact_person', data.nomor_contact_person)

            data.user = user
            data.judul = judul
            data.detail = detail
            data.penyelenggara = penyelenggara
            data.lokasi = lokasi
            data.tanggal_waktu_mulai = tanggal_waktu_mulai
            data.tanggal_waktu_selesai = tanggal_waktu_selesai
            data.link_event = link_event
            data.nama_contact_person = nama_contact_person
            data.nomor_contact_person = nomor_contact_person

            data.save()

            return JsonResponse({"success": "Event updated successfully"}, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    

@csrf_exempt
def delete_detail_event(request, id):
    try:
        if(request.method == "DELETE"):
            data = Event.objects.filter(id=id)
            print(data)
            data.delete()
            return JsonResponse({"success": "success deleeting data"}, status=200)
    except:
        return JsonResponse({"error": "error deleting data"}, status=500)


    

    