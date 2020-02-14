import datetime

from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models


# Create your views here.
def message(request):
    messages = models.Message.objects.all()
    return render(request, 'guestbook/message.html', {'messages': messages})


def save(request):
    if request.session.get('is_login', None):
        username = request.session.get('user_name')
        title = request.POST.get("title")
        content = request.POST.get("content")
        publish = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = models.Message(title=title, content=content, username=username, publish=publish)
        message.save()
        return redirect('guestbook:message')
    else:
        return redirect('oauth:login')
