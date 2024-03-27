from django.urls import path
from . import views 
from django.contrib import admin
from django.urls import path,include

urlpatterns =[
    path('admin/',admin.site.urls),
    path('',include('ClaimsKG.urls'))
    # path('count/', views.concept_count),
    # path('presidents/', views.presidents_view, name='presidents'),
    # path('politifact/', views.politifact_view, name='politifact'),
    # path('coronavirus/', views.coronavirus_view, name='coronavirus'),
]