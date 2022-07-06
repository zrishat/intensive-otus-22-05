from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse, resolve

from search_hotels.views import search_hotels



class UrlTests(TestCase):
    """
    UrlTests
    """
    def setUp(self):
        self.search_data = {
            'city': 'Москва',
            'check_in': '2022-11-01',
            'check_out': '2022-11-03',
            'guests': '2'
        }

    def test_get_page(self):
        response = self.client.get('/search_hotels/')

        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'Поиск отелей')

    def test_search_hotels(self):

        with patch('search_hotels.views.get_hotels_data') as get_hotels_data:
            get_hotels_data.return_value = [{'name': 'hotel_name',
                              'stars': '5',
                              'hotel_type': 'с бассейном',
                              'price': '5000',
                              'nights': '3',
                              'check_in': '2022-11-05',
                              'check_out': '2022-11-08',
                              'amount_guests': '2'}]
            response = self.client.post(
                '/search_hotels/',
                data={
                    'city': self.search_data['city'],
                    'check_in': self.search_data['check_in'],
                    'check_out': self.search_data['check_out'],
                    'guests': self.search_data['guests']
                }
            )
        self.assertEqual(200, response.status_code)
        # self.assertContains(response, 'с бассейном')
