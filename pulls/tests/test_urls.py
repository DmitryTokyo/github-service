from django.urls import reverse, resolve

from pulls.views import IndexView, RepositoriesView, PullsView


class TestUrls:

    def test_index_url(self):
        path = reverse('index')
        assert resolve(path).func.view_class == IndexView
    
    def test_repositories_url(self):
        path = reverse('repositories', kwargs={'username': 'dude'})
        assert resolve(path).func.view_class == RepositoriesView
    
    def test_pulls_url(self):
        path = reverse('pulls', kwargs={'username': 'dude', 'repository_name': 'super'})
        assert resolve(path).func.view_class == PullsView