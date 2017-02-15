from django.shortcuts import render, redirect
from django.http import Http404
from article.models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


'# Create your views here.'


def home(request):
    posts = Article.objects.all()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.paginator(paginator.num_pages)
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


def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request, 'article/home.html')
        else:
            post_list = Article.objects.filter(title__icontains=s)
            if len(post_list) == 0:
                return render(request, 'article/classify.html', {'post_list': post_list, 'error': True})
            else:
                return render(request, 'article/classify.html', {'post_list': post_list, 'error': False})
    return redirect('/')
