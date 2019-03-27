from django.test import TestCase

from rest_api.utils import get_keywords_from_keywords_generation_server


class UrlUtilTestCase(TestCase):

    def test_get_keywords_from_keywords_generation_server(self):
        self.assertEqual(get_keywords_from_keywords_generation_server('https://www.google.com'), ['Google'])
