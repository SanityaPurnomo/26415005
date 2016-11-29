--coba bokeh isi views.py--
from django.http import HttpResponse, Http404
from django.shortcuts import render,get_object_or_404
#from django.views import generic
from .models import Cabe, Bulan, Harga
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components

def simple_chart(request):
    plot = figure()
    plot.circle([1,2],[3,4])
    script, div = components(plot, CDN)
    context = {'the_script':script, 'the_div':div}
    return render(request, 'priceAnalysis/simple_chart.html', context)

def index(request):
    return render(request, 'priceAnalysis/index.html')

def detail(request, cabe_id):
    cabe = get_object_or_404(Cabe, pk=cabe_id)
    context = {'cabe' : cabe}
    return render(request, 'priceAnalysis/detail.html', context)

def list(request):
    all_cabe = Cabe.objects.all()
    context = {'all_cabe': all_cabe}
    return render(request,'priceAnalysis/listdata.html',context)






--isi dari urls.py supaya bisa ke bokeh html-
from django.conf.urls import url
from . import views

app_name = 'priceAnalysis'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<cabe_id>[0-9]+)$', views.detail, name='detail'),
    url(r'^datacabe/$', views.list, name='list'),
    url(r'^simple_chart/$',views.simple_chart,name="simple_chart"),
]
