from django.test import RequestFactory, TestCase,Client
from django.urls import reverse,resolve

# query params are not sent in reverse function because they are dealt at runtime

class TestCountryListView(TestCase):
    def setUp(self):
        self.client = Client()
        self.CountryData = reverse('CountryData',args=['Peru'])
        self.ScoreRange=reverse('ScoreRange')
    def test_country_details_view(self):
        
        response=self.client.get(self.CountryData)
        self.assertEquals(response.status_code,200)
    
    def test_country_list_view(self):
        
        response=self.client.get(self.ScoreRange,{'from':'7.5','to':'7.9'})
        self.assertEquals(response.status_code,200)
    
