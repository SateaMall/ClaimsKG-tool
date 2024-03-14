from django.shortcuts import render
from django.http import HttpResponse
from .sparql_queries import fetch_concept_counts, fetch_claims_presidents, fetch_mixed_claims_politifact, fetch_claims_coronavirus_2020

# Create your views here.
# 
# def test(request): 
#     return HttpResponse('Hello World')


def concept_count(request):    
    concept_data = fetch_concept_counts()
    return render(request, 'concept_count.html', {'concepts': concept_data})

def presidents_view(request):
    data = fetch_claims_presidents()
    return render(request, 'presidents.html', {'data': data})

def politifact_view(request):
    data = fetch_mixed_claims_politifact()
    return render(request, 'politifact.html', {'data': data})

def coronavirus_view(request):
    data = fetch_claims_coronavirus_2020()
    return render(request, 'coronavirus.html', {'data': data})