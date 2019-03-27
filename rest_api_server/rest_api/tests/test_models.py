from django.test import TestCase

from rest_api.models import Url as UrlModel


class UrlModelTestCase(TestCase):

    def test_create_url(self):
        url = UrlModel()
        url.url = 'https://www.google.com'
        self.assertTrue(url.save())

    def test_read_url(self):
        url = UrlModel.objects.get(url='https://www.google.com')
        self.assertEqual(url.url, 'https://www.google.com')

    def test_update_url(self):
        url = UrlModel.objects.get(url='https://www.google.com')
        url.url = "https://translate.google.com/"
        self.assertTrue(url.save())

    def test_delete_url(self):
        self.assertTrue(UrlModel.objects.get(url="https://translate.google.com/").delete())
