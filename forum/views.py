from django.shortcuts import render

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

from forum.models import Discussion, Comment

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


   