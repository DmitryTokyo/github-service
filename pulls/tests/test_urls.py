from django.test import TestCase
from django.urls import reverse, resolve

from pulls.views import index, get_projects, get_project_pulls


class TestUrls(TestCase):

    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)
        
    
    def test_repositories_url_is_resolved(self):
        url = reverse('repositories', args={'username': 'buddy'})
        self.assertEquals(resolve(url).func, get_projects)
        
    
    def test_pulls_url_is_resolved(self):
        url = reverse('pulls', args={'username': 'buddy', 'repository_name': 'thebest'})
        self.assertEquals(resolve(url).func, get_project_pulls)