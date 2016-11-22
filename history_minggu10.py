--isi models.py
from django.db import models

class Cabe(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Bulan(models.Model):
    cabe = models.ForeignKey(Cabe, on_delete=models.CASCADE)
    bulan = models.IntegerField()
    tahun = models.IntegerField()

    def __str__(self):
        return str(self.bulan) + str(self.tahun)

class Harga(models.Model):
    tgl = models.ForeignKey(Bulan, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return str(self.price)

class DataCabe(models.Model):
    data = models.FileField()





--isi url.py
from django.conf.urls import url
from . import views

app_name = 'priceAnalysis'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<cabe_id>[0-9]+)$', views.detail, name='detail'),
    url(r'^datacabe/$', views.list, name='list'),
]





--isi views.py
from django.http import HttpResponse, Http404
from django.shortcuts import render,get_object_or_404
#from django.views import generic
from .models import Cabe, Bulan, Harga

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

