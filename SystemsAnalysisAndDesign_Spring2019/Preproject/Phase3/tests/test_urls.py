from django.test import SimpleTestCase
from django.urls import reverse , resolve
from shabook.views import home , BookListView , SearchView


class TestUrls(SimpleTestCase):

    def test_shabookHome_url_is_resolved(self):
        url = reverse('shabook-home')
        self.assertEquals(resolve(url).func , home)

    def test_shabookHome1_url_is_resolved(self):
        url = reverse('shabook-home1')
        self.assertEquals(resolve(url).func.view_class , BookListView)

    def test_Search_url_is_resolved(self):
        url = reverse('query')
        self.assertEquals(resolve(url).func.view_class , SearchView)
