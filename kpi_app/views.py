from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Circle, Kpi
from .forms import KPIForm


def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request)) 


def choose_circle(request):  
    circles = Circle.objects.all()
    template = loader.get_template('circles.html')
    context = {
    'circles': circles,
  }
    
    return HttpResponse(template.render(context, request)) 


def choose_kpi(request, cid):
    circle = Circle.objects.get(id=cid)
    kpis = circle.kpi_set.all()
    template = loader.get_template('kpis.html')
    context = {
    'name': circle.circle_name,
    'kpis': kpis,
    'cid': cid,
  }
    return HttpResponse(template.render(context, request))


def update_kpi(request, cid, kid):
    kpi = Kpi.objects.get(id=kid)

    if request.user.is_authenticated:
        if request.method == "POST":
            f = KPIForm(request.POST, instance=kpi)
            if f.is_valid():
                kpi.updated_by = request.user.username
                f.save()
                return HttpResponseRedirect("saved")
        
        else:
            f = KPIForm(instance=kpi)
    
    hist = kpi.history.all()
    items = [(h.year, h.month, h.value, h.updated_at, h.updated_by) for h in hist]

    template = loader.get_template('update.html')
    context = {'name': kpi.kpi_name,
               'form': f,
               'cid': cid,
               'items': items,}

    return HttpResponse(template.render(context, request))


def saved(request, cid, kid):
    kpi = Kpi.objects.get(id=kid)
    template = loader.get_template('saved.html')
    context = {'cid': cid,
               'kid': kid,
               'name': kpi.kpi_name}

    return HttpResponse(template.render(context, request))

