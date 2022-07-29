#from django.test import TestCase
from django.test import SimpleTestCase
from django.http import HttpRequest
from django.urls import reverse, resolve
#from django.

from . import views

# Create your tests here.

#Testing homepage return status code - whether page exist or notation

class HomePageTest(SimpleTestCase):

    def test_home_page_exist(self):
        response = self.client.get('/')
        print(response)
        self.assertEquals(response.status_code, 200)

    def test_home_page_charset(self):
        response=self.client.get('/')
        self.assertEquals(response.charset, 'ASCII')

    def test_home_page_scheme(self):
        response=self.client.get('/')
        self.assertEquals(response.headers['Content-Type'], 'text/html; charset=ASCII')


    def test_home_page_url(self):
        url=self.client.get('/')
        print(url)
        url_rev=reverse('welcome')
        print(url_rev)
        print('REsolve:', resolve(url_rev))
