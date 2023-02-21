from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.
def view_home(request):
    template = loader.get_template('home.html')
    context = {
        'navbar': 'home'
    }
    return HttpResponse(template.render(context, request))


def view_members(request):
    template = loader.get_template('members.html')
    context = {
        'navbar': 'members'
    }
    return HttpResponse(template.render(context, request))


def view_vehicles(request):
    template = loader.get_template('vehicles.html')
    context = {
        'navbar': 'vehicles'
    }
    return HttpResponse(template.render(context, request))


def view_aboutus(request):
    template = loader.get_template('aboutus.html')
    context = {
        'navbar': 'aboutus'
    }
    return HttpResponse(template.render(context, request))
