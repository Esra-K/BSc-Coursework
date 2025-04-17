from django.test import TestCase , Client
from django.urls import reverse
from shabook.models import PostManager , Book , Message
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.shabookHome_url = reverse('shabook-home')
        self.shabookHome1_url = reverse('shabook-home1')
        self.Search_url = reverse('query')


    def test_shabookHome_GET(self):
        response = self.client.get(self.shabookHome_url)

        self.assertEquals(response.status_code , 200)
        self.assertTemplateUsed(response , 'shabook/homepage/home.html')


    def test_shabookHome1_GET(self):
        response = self.client.get(self.shabookHome1_url)

        self.assertEquals(response.status_code , 200)
        self.assertTemplateUsed(response , 'shabook/home.html')

    def test_Search_GET(self):
        response = self.client.get(self.Search_url)

        self.assertEquals(response.status_code , 200)
        self.assertTemplateUsed(response , 'shabook/view.html')
