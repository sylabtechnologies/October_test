# Webcrawler.py
import sys
import urllib.request
import html
import io

# print message
def std_log(msg):
    print(msg)

# retrieve URL    
def get_page(url, log):
    try:
        page = urllib.request.urlopen(url)
    except urllib.URLError:
        log("Error retrieving: " + url)
        return ''
    body = page.read()
    page.close()
    return body    

lkd = "https://www.linkedin.com/jobs/matlab-jobs"

std_log(myurl)
print(get_page(myurl, std_log))