#!/usr/bin/python

from urllib2 import Request, urlopen, URLError, HTTPError

def main():
    public = 1;
    tipe = "city";
    lid = 2;
    m = 11;
    y = 2016;
    sourceUrl = "http://infopangan.jakarta.go.id/api/price/series_by_location?";
    finalUrl = sourceUrl + "public=" + str(public) + "&type=" + tipe + "&lid=" + str(lid) + "&m=" + str(m) + "&y=" + str(y);
    req = Request(finalUrl);
    file = open('source.txt','w');
    try:
        response = urlopen(req)
    except HTTPError as e:
        print 'The server couldn\'t fulfill the request.'
        print 'Error code: ', e.code
    except URLError as e:
        print 'We failed to reach a server.'
        print 'Reason: ', e.reason
    else:
        string = response.read();
        file.write(string);
        print 'everthing is fine'

    file.close();

if __name__ == '__main__':
    main();






awk -F '{"name":' '{for(i=2 ; i <= NF ; i++) {print $i}}' source.txt | grep "Cabe Merah" | sed 's/[{}"]//g' | sed 's/,/ | /g' | sed 's/series://g' | awk -F'|' '{printf("%s",$1)}; {for(i=8 ; i<NF ; i++){printf("%s ",$i);}{printf("\n");}}'





awk -F '{"name":' '{for(i=2 ; i <= NF ; i++) {print $i}}' $source | grep "Cabe Merah" | sed 's/[{}"]//g' | sed 's/,/| /g' | sed 's/series://g' | sed 's/[0-9]://g' | awk -F'|' '{printf("%s ",$1)}; {for(i=8 ; i<NF ; i++){printf("%d ",$i);}{printf("\n");}}'





--isi views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World. You're at the polls index.")




--isi urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
]
