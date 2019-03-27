from django.test import TestCase

from api.utils import check_url, get_title, generate_keywords_list


class UtilsTests(TestCase):

    def test_check_url(self):
        self.assertTrue(check_url("https://devchallenge.it"))

    def test_get_title(self):
        self.assertEqual(get_title(check_url("https://devchallenge.it")), "DEV Challenge")

    def test_generate_keywords_list(self):
        self.assertEqual(generate_keywords_list("DEV Challenge"), ["DEV", "Challenge", "DEV Challenge"])
