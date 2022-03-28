from django.shortcuts import render
from . models import Articles, Categories, AnalyticsCode, Comments, Messages
from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.http import HttpResponse, JsonResponse
import datetime

# Create your views here.
def index(request):
    all_posts = Articles.objects.all()
    categories = Categories.objects.all()
    analyticscode = AnalyticsCode.objects.all().first()
    return render(request, 'blog/index.html', {"posts":all_posts,
                                               "categories":categories,
                                               "analyticscode":analyticscode})

def article(request, slug):
    categories = Categories.objects.all()
    post = Articles.objects.get(slug = slug)
    analyticscode = AnalyticsCode.objects.all().first()
    return render(request, 'blog/article.html', {"post":post,
                                                 "categories":categories,
                                                 "analyticscode":analyticscode})


def article_list(request, category):
    analyticscode = AnalyticsCode.objects.all().first()
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
                                                      "categories":categories,
                                                      "analyticscode":analyticscode})



def save_comment(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        comment = request.POST.get('actual_comment', None)
        blog_id = request.POST.get('blog_id', None)
        print(blog_id)
        
        blog = Articles.objects.get(id=blog_id)
        save_comment = Comments.objects.create(name=name, comment=comment, blog=blog)
        save_comment.save()

        mydict = {"name":name, "comment":comment, "blog_id":blog_id, "date_created":save_comment.date_created}
    print(save_comment.date_created)
    return JsonResponse(mydict)

def like_dislike_comment(request, val, comment_id):
    total = ''
    if val == 'like':
        comment = Comments.objects.get(id=comment_id)
        comment.likes +=1
        comment.save()
        total = comment.likes
    elif val == 'dislike':
        comment = Comments.objects.get(id=comment_id)
        comment.dislikes +=1
        comment.save()
        total = comment.dislikes
        print(val)
        print(comment)
    else:
        pass
    
    comment_like_dislike_details = {"total_like_dislike":total, "val":val, "comment_id":comment_id }
    print(total, val)
    return JsonResponse(comment_like_dislike_details)


def sendmessage(request):
    if request.method == "POST":
        name = request.POST.get("name", None)
        email = request.POST.get("email", None)
        phone = request.POST.get("phone", None)
        message = request.POST.get("message", None)
        
        user_message = Messages.objects.create(name=name, email=email, phone=phone, message=message)
        user_message.save()

    return render(request, 'blog/sendmessage.html')


def contacts(request):
    return render(request, 'blog/contacts.html')

