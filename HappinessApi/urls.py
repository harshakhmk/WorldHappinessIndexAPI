from django.urls import path,include,register_converter
from .views import *
from . import converters


register_converter(converters.FloatUrlParameterConverter, 'float')

urlpatterns = [
   path('country/<str:country>',CountryData,name="countryData"),
   #path('score-range/?<float:from_score>',ScoreData,name="scoreRange"),
   #path(r"^score-range/(?P<from_score>\d+\.\d+)$/(?P<to_score>\d+\.\d+)$", ScoreData, name="scoreRange"),
   path('score-range/?from=<str:from_score>&to=<str:to_score>',ScoreData, name="scoreRange"),

]
