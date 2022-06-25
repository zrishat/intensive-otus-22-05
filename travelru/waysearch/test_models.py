from django.test import TestCase
from waysearch.models import Country, City, Airport

class CountryTestCase(TestCase):
    def setUp(self):
        Country.objects.create(db_id=2, name_rus="США", name_eng="USA", code_eng="USA")
        Country.objects.create(db_id=3, name_rus="Великобритания", name_eng="Greate Britain", code_eng="GBR")

    def test_country_fields(self):
        """Country objects created correctry"""
        USA = Country.objects.get(name_rus="США")
        GBR = Country.objects.get(name_rus="Великобритания")
        self.assertEqual(USA.db_id, 2)
        self.assertEqual(USA.name_rus, "США")
        self.assertEqual(USA.name_eng, "USA")
        self.assertEqual(USA.code_eng, "USA")
        self.assertEqual(str(USA), "США")
        self.assertTrue(isinstance(USA, Country))

        self.assertNotEqual(GBR.db_id, 2)
        self.assertNotEqual(GBR.name_rus, "США")
        self.assertNotEqual(GBR.name_eng, "USA")
        self.assertNotEqual(GBR.code_eng, "USA")
        self.assertNotEqual(GBR.name_rus, "США")