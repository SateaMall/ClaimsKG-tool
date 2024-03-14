from SPARQLWrapper import SPARQLWrapper, JSON


def fetch_concept_counts():
    sparql = SPARQLWrapper("https://data.gesis.org/claimskg/sparql") 
    sparql.setQuery("""
        SELECT ?type (COUNT(DISTINCT ?x) AS ?count) WHERE {
            GRAPH <http://data.gesis.org/claimskg> {
                ?x a ?type.
            }
        } GROUP BY ?type
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    concept_counts = []
    for result in results["results"]["bindings"]:
        concept_counts.append({
            'type': result["type"]["value"],
            'count': result["count"]["value"]
        })

    return concept_counts

##########################################################
##########################################################

def fetch_claims_presidents():
    sparql = SPARQLWrapper("https://data.gesis.org/claimskg/sparql")  # replace with your endpoint
    sparql.setQuery("""
        PREFIX itsrdf: <https://www.w3.org/2005/11/its/rdf#>
		PREFIX schema: <http://schema.org/>
		PREFIX dbr: <http://dbpedia.org/resource/>
		PREFIX dbo: <http://dbpedia.org/ontology/>
		PREFIX nee: <http://www.ics.forth.gr/isl/oae/core#>
		PREFIX dc: <http://purl.org/dc/terms/>
    SELECT DISTINCT ?text ?reviewurl ?President 
    WHERE { 
    SERVICE <http://dbpedia.org/sparql> 
    {?President <http://dbpedia.org/property/office> "President of the United States"@en .
    ?President <http://dbpedia.org/property/party> <http://dbpedia.org/resource/Democratic_Party_(United_States)> .}
    ?claim a schema:CreativeWork . 
    ?claimReview schema:itemReviewed ?claim ;schema:url ?reviewurl .
    ?claim schema:text ?text ; schema:mentions ?entity1 . 
    ?entity1 <https://www.w3.org/2005/11/its/rdf#taIdentRef> ?President.
    }
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    claims_data = []
    for result in results["results"]["bindings"]:
        claims_data.append({
            'text': result["text"]["value"],
            'reviewurl': result["reviewurl"]["value"],
            'President': result["President"]["value"]
        })

    return claims_data

##########################################################
##########################################################

def fetch_mixed_claims_politifact():
    sparql = SPARQLWrapper("https://data.gesis.org/claimskg/sparql")  # replace with your endpoint
    sparql.setQuery("""
        PREFIX itsrdf:<https://www.w3.org/2005/11/its/rdf#>
        PREFIX schema:<http://schema.org/>

        SELECT ?text ?reviewurl WHERE {
            ?claim a schema:CreativeWork .
            ?claim schema:text ?text .
            ?claimReview schema:itemReviewed ?claim ; 
                        schema:reviewRating <http://data.gesis.org/claimskg/rating/normalized/claimskg_MIXTURE> ; 
                        schema:url ?reviewurl ;
                        schema:author <http://data.gesis.org/claimskg/organization/politifact> .
        }
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    claims_data = []
    for result in results["results"]["bindings"]:
        claims_data.append({
            'text': result["text"]["value"],
            'reviewurl': result["reviewurl"]["value"]
        })

    return claims_data


##########################################################
##########################################################

def fetch_claims_coronavirus_2020():
    sparql = SPARQLWrapper("https://data.gesis.org/claimskg/sparql")  # replace with your endpoint
    sparql.setQuery("""
        PREFIX itsrdf:<https://www.w3.org/2005/11/its/rdf#>
        PREFIX schema:<http://schema.org/>
        PREFIX dbr:<http://dbpedia.org/resource/>
        PREFIX au:<http://data.gesis.org/claimskg/organization/claimskg>
        SELECT ?text ?date ?reviewurl ?ratingName
        WHERE {
        ?claim a schema:CreativeWork ;
                schema:datePublished ?date FILTER(year(?date)=2020)
        ?claim schema:author ?author ;
                schema:text ?text ; 
                schema:mentions ?entity .
        ?entity itsrdf:taIdentRef dbr:Coronavirus.
        ?claimReview schema:itemReviewed ?claim ;
                    schema:url ?reviewurl.        
        ?rating schema:author ?au ;
                schema:alternateName ?ratingName ;
                schema:ratingValue ?ratingValue FILTER(?ratingValue =-1)} 
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    claims_data = []
    for result in results["results"]["bindings"]:
        claims_data.append({
            'text': result["text"]["value"],
            'date': result["date"]["value"],
            'reviewurl': result["reviewurl"]["value"],
            'ratingName': result["ratingName"]["value"]
        })

    return claims_data
