from django.test import TestCase
from .models import *
from django.urls import reverse

# Create your tests here.

class QuoteModelTest(TestCase):

    def setUp(self):
        Quote.objects.create(text='Just a test', author = 'by test')
        
    def test_text_content(self):
        quote=Quote.objects.get(id=1)
        expected_object_name = f'{Quote.text}'
        self.assertEqual(expected_object_name, 'Just a test')

class HomePageViewTest(TestCase):
    def setUp(self):
        Quote.objects.create(text='Second test')
    
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
    
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
    
    def test_view_uses_corrext_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
# Create your tests here.
