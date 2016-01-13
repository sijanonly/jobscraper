from unittest import TestCase

from jobscraper.scraper import scrape


class TestScrape(TestCase):
    def test_is_dict(self):
        s = scrape('python')
        self.assertTrue(isinstance(s, dict))
