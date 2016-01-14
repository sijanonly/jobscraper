jobscraper
--------

![Travis Build](https://travis-ci.org/sijanonly/jobscraper.svg)

	>>> pip install jobscraper


To use, simply do::

    >>> from jobscraper import scrape
    >>> jobs = scrape('python')


'jobs' is a dictionary of jobs with keys (1,2,........10) top 10 jobs.

	>>> jobs['1']
