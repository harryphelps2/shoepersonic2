from django.test import TestCase, Client

class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1+1, 3)

# class HomeTests(TestCase):
#     """
#     Tests for home page.
#     """
#     def test_home_page_happy_path(self):
#         client = Client()
#         response = client.get('/')
#         self.assertEqual(response.status_code, 200)