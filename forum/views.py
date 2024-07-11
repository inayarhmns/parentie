from django.shortcuts import render, redirect
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

from forum.models import Discussion, Comment, PesertaEvent

def get_all_discussion(request):
    discussion = Discussion.objects.all()
    # context={
    #     'post_item':discussion,
    # }
    data = []
    
    for item in discussion:
        data.append({
            "pk" : item.pk,
            "fields" : {
                "user" : { 
                        "username" : item.user.username,
                        },
               
                "date" : item.date,
                "title" : item.title,
                "body" : item.body,             
            }
        })
    return JsonResponse(data, safe=False)
    # return render(request,'discussion.html',context)

@csrf_exempt
def add_discussion(request):
    discussion = Discussion.objects.all()
    if request.method == "POST":
        username = request.user
        date_user = datetime.date.today()
        title_user = request.POST.get('title')
        body_user = request.POST.get('body')

        new_discussion = discussion(user=username, date=date_user, title=title_user,body=body_user)
        new_discussion.save()
        return JsonResponse({
            "pk" : new_discussion.pk,
            "fields" : {
                "user" : { 
                        "username" : new_discussion.user.username
                        },
               
                "date" : new_discussion.date,
                "title" : new_discussion.title,
                "body" : new_discussion.body,
                
            }
        })
    return JsonResponse({"instance": "gagal Dibuat"}, status=400)



# def get_post_json(request):

#     data = []
#     discussion = discussion.objects.all()
    
#     for item in discussion:
#         data.append({
#             "pk" : item.pk,
#             "fields" : {
#                 "user" : { 
#                         "username" : item.user.username,
#                         "name"     : item.user.name,
#                         "role"     : item.user.role
#                         },
               
#                 "date" : item.date,
#                 "title" : item.title,
#                 "body" : item.body,
#                 "slug":item.slug,
                
#             }
#         })
#     return JsonResponse(data, safe=False)

# def get_comments_json(request):
#     dataa = []
#     comments = Comment.objects.all()
    
#     for item in comments:
#         dataa.append({
#             "pk" : item.pk,
#             "fields" : {
#                 "name" : { 
#                         "username" : item.name.username,
#                         "name"     : item.name.name,
#                         "role"     : item.name.role
#                         },
#                 "discussion":{
#                     "pk":item.discussion.pk
#                 },
#                 "date_added" : item.date_added,
#                 "body" : item.body,
                
#             }
#         })
#     return JsonResponse(dataa, safe=False)



# @csrf_exempt
# @login_required (login_url='../login/')
# def add_comment(request,slug):
#     posts = discussion.objects.get(slug=slug)
#     if request.method == "POST":
#         form = comment_form(request.POST)

#         if form.is_valid():
#             name_user = request.user
#             post_user = posts
#             date_user = datetime.date.today()
#             comment_user = request.POST.get('body')
#             new_comment = Comment(discussion=post_user, name= name_user, body=comment_user, date_added = date_user)
#             Comment.objects.create(discussion=post_user, name= name_user, body=comment_user, date_added = date_user)
#             return JsonResponse({
#             "pk" : new_comment.pk,
#             "fields" : {
#                 "name" : { 
#                         "username" : new_comment.name.username,
#                         "name"     : new_comment.name.name,
#                         "role"     : new_comment.name.role
#                         },
               
#                 "discussion" : new_comment.discussion,
#                 "date_added" : new_comment.date_added,
#                 "body" : new_comment.body,                
#             }
#         })



# @csrf_exempt
# @login_required(login_url='../login/')
# def detail(request,slug):
#     # posts = discussion.objects.get(slug=slug)
    
#     posts = discussion.objects.get(slug=slug)


#     if request.method == "POST":
#         form = comment_form(request.POST)

#         if form.is_valid():
#             name_user = request.user
#             post_user = posts
#             date_user = datetime.date.today()
#             comment_user = request.POST.get('body')
#             new_comment = Comment(discussion=post_user, name= name_user, body=comment_user, date_added = date_user)
#             return JsonResponse({
#             "pk" : new_comment.pk,
#             "fields" : {
#                 "name" : { 
#                         "username" : new_comment.name.username,
#                         "name"     : new_comment.name.name,
#                         "role"     : new_comment.name.role
#                         },
               
#                 "discussion" : new_comment.discussion,
#                 "date_added" : new_comment.date_added,
#                 "body" : new_comment.body,                
#             }
#         })
           

#         return redirect('discussion:detail',slug=posts.slug)
#     context={
#         'posts':posts,
#         'form' :comment_form,
#     }
#     return render(request,'detail_post.html',context)


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
        data = Event.objects.filter(id=id)
        data.delete()
        return JsonResponse({"success": "Event deleted successfully"}, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500) 

    # return redirect('forum:event/4')

    