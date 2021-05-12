from django.urls import reverse, resolve
from django.test import Client
import pytest
from pytest_django.asserts import assertTemplateUsed, assertRedirects
from django.core.cache import cache


@pytest.mark.django_db
class TestViews:
    client = Client()
    index_url = reverse('index')
    pulls_url = reverse('pulls', kwargs={'username': 'DmitryTokyo', 'repository_name': 'some-test'})

    def test_index_get_view(self):
        response = self.client.get(self.index_url)
        assert response.status_code == 200
        assertTemplateUsed(response, 'index.html')
    
    def test_index_post_view(self):
        response = self.client.post(self.index_url, {
            'username': 'buddy'
        })
        assert response.status_code == 302
        assertRedirects(response, '/buddy/repositories')

    def test_repositories_get_view(self):
        repositories_url = reverse('repositories', kwargs={'username': 'dude'})
        response = self.client.get(repositories_url)
        assert response.status_code == 200
        assertTemplateUsed(response, 'repositories.html')
    
    def test_pulls_get_view(self):
        response = self.client.get(self.pulls_url)
        assert response.status_code == 200
        assertTemplateUsed(response, 'pull_requests.html')
    
    def test_pulls_post_view(self):
        response = self.client.post(self.pulls_url, {
            'is_merged': 'unmerged pulls'
        })
        assert response.status_code == 302
    
    def test_repositories_unavailable_username_redirect(self):
        repositories_url = reverse('repositories', kwargs={'username': ';;;;;'})
        response = self.client.get(repositories_url)
        assert response.status_code == 302
        assertRedirects(response, self.index_url)