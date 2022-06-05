from django.test import TestCase
from django.urls import resolve, reverse
from waySearch.views import index, search_avia_page, search_train_page

# Create your tests here.


class UrlTests(TestCase):

    def test_index_page(self):

        url = reverse('waySearch:index')
        # url is available
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, msg=f"{url} is  NOT available")
        # url correspond to right view
        self.assertEqual(resolve(url).func, index)
        # url correspond to the right template
        self.assertTemplateUsed(response, 'waySearch/index.html')

    def test_search_avia_page(self):
        url = reverse('waySearch:search_avia')
        # url is available
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, msg=f"{url} is  NOT available")
        # url correspond to right view
        self.assertEqual(resolve(url).func, search_avia_page)
        # url correspond to the right template
        self.assertTemplateUsed(response, 'waySearch/search_avia.html')

    def test_search_train_page(self):
        url = reverse('waySearch:search_train')
        # url is available
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, msg=f"{url} is  NOT available")
        # url correspond to right view
        self.assertEqual(resolve(url).func, search_train_page)
        # url correspond to the right template
        self.assertTemplateUsed(response, 'waySearch/search_train.html')