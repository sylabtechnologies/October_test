# PY2
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

mylink = "https://api.nexchange.io/en/api/v1/price/BTCUSD/latest/?market_code=nex"

log_stdout(mylink + ":")

result = get_page(mylink, log_stdout)
d = json.loads(result[1:-1])
price = d["ticker"]

print "bid:\t", price["bid"]
print "ask:\t", price["ask"]
