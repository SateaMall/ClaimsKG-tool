from django.urls import path
from . import views 

urlpatterns =[
    path('count/', views.concept_count),
    path('presidents/', views.presidents_view, name='presidents'),
    path('politifact/', views.politifact_view, name='politifact'),
    path('coronavirus/', views.coronavirus_view, name='coronavirus'),
]