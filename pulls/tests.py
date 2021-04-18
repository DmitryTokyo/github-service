from django.test import TestCase
from django.urls import reverse


class IndexPageView(TestCase):
    def test_index_page_view_status_code(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200) 