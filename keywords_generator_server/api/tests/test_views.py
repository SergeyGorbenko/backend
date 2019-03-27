from django.test import TestCase
from django.urls import reverse


class ViewsTests(TestCase):

    def test_main_API_view(self):
        resp = self.client.get(reverse('API'))
        self.assertEqual(resp.status_code, 200)

    def test_get_keywords_view(self):
        resp = self.client.get(reverse('keywords_generator'))
        self.assertEqual(resp.status_code, 405)

    def test_good_post_keywords_view(self):
        resp = self.client.post('http://127.0.0.1:8000/keywords_generator/api/keywords/',
                                data={'url': 'https://devchallenge.it'})
        self.assertEqual(resp.status_code, 202)

    def test_bed_host_post_keywords_view(self):
        resp = self.client.post('http://127.0.0.1:8000/keywords_generator/api/keywords/',
                                data={'url': 'https://bad_host_devchallenge.it'})
        self.assertEqual(resp.status_code, 400)

    def test_bed_path_post_keywords_view(self):
        resp = self.client.post('http://127.0.0.1:8000/keywords_generator/api/keywords/',
                                data={'url': 'https://devchallenge.it/bad_path'})
        self.assertEqual(resp.status_code, 400)
