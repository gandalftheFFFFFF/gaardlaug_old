from django.shortcuts import render

from .models import Uploader

from django.http import HttpResponse

# Create your views here.

def uploads(request):
    # render(request, template, context

    # request

    # template
    template = 'documents.html'

    # context
    documents = Uploader.objects.all()[0:5]
    context = {'documents': documents}

    return render(request, template, context)

def documents_by_category(request, specification):
    """ render(request, template, context) """

    template = 'document_category.html'

    try:
        docs = Uploader.objects.filter(category=specification)
    except Uploader.DoesNotExist:
        docs = None

    context= {'docs':docs}

    return render(request, template, context)
