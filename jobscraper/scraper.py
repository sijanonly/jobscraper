import requests
import urllib
import xmltodict


UPWORK_FEED = "https://www.upwork.com/jobs/rss?q={0}"


def scrape_content(title):
    hdr = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11'
        ' (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9'
        ',*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'
    }
    # params = urllib.urlencode({'q': title, 'sort': 'create_time+desc'})
    myurl = UPWORK_FEED.format(urllib.quote(title))
    print "url is", myurl
    # try:
    req = requests.get(
        myurl, headers=hdr)
    return req.text


def scrape(job):
    jobs = scrape_content(job)
    return dict(xmltodict.parse(jobs))


if __name__ == '__main__':
    scrape('python')
