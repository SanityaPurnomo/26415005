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





--isi detail.html
{% extends 'priceAnalysis/base.html' %}
{% block title %}
  List - {{ cabe.name }}
{% endblock %}
{% block list_active %}active{% endblock %}
{% block body %}
  <h1>{{ cabe.name }} </h1>
  {% for item in cabe.bulan_set.all %}
    <h4>{{ item.bulan }} - {{ item.tahun }}</h4>
    <ul>
      {% for item2 in item.harga_set.all %}
        <li>{{ item2.price }}</li>
      {% endfor %}
    </ul>
  {% endfor %}
{% endblock %}





--isi base.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{% block title %}Price Analysis{% endblock %}</title>
  {% load staticfiles %}
  <link rel="stylesheet" type="text/css" href="{% static 'priceAnalysis/style.css' %}" />
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" />
  <link href="https://fonts.googleapis.com/css?family=Satisfy" rel="stylesheet" type="text/css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootsrap.min.js"></script>
</head>
<body>
  <nav class="navbar navbar-inverse">
    <div class="container-fluid">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#topNavBar">
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <a class="navbar-brand" href="{% url 'priceAnalysis:index' %}">PriceAnalysis</a>
      </div>

      <div class="collapse navbar-collapse">
        <ul class="nav navbar-nav">
          <li class={% block index_active %}{% endblock %}>
            <a href="{% url 'priceAnalysis:index' %}">
              <span class="glyphicon glyphicon-signal"aria-hidden="true">
              </span>&nbsp;Charts
            </a>
          </li>
          <li class={% block list_active %}{% endblock %}>
            <a href="{% url 'priceAnalysis:list' %}">
              <span class="glyphicon glyphicon-list-alt"aria-hidden="true">
              </span>&nbsp;Database
            </a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
{% block body %}
{% endblock %}
</body>
</html>
