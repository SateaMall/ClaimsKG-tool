from django.shortcuts import render
from django.http import HttpResponse
from .sparql_queries import fetch_concept_counts, fetch_claims_presidents, fetch_mixed_claims_politifact, fetch_claims_coronavirus_2020
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
import json

from django.http import JsonResponse

@api_view(['GET'])
def politifact_view(request):
    data = fetch_mixed_claims_politifact()
    return JsonResponse({'data': data}, json_dumps_params={'indent': 4})

@api_view(['GET'])
def counts_view(request):
    data = fetch_concept_counts()
    return JsonResponse({'data': data}, json_dumps_params={'indent': 4})

@api_view(['GET'])
def coronavirus_view(request):
    data = fetch_claims_coronavirus_2020()
    return JsonResponse({'data': data}, json_dumps_params={'indent': 4})

@api_view(['GET'])
def presidents_view(request):
    data = fetch_claims_presidents()
    return JsonResponse({'data': data}, json_dumps_params={'indent': 4})
