from django.shortcuts import render
from . models import Articles, Categories

# Create your views here.
def index(request):
    all_posts = Articles.objects.all()
    categories = Categories.objects.all()
    return render(request, 'blog/index.html', {"posts":all_posts,
                                               "categories":categories})

def article(request, slug):
    categories = Categories.objects.all()
    post = Articles.objects.get(slug = slug)
    return render(request, 'blog/article.html', {"post":post,
                                                 "categories":categories})


def article_list(request, category):
    categories = Categories.objects.all()
    try:
        category_id = Categories.objects.filter(name = category).first().id
    except AttributeError:
        category_id = 0
    print(category_id)
    posts = Articles.objects.filter(category = category_id)
    print(posts)
    return render(request, 'blog/article-list.html', {"posts":posts, 
                                                      "category":category,
                                                      "categories":categories})
