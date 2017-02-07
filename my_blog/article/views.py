from django.shortcuts import render
from django.http import Http404
from article.models import Article


'# Create your views here.'


def home(request):
    post_list = Article.objects.all()
    return render(request, 'article/home.html', {'post_list': post_list})


def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'article/post.html', {'post': post})


def classify(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'article/classify.html', {'post_list': post_list, 'error': False})


def search_tag(request, tag):
    try:
        post_list = Article.objects.filter(category__iexact=tag) #contains
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'article/tag.html', {'post_list': post_list})

