from django.shortcuts import get_object_or_404, render, redirect
from forum.models import Event
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json



# Create your views here.

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import HttpResponse, render
from django.core import serializers
import datetime
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
from django.views.decorators.csrf import csrf_exempt

from authentication.models import RegisteredUser
from forum.models import Discussion, Comment, PesertaEvent
from django.contrib.auth.models import User

def get_all_discussion(request):

    query = request.GET.get('q')
    if query:
        discussions = Discussion.objects.filter(title__icontains=query)
    else:
        discussions = Discussion.objects.all()

    data = []
    
    for item in discussions:
        data.append({
            "pk" : item.pk,
            "fields" : {
                "user" : { 
                        "username" : item.user.user.username
                        },
               
                "date" : item.date,
                "title" : item.title,
                "body" : item.body,             
            }
        })

    context={
        'discussion_item':data,
    }
    # return JsonResponse(data, safe=False)
    return render(request,'discussion.html',context)

def get_detail_discussion(request, id):
    try:
        discussion_by_id = Discussion.objects.get(id=id)
        comment_by_discussion = discussion_by_id.comment.all()

        discussion = {
            "id": discussion_by_id.pk,
            "user": discussion_by_id.user.user.username,
            "body": discussion_by_id.body,
            "date": discussion_by_id.date,
            "title": discussion_by_id.title,
        }

        comments = [
            {   "id" : comment.pk,
                "discussion_id":comment.post.id,
                "user": comment.user_commenting.user.username,
                "body": comment.body,
                "date_added": comment.date_added,
            }
            for comment in comment_by_discussion
        ]

        context = {
            'discussion': discussion,
            'comments': comments
        }
        # return JsonResponse(context)
        return render(request,'discussion_detail.html',context)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def add_comment(request, id):
    if request.method == "POST":
        try: 
            user = request.user
            registered_user = get_object_or_404(RegisteredUser, user=user)
            body = request.POST.get('body')
            discussion = get_object_or_404(Discussion, id=id)
            comment = Comment.objects.create(post=discussion, user_commenting=registered_user, body=body)
            # return JsonResponse({
            #     "status": "success",
            #     "comment": {
            #         "user": registered_user.user.username,
            #         "body": body,
            #         "date_added": comment.date_added.strftime('%B %d, %Y')
            #     }
            # })
            return redirect('forum:get_discussion_by_id', id=id)
        except Exception as e:
            return JsonResponse({"status": str(e)})
    return JsonResponse({"status": "error" }, status=400)



@csrf_exempt
def add_discussion(request):
    if request.method == "POST":
        try: 
            user = request.user
            registered_user = get_object_or_404(RegisteredUser, user=user)
            title = request.POST.get('title')
            body = request.POST.get('body')
            new_discussion = Discussion.objects.create(user=registered_user, title=title, body=body)

        #     return JsonResponse({
        #         "pk" : new_discussion.pk,
        #         "fields" : {
        #             "user" : { 
        #                     "username" : new_discussion.user.user.username
        #                     },
                
        #             "date" : new_discussion.date,
        #             "title" : new_discussion.title,
        #             "body" : new_discussion.body,
                    
        #     }
        # })
            return redirect('forum:discussion')

        except Exception as e:
            return JsonResponse({"status": str(e)})
    return JsonResponse({"instance": "gagal Dibuat"}, status=400)

def search_discussions(request):
    query = request.GET.get('q')
    if query:
        discussions = Discussion.objects.filter(title__icontains=query)
    else:
        discussions = Discussion.objects.all()
    
    context = {
        'discussions': discussions,
        'query': query
    }
    return render(request, 'search_results.html', context)

@csrf_exempt
def delete_discussion(request, id):
    try:
        data = Discussion.objects.filter(id=id)
        data.delete()
        return redirect('forum:discussion')
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500) 

@csrf_exempt
def delete_comment(request, id):
    try:
        data = Comment.objects.filter(id=id)
        data.delete()
        return redirect('forum:get_discussion_by_id', id=id)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500) 


def event(request, id):
    id_logged_in = request.session.get('user_id')
    print(id_logged_in)
    context = get_detail_event(id)
    if id_logged_in:
        context["id_logged_in"] = id_logged_in
    else:
        context["id_logged_in"] = ""
    return render(request, 'detail_event.html', context)


def events(request):
    if(request.method == 'GET'):
        data = Event.objects.all()
        return JsonResponse({"error": "user Dibuat"}, status=200)

    
def get_detail_event(id):
    event = Event.objects.filter(id=id).values().first()
    if event:
        peserta_events = PesertaEvent.objects.filter(event_id=id).values('peserta')
        event['peserta_events'] = list(peserta_events)
    return event

    
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
    print(request)
    print("request")
    data = Event.objects.filter(id=id).first()
    if not data:
        return JsonResponse({"error": "Event not found"}, status=404)
    
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    print(body)
    print("body")


    data.user = body.get('user', data.user)
    data.judul = body.get('judul', data.judul)
    data.detail = body.get('detail', data.detail)
    data.penyelenggara = body.get('penyelenggara', data.penyelenggara)
    data.lokasi = body.get('lokasi', data.lokasi)
    data.tanggal_waktu_mulai = body.get('tanggal_waktu_mulai', data.tanggal_waktu_mulai)
    data.tanggal_waktu_selesai = body.get('tanggal_waktu_selesai', data.tanggal_waktu_selesai)
    data.link_event = body.get('link_event', data.link_event)
    data.nama_contact_person = body.get('nama_contact_person', data.nama_contact_person)
    data.nomor_contact_person = body.get('nomor_contact_person', data.nomor_contact_person)

    data.save()

    return JsonResponse({"success": "Event updated successfully"}, status=200)

    return JsonResponse({"error": "Invalid request method"}, status=405)
    

@csrf_exempt
def delete_detail_event(request, id):
    try:
        data = Event.objects.filter(id=id)
        data.delete()
        return JsonResponse({"success": "Event deleted successfully"}, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500) 

    # return redirect('forum:event/4')

    