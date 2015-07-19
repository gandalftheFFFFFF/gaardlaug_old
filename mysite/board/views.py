from django.shortcuts import render

from .models import BoardMember, Role, Cadastre

from django.http import HttpResponse
# Create your views here.

def index(request):

    template = 'board_overview.html'

    try:
        board_members = BoardMember.objects.filter(active=True)
    except BoardMember.DoesNotExist:
        board_members = None

    try:
        roles = Role.objects.all()
    except Role.DoesNotExist:
        roles = None

    try:
        cadastres = Cadastre.objects.all()
    except Cadastre.DoesNotExist:
        cadastres = None

    context = {
        'board_members':board_members,
        'roles':roles,
        'cadastres':cadastres,
    }

    return render(request, template, context)