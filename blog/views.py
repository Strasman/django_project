from django.http import HttpResponse, HttpResponsePermanentRedirect
import datetime
from django.shortcuts import render, get_object_or_404, get_list_or_404, reverse, redirect
from django.conf import settings
from .models import Author, Tag, Category, Post
from django.http import (HttpResponse, HttpResponseNotFound, 
                        Http404, HttpResponseRedirect, HttpResponsePermanentRedirect)
from django.contrib import messages
from .forms import FeedbackForm, ContactForm
from django.core.mail import mail_admins
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django_project import helpers
from django.contrib import messages
from django.contrib import auth

def index(request):
    return HttpResponse("Hello Django")


def test_redirect(request):
    #c = Category.objects.get(name='java')
    #return redirect(c.get_absolute_url())
    return redirect('post_list', permanent=True)



# view function to display a list of posts
def post_list(request):
    posts = Post.objects.order_by("-id").all()
    posts = helpers.pg_records(request, posts, 5)
    return render(request, 'blog/post_list.html', {'posts': posts})


# view function to display a single post
def post_detail(request, pk, post_slug):    
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


# view function to display post by category
def post_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = get_list_or_404(Post.objects.order_by("-id"), category=category)
    posts = helpers.pg_records(request, posts, 5)
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'blog/post_by_category.html', context)


# view function to display post by tag
def post_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = get_list_or_404(Post.objects.order_by("-id"), tags=tag)
    posts = helpers.pg_records(request, posts, 5)
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

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            
            # Display a success message
            messages.success(request, 'Your message has been sent.')

            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form})

"""" With sending an email 
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            sender = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            topic = form.cleaned_data['topic']
            message = form.cleaned_data['message']
            headline = "You've been contacted from {}:{}".format(name, sender)
            msg_body = "Topic: {}\n\nMessage: {}\n\Phone: {}".format(topic, message,phone)
            recipients = ['elad.strasman@gmail.com'] 
            
            mail_admins(headline, msg_body, fail_silently=False, connection=None, html_message=None)
            messages.success(request, 'Your message has been sent.')
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form})
"""

def test_cookie(request):   
    if not request.COOKIES.get('color'):
        response = HttpResponse("Cookie Set")
        response.set_cookie('color', 'blue')
        return response
    else:
        return HttpResponse("Your favorite color is {0}".format(request.COOKIES['color']))
    

def track_user(request):
    response = render(request, 'blog/track_user.html') # store the response in response variable
    if not request.COOKIES.get('visits'):        
        response.set_cookie('visits', '1', 3600 * 24 * 365 * 2)
    else:
        visits = int(request.COOKIES.get('visits', '1')) + 1
        response.set_cookie('visits', str(visits),  3600 * 24 * 365 * 2)
    return response

def stop_tracking(request):
    if request.COOKIES.get('visits'):
       response = HttpResponse("Cookies Cleared")
       response.delete_cookie("visits")
    else:
        response = HttpResponse("We are not tracking you.")
    return response

def test_session(request):
    request.session.set_test_cookie()
    return HttpResponse("Testing session cookie")


def test_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("Cookie test passed")
    else:
        response = HttpResponse("Cookie test failed")
    return response

def save_session_data(request):
    # set new data
    request.session['id'] = 1
    request.session['name'] = 'root'
    request.session['password'] = 'rootpass'
    return HttpResponse("Session Data Saved")


def access_session_data(request):
    response = ""
    if request.session.get('id'):
        response += "Id : {0} <br>".format(request.session.get('id'))
    if request.session.get('name'):
        response += "Name : {0} <br>".format(request.session.get('name'))
    if request.session.get('password'):
        response += "Password : {0} <br>".format(request.session.get('password'))

    if not response:
        return HttpResponse("No session data")
    else:
        return HttpResponse(response)


def delete_session_data(request):
    try:
        del request.session['id']
        del request.session['name']
        del request.session['password']
    except KeyError:
        pass

    return HttpResponse("Session Data cleared")

def lousy_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == "root" and password == "pass":
            request.session['logged_in'] = True
            return redirect('lousy_secret')
        else:
            messages.error(request, 'Error wrong username/password')
    return render(request, 'blog/lousy_login.html')


def lousy_secret(request):
    if not request.session.get('logged_in'):
        return redirect('lousy_login')
    return render(request, 'blog/lousy_secret_page.html')


def lousy_logout(request):
    try:
        del request.session['logged_in']
    except KeyError:
        return redirect('lousy_login')
    return render(request, 'blog/lousy_logout.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('admin_page')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return redirect('admin_page')

        else:
            messages.error(request, 'Error wrong username/password')

    return render(request, 'blog/login.html')


def logout(request):
    auth.logout(request)
    return render(request,'blog/logout.html')

"""
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # To log in the user immediately after registration,
            # add import auth and use auth.login(request, user)
            return redirect('login')  
    else:
        form = RegistrationForm()

    return render(request, 'blog/register.html', {'form': form})
"""

def admin_page(request):
    if not request.user.is_authenticated:
        return redirect('blog_login')

    return render(request, 'blog/admin_page.html')


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