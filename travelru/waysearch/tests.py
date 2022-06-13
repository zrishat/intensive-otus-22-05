"""
tests
"""
from django.test import TestCase
from django.urls import resolve, reverse
from waysearch.views import index, search_avia_page, search_train_page

# Create your tests here.


class UrlTests(TestCase):
    """
    UrlTests
    """
    def test_index_page(self):
        """
        test_index_page
        """
        url = reverse('waysearch:index')
        # url is available
        response = self.client.get(url)
        self.assertEqual(
            response.status_code, 200, msg=f"{url} is  NOT available")
        # url correspond to right view
        self.assertEqual(resolve(url).func, index)
        # url correspond to the right template
        self.assertTemplateUsed(response, 'waysearch/index.html')

    def test_search_avia_page(self):
        """
        test_search_avia_page
        """
        url = reverse('waysearch:search_avia')
        # url is available
        response = self.client.get(url)
        self.assertEqual(
            response.status_code, 200, msg=f"{url} is  NOT available")
        # url correspond to right view
        self.assertEqual(resolve(url).func, search_avia_page)
        # url correspond to the right template
        self.assertTemplateUsed(response, 'waysearch/search_avia.html')

    def test_search_train_page(self):
        """
        test_search_train_page
        """
        url = reverse('waysearch:search_train')
        # url is available
        response = self.client.get(url)
        self.assertEqual(
            response.status_code, 200, msg=f"{url} is  NOT available")
        # url correspond to right view
        self.assertEqual(resolve(url).func, search_train_page)
        # url correspond to the right template
        self.assertTemplateUsed(response, 'waysearch/search_train.html')
