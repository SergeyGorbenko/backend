from django.test import TestCase

from api.forms import UrlForm


class FormsTests(TestCase):

    def test_good_url(self):
        form = UrlForm({'url': 'https://devchallenge.it'})
        self.assertTrue(form.is_valid())

    def test_bed_host(self):
        form = UrlForm({'url': 'https://bad_url_devchallenge.it'})
        self.assertFalse(form.is_valid())

    def test_bed_path(self):
        form = UrlForm({'url': 'https://devchallenge.it/bad_path/'})
        self.assertFalse(form.is_valid())
