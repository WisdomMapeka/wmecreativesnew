from django.shortcuts import render
from . models import Articles, Categories

# Create your views here.
def index(request):
    all_posts = Articles.objects.all()
    categories = Categories.objects.all()
    return render(request, 'blog/index.html', {"all_posts":all_posts,
                                               "categories":categories})

def article(request, slug):
    post = Articles.objects.get(slug = slug)
    return render(request, 'blog/article.html', {"post":post})
