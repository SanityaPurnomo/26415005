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





--coba html dari bokeh
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Experiment with Bokeh</title>
    <script src="http://cdn.pydata.org/bokeh/release/bokeh-0.11.0.min.js"></script>
    <link rel="stylesheet" href="http://cdn.pydata.org/bokeh/release/bokeh-0.11.0.min.css">
    {{the_script|safe}}
</head>
<body>

    {{the_div|safe}}

</body>
</html>





--coba standalone html bokeh--
rom bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html

plot = figure()
plot.circle([1,2], [3,4])

html = file_html(plot, CDN, "my plot")





--coba graph di bokeh
from bokeh.plotting import figure, output_file, show

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 7, 3]

output_file("multiple.html")

p = figure(plot_width=400, plot_height=400)

# add both a line and circles on the same plot
p.line(x, y, line_width=2)
p.circle(x, y, fill_color="white", size=8)

show(p)
