from django.urls import path,include,register_converter,re_path
from .views import *


urlpatterns = [
   
   path('country/<str:country>',CountryData.as_view(),name="CountryData"),
   path('score-range/',CountryList.as_view(),name="ScoreRange"),
   

]
