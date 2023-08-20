from django.http import HttpResponse
from django import template
import datetime
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello Django")

def today_is(request):
    now = datetime.datetime.now()
    return render(request, 'blog/datetime.html', {'now': now })


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