from django.test import TestCase, Client
from django.urls import reverse, resolve

from pulls.views import index, get_projects, get_project_pulls


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')


    def test_index_page_GET(self):
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    

    def test_index_post(self):
        response = self.client.post(self.index_url, {
            'username': 'buddy'
        })
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/buddy/repositories')
        