from django.shortcuts import render
from .models import Country
from django.http import HttpResponseNotFound
import json
from rest_framework import status    
from rest_framework.response import Response
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import CountrySerializer
# Create your views here.
def error404(request, exception=None):
    
    return JsonResponse({
        'status_code': 404,
        'error': 'The resource was not found'
    },safe=False,status=404)

def error500(request, exception=None):
    return JsonResponse({
        'status_code': 500,
        'error': 'Internal Server Error'
    },safe=False)

def error400(request, exception=None):
    return JsonResponse({
        'status_code': 400,
        'error': 'Bad Request'
    },status=status.HTTP_400_BAD_REQUEST)
def error403(request, exception=None):
    return JsonResponse({
        'status_code': 403,
        'error': 'Request Forbidden'
    },status=status.HTTP_403_FORBIDDEN)


def CountryData(request,country):
    
    country=get_object_or_404(Country,CountryName=country)
    serializer=CountrySerializer(country)
    return JsonResponse(serializer.data, safe=False)  

def ScoreData(request,from_score,to_score):
    from_score=float(from_score)
    to_score=float(to_score)
    countries_score=Country.objects.filter(LadderScore__gte=from_score,LadderScore__lte=to_score)
    serializer=CountrySerializer(country,many=True)
    return JsonResponse(serializer.data, safe=False)

