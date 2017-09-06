queries = '''
# Multivalued attributes

:documentModifier_affiliations
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.SelectQueryDocumentModifier> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.DocumentModifier> ;
    rdfs:label "All labels are added to name fields." ;
    :hasTargetField "affiliations" ;
    :hasTypeRestriction "http://xmlns.com/foaf/0.1/Person";
    :hasSelectQuery """
        PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#> 
        PREFIX blocal:<http://vivo.brown.edu/ontology/vivo-brown/>
        SELECT DISTINCT ?clnd
        WHERE {
            ?uri blocal:hasAffiliation ?aff .
            ?aff rdfs:label ?label .
            BIND(str(?label) as ?clnd) .
        }
        """ .

:documentModifier_teacherFor
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.SelectQueryDocumentModifier> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.DocumentModifier> ;
    rdfs:label "All labels are added to name fields." ;
    :hasTargetField "teacher_for" ;
    :hasTypeRestriction "http://xmlns.com/foaf/0.1/Person";
    :hasSelectQuery """
        PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#> 
        PREFIX blocal:<http://vivo.brown.edu/ontology/vivo-brown/>
        SELECT DISTINCT ?label
        WHERE {
            ?uri blocal:teacherFor ?crs .
            ?crs rdfs:label ?label .
        }
        """ .

:documentModifier_researchAreas
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.SelectQueryDocumentModifier> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.DocumentModifier> ;
    rdfs:label "All labels are added to name fields." ;
    :hasTargetField "research_areas" ;
    :hasTypeRestriction "http://xmlns.com/foaf/0.1/Person";
    :hasSelectQuery """
        PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#> 
        PREFIX blocal:<http://vivo.brown.edu/ontology/vivo-brown/>
        PREFIX vivo:<http://vivoweb.org/ontology/core#>
        SELECT DISTINCT ?label
        WHERE {
            {
              ?uri vivo:hasResearchArea ?ra .
              ?ra rdfs:label ?label .
	    } UNION {
              ?uri blocal:hasGeographicResearchArea ?gra .
              ?gra rdfs:label ?label .
            }
        }
        """ .

:documentModifier_publishedIn
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.SelectQueryDocumentModifier> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.DocumentModifier> ;
    rdfs:label "All labels are added to name fields." ;
    :hasTargetField "published_in" ;
    :hasTypeRestriction "http://xmlns.com/foaf/0.1/Person";
    :hasSelectQuery """
        PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#> 
        PREFIX bcite:<http://vivo.brown.edu/ontology/citation#>
        SELECT DISTINCT ?label
        WHERE {
            ?uri bcite:contributorTo ?cite .
            ?cite bcite:hasVenue ?venue .
            ?venue rdfs:label ?label .
        }
        """ .

:documentModifier_alumniOf
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.SelectQueryDocumentModifier> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.DocumentModifier> ;
    rdfs:label "All labels are added to name fields." ;
    :hasTargetField "alumni_of" ;
    :hasTypeRestriction "http://xmlns.com/foaf/0.1/Person";
    :hasSelectQuery """
        PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#> 
        PREFIX vivo:<http://vivoweb.org/ontology/core#>
        SELECT DISTINCT ?label
        WHERE {
            ?uri vivo:educationalTraining ?edu .
            ?edu vivo:trainingAtOrganization ?org .
            ?org rdfs:label ?label .
        }
        """ .
'''