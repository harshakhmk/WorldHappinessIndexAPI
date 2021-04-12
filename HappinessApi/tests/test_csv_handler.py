from django.test import TestCase,SimpleTestCase
from HappinessApi.CSV_Handler import*

class TestCsvExecutor(SimpleTestCase):
    def setUp(self):
        self.csv_obj=CsvExecuter()

    def test_get_country_details(self,country='Peru'): 
        output = self.csv_obj.get_country_details(country)
        assert type(output)==dict
    def test_get_countries_within_scores(self,from_score=7.5,to_score=9.9): 
        output = self.csv_obj.get_countries_within_scores(from_score,to_score)
        assert type(output)==list    