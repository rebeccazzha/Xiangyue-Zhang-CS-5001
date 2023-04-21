from django.test import RequestFactory, TestCase
from django.urls import reverse
from app01.models import Thumbnail
from app01.views import (home, welcome, popular, base, vodka, whiskey, rum, tequila, gin, mixed, brandly)


class TestViews(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_home(self):
        request = self.factory.get(reverse('home'))
        response = home(request)
        self.assertEqual(response.status_code, 200)

    def test_welcome(self):
        request = self.factory.get(reverse('welcome'))
        response = welcome(request)
        self.assertEqual(response.status_code, 200)

    def test_popular(self):
        request = self.factory.get(reverse('popular'))
        response = popular(request)
        self.assertEqual(response.status_code, 200)

    def test_base(self):
        request = self.factory.get(reverse('base'))
        response = base(request)
        self.assertEqual(response.status_code, 200)

    def test_vodka(self):
        request = self.factory.get(reverse('vodka'))
        response = vodka(request)
        self.assertEqual(response.status_code, 200)

    def test_whiskey(self):
        request = self.factory.get(reverse('whiskey'))
        response = whiskey(request)
        self.assertEqual(response.status_code, 200)

    def test_rum(self):
        request = self.factory.get(reverse('rum'))
        response = rum(request)
        self.assertEqual(response.status_code, 200)

    def test_tequila(self):
        request = self.factory.get(reverse('tequila'))
        response = tequila(request)
        self.assertEqual(response.status_code, 200)

    def test_gin(self):
        request = self.factory.get(reverse('gin'))
        response = gin(request)
        self.assertEqual(response.status_code, 200)

    def test_mixed(self):
        request = self.factory.get(reverse('mixed'))
        response = mixed(request)
        self.assertEqual(response.status_code, 200)

    def test_brandly(self):
        request = self.factory.get(reverse('brandly'))
        response = brandly(request)
        self.assertEqual(response.status_code, 200)
