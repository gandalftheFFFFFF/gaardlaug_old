from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Message
from .forms import MessageForm
# Create your views here.

def guestbook(request):
    messages = Message.objects.all()
    form = MessageForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        msg = Message.objects.create(name=data['name'], message=data['message'])
        msg.save()
        return HttpResponseRedirect('')

    context = {'form':form, 'messages':messages}
    return render(request, 'guestbook.html', context)
