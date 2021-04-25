from django.urls import reverse, resolve
from django.test import Client
import pytest
from pytest_django.asserts import assertTemplateUsed, assertRedirects


@pytest.mark.django_db
class TestViews:
    client = Client()
    index_url = reverse('index')

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
    