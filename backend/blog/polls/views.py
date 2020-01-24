from django.shortcuts import render
from .models import Article
from .models import Image
from django.core import serializers
# Create your views here.
import json
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def add_article(request):
    data_article = json.loads(request.body.decode('utf-8'))
    new_article = Article(
         title = data_article['title'],
         content = data_article['content'],
         article_id = data_article['article_id'],
        )
    new_article.save()
    return JsonResponse(data_article)

@csrf_exempt
def get_articles(request):
    data_article = Article.objects.all().order_by('article_id').reverse()
    posts_serialized = serializers.serialize('json', data_article)
    return JsonResponse(posts_serialized, safe=False)

@csrf_exempt
def update_article(request):
    data_article = json.loads(request.body.decode('utf-8'))
    obj = Article.objects.get(article_id=data_article['id'])
    obj.title = data_article['title']
    obj.content = data_article['content']
    obj.save()
    return JsonResponse(data_article)

@csrf_exempt
def delete_article(request):
    data_article = json.loads(request.body.decode('utf-8'))
    Article.objects.filter(article_id=data_article['id']).delete()
    return JsonResponse(data_article)

@csrf_exempt
def register(request):
    data_article = json.loads(request.body.decode('utf-8'))
    username = data_article['username']
    password = data_article['password']
    email = data_article['email']

    #user = User.objects.create_user(username=username, password=password, email=email)
    #user.save()
    return JsonResponse(data_article)

@csrf_exempt
def login(request):
    data_article = json.loads(request.body.decode('utf-8'))
    username = data_article['username']
    password = data_article['password']

    user = auth.authenticate(username=username, password=password)
    if user is not None:
        return HttpResponse("true")
    else:
        return HttpResponse("false")

@csrf_exempt
def change_image(request):
    data_img = json.loads(request.body.decode('utf-8'))
    obj = Image.objects.get(img_id=1)
    obj.url = data_img['url']
    obj.save()
    return JsonResponse(data_img)

@csrf_exempt
def get_url(request):
    data = Image.objects.all()
    posts_serialized = serializers.serialize('json', data)
    return JsonResponse(posts_serialized, safe=False)