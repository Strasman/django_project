from django.http import HttpResponse
import datetime
from django.shortcuts import render
from django.conf import settings
from .models import Author, Tag, Category, Post

def index(request):
    return HttpResponse("Hello Django")


# view function to display a list of posts
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


# view function to display a single post
def post_detail(request, pk):    
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


# view function to display post by category
def post_by_category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    posts = Post.objects.filter(category__slug=category_slug)
    context = {
        'category': category,
        'posts': posts
    }
    print(category)
    return render(request, 'blog/post_by_category.html', context)


# view function to display post by tag
def post_by_tag(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    posts = Post.objects.filter(tags__name=tag)
    context = {
        'tag': tag,
        'posts': posts
    }
    return render(request, 'blog/post_by_tag.html', context )



def today_is(request):
    now = datetime.datetime.now()
    return render(request, 'blog/datetime.html', {
                                'now': now,
                                'template_name': 'blog/nav.html',
                                'base_dir': settings.BASE_DIR })


"""""
def today_is(request):
    now = datetime.datetime.now()
    t = template.loader.get_template('blog/datetime.html')
    #In modern versions of Django, the use of the Context class is not necessary. 
    #Instead, you can pass a dictionary directly to the template rendering function.
    c = {'now': now} 
    html = t.render(c)
    return HttpResponse(html)
"""