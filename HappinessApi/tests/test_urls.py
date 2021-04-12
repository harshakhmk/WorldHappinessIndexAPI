from django.urls import reverse,resolve
from django.test import SimpleTestCase
from HappinessApi.views import *
class TestUrls(SimpleTestCase):

    def test_country_data_url(self):
        url=reverse('CountryData',args=['Peru'])
       # print(resolve(url))
        assert resolve(url).view_name == 'CountryData'
    def test_countries_score_url(self):
        url=reverse('ScoreRange')
        assert resolve(url).view_name == 'ScoreRange'  