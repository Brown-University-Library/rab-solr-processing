queries = '''
# Single-valued attributes, stored as multivals in Solr
:documentModifier_nameT
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.SelectQueryDocumentModifier> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.DocumentModifier> ;
    rdfs:label "All labels are added to name fields." ;
    :hasTargetField "name_t" ;
    :hasTypeRestriction "http://xmlns.com/foaf/0.1/Person";
    :hasSelectQuery """
        PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#> 
        SELECT DISTINCT ?fullname
        WHERE {
            ?uri rdfs:label ?fullname .
        }
        """ .

:documentModifier_titleT
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.SelectQueryDocumentModifier> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.DocumentModifier> ;
    rdfs:label "All labels are added to name fields." ;
    :hasTargetField "title_t" ;
    :hasTypeRestriction "http://xmlns.com/foaf/0.1/Person";
    :hasSelectQuery """
        PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#> 
        PREFIX vivo:<http://vivoweb.org/ontology/core#>
        SELECT DISTINCT ?title
        WHERE {
            ?uri vivo:preferredTitle ?title .
        }
        """ .

:documentModifier_departmentT
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.SelectQueryDocumentModifier> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.DocumentModifier> ;
    rdfs:label "All labels are added to name fields." ;
    :hasTargetField "department_t" ;
    :hasTypeRestriction "http://xmlns.com/foaf/0.1/Person";
    :hasSelectQuery """
        PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#> 
        PREFIX blocal:<http://vivo.brown.edu/ontology/vivo-brown/>
        SELECT DISTINCT ?primary
        WHERE {
            ?uri blocal:primaryOrgLabel ?primary .
        }
        """ .

:documentModifier_overiewT
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.SelectQueryDocumentModifier> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.DocumentModifier> ;
    rdfs:label "All labels are added to name fields." ;
    :hasTargetField "overview_t" ;
    :hasTypeRestriction "http://xmlns.com/foaf/0.1/Person";
    :hasSelectQuery """
        PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#> 
        PREFIX vivo:<http://vivoweb.org/ontology/core#>
        SELECT DISTINCT ?overview
        WHERE {
            ?uri vivo:overview ?overview .
        }
        """ .

# Single-valued attributes

:documentModifier_emailS
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.SelectQueryDocumentModifier> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.DocumentModifier> ;
    rdfs:label "All labels are added to name fields." ;
    :hasTargetField "email_s" ;
    :hasTypeRestriction "http://xmlns.com/foaf/0.1/Person";
    :hasSelectQuery """
        PREFIX vivo:<http://vivoweb.org/ontology/core#>
        SELECT DISTINCT ?email
        WHERE {
            ?uri vivo:primaryEmail ?email .
        }
        """ .

:documentModifier_shortIdS
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.SelectQueryDocumentModifier> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.DocumentModifier> ;
    rdfs:label "All labels are added to name fields." ;
    :hasTargetField "short_id_s" ;
    :hasTypeRestriction "http://xmlns.com/foaf/0.1/Person";
    :hasSelectQuery """
        PREFIX blocal:<http://vivo.brown.edu/ontology/vivo-brown/>
        SELECT DISTINCT ?short
        WHERE {
            ?uri blocal:shortId ?short .
        }
        """ .

:documentModifier_affiliationsText
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.SelectQueryDocumentModifier> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.DocumentModifier> ;
    rdfs:label "All labels are added to name fields." ;
    :hasTargetField "affiliations_text" ;
    :hasTypeRestriction "http://xmlns.com/foaf/0.1/Person";
    :hasSelectQuery """
        PREFIX blocal:<http://vivo.brown.edu/ontology/vivo-brown/>
        SELECT DISTINCT ?aff
        WHERE {
            ?uri blocal:affiliations ?aff .
        }
        """ .

:documentModifier_awardsAndHonors
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.SelectQueryDocumentModifier> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.DocumentModifier> ;
    rdfs:label "All labels are added to name fields." ;
    :hasTargetField "awards" ;
    :hasTypeRestriction "http://xmlns.com/foaf/0.1/Person";
    :hasSelectQuery """
        PREFIX blocal:<http://vivo.brown.edu/ontology/vivo-brown/>
        SELECT DISTINCT ?aws
        WHERE {
            ?uri blocal:awardsAndHonors ?aws .
        }
        """ .

:documentModifier_fundedResearch
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.SelectQueryDocumentModifier> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.DocumentModifier> ;
    rdfs:label "All labels are added to name fields." ;
    :hasTargetField "funded_research" ;
    :hasTypeRestriction "http://xmlns.com/foaf/0.1/Person";
    :hasSelectQuery """
        PREFIX blocal:<http://vivo.brown.edu/ontology/vivo-brown/>
        SELECT DISTINCT ?fr
        WHERE {
            ?uri blocal:fundedResearch ?fr .
        }
        """ .

:documentModifier_researchStatement
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.SelectQueryDocumentModifier> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.DocumentModifier> ;
    rdfs:label "All labels are added to name fields." ;
    :hasTargetField "research_statement" ;
    :hasTypeRestriction "http://xmlns.com/foaf/0.1/Person";
    :hasSelectQuery """
        PREFIX blocal:<http://vivo.brown.edu/ontology/vivo-brown/>
        SELECT DISTINCT ?rs
        WHERE {
            ?uri blocal:researchStatement ?rs .
        }
        """ .

:documentModifier_researchOverview
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.SelectQueryDocumentModifier> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.DocumentModifier> ;
    rdfs:label "All labels are added to name fields." ;
    :hasTargetField "research_overview" ;
    :hasTypeRestriction "http://xmlns.com/foaf/0.1/Person";
    :hasSelectQuery """
        PREFIX vivo:<http://vivoweb.org/ontology/core#>
        SELECT DISTINCT ?ro
        WHERE {
            ?uri vivo:researchOverview ?ro .
        }
        """ .

:documentModifier_teachingOverview
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.SelectQueryDocumentModifier> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.DocumentModifier> ;
    rdfs:label "All labels are added to name fields." ;
    :hasTargetField "teaching_overview" ;
    :hasTypeRestriction "http://xmlns.com/foaf/0.1/Person";
    :hasSelectQuery """
        PREFIX vivo:<http://vivoweb.org/ontology/core#>
        SELECT DISTINCT ?to
        WHERE {
            ?uri vivo:teachingOverview ?to .
        }
        """ .

:documentModifier_scholarlyWork
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.SelectQueryDocumentModifier> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.DocumentModifier> ;
    rdfs:label "All labels are added to name fields." ;
    :hasTargetField "scholarly_work" ;
    :hasTypeRestriction "http://xmlns.com/foaf/0.1/Person";
    :hasSelectQuery """
        PREFIX blocal:<http://vivo.brown.edu/ontology/vivo-brown/>
        SELECT DISTINCT ?sw
        WHERE {
            ?uri blocal:scholarlyWork ?sw .
        }
        """ .
'''