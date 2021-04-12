from django.shortcuts import render
from django.http import HttpResponseNotFound
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status    
from rest_framework.response import Response
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import CountrySerializer
from .CSV_Handler import *


country_obj=CsvExecuter()

class CountryData(APIView):

    def get(self,request,country):
       # country_name = self.request.query_params.get('country',None)
        country_data={
            'data':country_obj.get_country_details(country)
          } 
        return JsonResponse(country_data, safe=False)  

class CountryList(APIView):

    def get(self,request):
        
        from_score=request.query_params.get('from', None)
        to_score=request.query_params.get('to', None)
        
        from_score=float(from_score)
        to_score=float(to_score)

        
        
        if from_score is not None and to_score is not None:
            country_data={
               'data':country_obj.get_countries_within_scores(from_score,to_score)
            } 
            return JsonResponse(country_data, safe=False)   
        else:
             return JsonResponse({'detail':'Query Paramas Cannot be null',
             'status_code':400,
             'error':'BAD REQUEST'
             })    

    
