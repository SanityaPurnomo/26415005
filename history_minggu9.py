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
