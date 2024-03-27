from django.shortcuts import render
from django.http import HttpResponse
from .sparql_queries import fetch_concept_counts, fetch_claims_presidents, fetch_mixed_claims_politifact, fetch_claims_coronavirus_2020
import matplotlib.pyplot as plt
from io import BytesIO
import base64

import matplotlib.pyplot as plt
from io import BytesIO
import base64

def concept_count(request):
    # Récupérer les données de comptage des concepts
    concept_data = fetch_concept_counts()
    
    # Extraire les sources et les comptes
    sources = [concept['type'] for concept in concept_data]
    counts = [concept['count'] for concept in concept_data]
    
    # Trier les sources et les comptes par ordre croissant de comptes
    sources_sorted, counts_sorted = zip(*sorted(zip(sources, counts), key=lambda x: x[1]))
    
    # Créer le graphique
    plt.figure(figsize=(10, 6))
    plt.barh(range(len(counts_sorted)), counts_sorted)
    plt.yticks(range(len(counts_sorted)), sources_sorted)
    plt.xlabel('Compte')
    plt.ylabel('Sources (Liens)')
    plt.title('Nombre de compte par source (trié)')
    plt.tight_layout()
    
    # Enregistrer le graphique dans un fichier BytesIO
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    
    # Convertir l'image en base64
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    
    # Créer la réponse HTTP avec l'image
    response = HttpResponse(content_type='text/html')
    response.write('<img src="data:image/png;base64,{}">'.format(image_base64))
    
    return response

def presidents_view(request):
    claims_data = fetch_claims_presidents()

    # Comptage du nombre d'articles par président
    article_counts = {}
    for claim in claims_data:
        president = claim['President']
        if president not in article_counts:
            article_counts[president] = 0
        article_counts[president] += 1

    # Extraction des noms de président et des nombres d'articles
    presidents = list(article_counts.keys())
    counts = list(article_counts.values())

    # Création du graphique avec des barres horizontales
    plt.barh(presidents, counts)
    plt.xlabel('Nombre d\'articles')
    plt.ylabel('Président')
    plt.title('Nombre d\'articles par président')

    # Conversion du graphique en image
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    plt.close()

    # Récupération des données de l'image
    image_stream.seek(0)
    image_data = image_stream.getvalue()

    # Renvoi de l'image en réponse HTTP
    response = HttpResponse(content_type='image/png')
    response.write(image_data)

    return response

def politifact_view(request):
    data = fetch_mixed_claims_politifact()
    return render(request, 'politifact.html', {'data': data})

def coronavirus_view(request):
    data = fetch_claims_coronavirus_2020()
    return render(request, 'coronavirus.html', {'data': data})