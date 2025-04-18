from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse

from .models import Member

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('page.html')
    context = {
    'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))