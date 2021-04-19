from django.test import TestCase
from django.urls import reverse, resolve

from .views import index, get_projects, get_project_pulls


class IndexPageView(TestCase):
    def test_index_page_view_status_code(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)
    

    def test_repositories_url_is_resolved(self):
        url = reverse('repositories', kwargs={'username': 'buddy'})
        self.assertEquals(resolve(url).func, get_projects)


    def test_pulls_url_is_resolved(self):
        url = reverse('pulls', kwargs={'username': 'buddy', 'repository_name': 'thebest'})
        self.assertEquals(resolve(url).func, get_project_pulls)