from django.http import HttpResponse, HttpResponsePermanentRedirect
import datetime
from django.shortcuts import render, get_object_or_404, get_list_or_404, reverse, redirect
from django.conf import settings
from .models import Author, Tag, Category, Post
from django.http import (HttpResponse, HttpResponseNotFound, 
                        Http404, HttpResponseRedirect, HttpResponsePermanentRedirect)
from django.contrib import messages
from .forms import FeedbackForm
from django.core.mail import mail_admins

def index(request):
    return HttpResponse("Hello Django")


def test_redirect(request):
    #c = Category.objects.get(name='java')
    #return redirect(c.get_absolute_url())
    return redirect('post_list', permanent=True)



# view function to display a list of posts
def post_list(request):
    posts = Post.objects.order_by("-id").all()
    return render(request, 'blog/post_list.html', {'posts': posts})


# view function to display a single post
def post_detail(request, pk, post_slug):    
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


# view function to display post by category
def post_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = get_list_or_404(Post.objects.order_by("-id"), category=category)
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'blog/post_by_category.html', context)


# view function to display post by tag
def post_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = get_list_or_404(Post.objects.order_by("-id"), tags=tag)
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

def feedback(request):
    if request.method == 'POST':
        f = FeedbackForm(request.POST)
        if f.is_valid():
            name = f.cleaned_data['name']
            sender = f.cleaned_data['email']
            subject = "You have a new Feedback from {}:{}".format(name, sender)
            message = "Subject: {}\n\nMessage: {}".format(f.cleaned_data['subject'], f.cleaned_data['message'])
            mail_admins(subject, message)
        
            f.save()
            messages.add_message(request, messages.INFO, 'Feedback Submitted.')
            return redirect('feedback')
    else:
        f = FeedbackForm()
    return render(request, 'blog/feedback.html', {'form': f})


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