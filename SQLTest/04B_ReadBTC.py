#PY2

import json
import sys
import urllib2
import urlparse
import htmllib, formatter
from cStringIO import StringIO

def log_stdout(msg):
    print msg

def get_page(url, log):
    try:
        page = urllib2.urlopen(url)
    except urllib2.URLError:
        log("Error retrieving: " + url)
        return ''
    body = page.read()
    page.close()
    return body

mylink = "https://api.nexchange.io/en/api/v1/pair/"

pairPage = get_page(mylink, log_stdout)
pairs = pairPage[1:-1].split("{")

print "{"

for x in pairs[1:-1] :
    dd = json.loads("{" + x[:-1])
    pairStr = str(dd["name"])

    if pairStr.find("USD") != -1 :
        datalink = "https://api.nexchange.io/en/api/v1/price/" + pairStr + "/latest/?market_code=nex"
        result = get_page(datalink, log_stdout)
        if len(result) > 0 :
            dTicker = json.loads(result[1:-1])
            price = dTicker["ticker"]
            sys.stdout.write("{ \"pair\": \"")
            sys.stdout.write(pairStr)
            sys.stdout.write("\",\n")
            sys.stdout.write("  \"ticker\": \"")
            sys.stdout.write(str(price))
            sys.stdout.write("\" },\n")

print "}"
