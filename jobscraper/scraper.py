import requests
from bs4 import BeautifulSoup
import urllib


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
    params = urllib.urlencode({'q': title, 'sort': 'create_time+desc'})
    myurl = "https://www.upwork.com/o/jobs/browse/?%s" % params
    print "url is", myurl
    # try:
    req = requests.get(
        myurl, headers=hdr)
    return req.text
    # except:
        # raise


def scrape(job):
    jobs = scrape_content(job)
    soup = BeautifulSoup(jobs, "html.parser")
    # print "jobs are", soup
    job_body = soup.find("div", {"id": "jobs-list"})
    jobs = job_body.find_all('article')
    # print "all jobs are", jobs
    total_jobs = {}
    for each_job in jobs:
        job_dict = {}
        job_link = each_job.find('a')
        dict_id = job_link['data-position']
        job_dict['title'] = job_link.text.strip()
        print "job_link", job_link['href']
        job_href = job_link['href']
        job_href = job_href.split('/')
        job_href = job_href[4]
        job_dict['link'] = "https://www.upwork.com/jobs/_" + job_href
        total_jobs[dict_id] = job_dict

    # job_link = jobs[0].find('a')
    # print "job_link", job_link['href'], job_link.text.strip()
    print "job_dict is", total_jobs


if __name__ == '__main__':
    scrape('python')
