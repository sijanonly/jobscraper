import requests
import urllib
import xmltodict


UPWORK_FEED = "https://www.upwork.com/jobs/rss?q={0}"


def scrape_content(title):
    # params = urllib.urlencode({'q': title, 'sort': 'create_time+desc'})
    myurl = UPWORK_FEED.format(urllib.quote(title))
    print("url is", myurl)
    # try:
    req = requests.get(myurl)
    return req.text


def scrape(job):
    jobs = scrape_content(job)
    return dict(xmltodict.parse(jobs))


if __name__ == '__main__':
    scrape('python')
