from django.test import TestCase, Client
from django.urls import resolve
from home.views import home_page

class HomeTests(TestCase):
    def test_root_url_resolves_to_homepage_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)