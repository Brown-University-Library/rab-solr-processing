queries = '''
# Build JSON attributes

:documentModifier_cvJSON
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.SelectQueryDocumentModifier> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.DocumentModifier> ;
    rdfs:label "All labels are added to name fields." ;
    :hasTargetField "cv_json" ;
    :hasTypeRestriction "http://xmlns.com/foaf/0.1/Person";
    :hasSelectQuery """
        PREFIX vivo:<http://vivoweb.org/ontology/core#>
        PREFIX blocal:<http://vivo.brown.edu/ontology/vivo-brown/>
        SELECT DISTINCT ?json
        WHERE {
            ?uri blocal:cv ?cv .
            ?cv vivo:linkURI ?link .
            ?cv vivo:linkAnchorText ?text .
            BIND(replace( '\"cv_link\":\"lnk\",', 'lnk', str(?link) ) as ?linkStr)
            BIND(replace( '\"cv_link_text\":\"txt\"', 'txt', str(?text) ) as ?textStr)
            BIND(concat( '{', ?linkStr, ?textStr, '}') as ?json)
        }
        """ .

:documentModifier_affiliationsJSON
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.SelectQueryDocumentModifier> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.DocumentModifier> ;
    rdfs:label "All labels are added to name fields." ;
    :hasTargetField "affiliations_json" ;
    :hasTypeRestriction "http://xmlns.com/foaf/0.1/Person";
    :hasSelectQuery """
        PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#> 
        PREFIX blocal:<http://vivo.brown.edu/ontology/vivo-brown/>
        SELECT DISTINCT ?json
        WHERE {
            ?uri blocal:hasAffiliation ?aff .
            ?aff rdfs:label ?label .
            BIND(replace( '\"uri\":\"aff\",', 'aff', str(?aff) ) as ?uriStr)
            BIND(replace( '\"id\":\"aff\",', 'aff', str(?aff) ) as ?idStr)
            BIND(replace( '\"name\":\"aff\"', 'aff', str(?label) ) as ?nameStr)
            BIND(concat( '{', ?uriStr, ?idStr, ?nameStr, '}') as ?json)
        }
        """ .

### Expects a title for each collaborator; OPTIONAL or UNION?
:documentModifier_collaboratorsJSON
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.SelectQueryDocumentModifier> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.DocumentModifier> ;
    rdfs:label "All labels are added to name fields." ;
    :hasTargetField "collaborators_json" ;
    :hasTypeRestriction "http://xmlns.com/foaf/0.1/Person";
    :hasSelectQuery """
        PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#> 
        PREFIX vivo:<http://vivoweb.org/ontology/core#>
        SELECT DISTINCT ?json
        WHERE {
            ?uri vivo:hasCollaborator ?clb .
            ?clb rdfs:label ?label .
            ?clb vivo:preferredTitle ?title .
            BIND(replace( '\"uri\":\"clb\",', 'clb', str(?clb) ) as ?uriStr)
            BIND(replace( '\"id\":\"clb\",', 'clb', str(?clb) ) as ?idStr)
            BIND(replace( '\"name\":\"clb\",', 'clb', str(?label) ) as ?nameStr)
            BIND(replace( '\"title\":\"val\"', 'val', str(?title) ) as ?titleStr)
            BIND(concat( '{', ?uriStr, ?idStr, ?nameStr, ?titleStr, '}' ) as ?json)
        }
        """ .

:documentModifier_contributorJSON
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.SelectQueryDocumentModifier> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.DocumentModifier> ;
    rdfs:label "All labels are added to name fields." ;
    :hasTargetField "contributor_to_json" ;
    :hasTypeRestriction "http://xmlns.com/foaf/0.1/Person";
    :hasSelectQuery """
        PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
        PREFIX bcite: <http://vivo.brown.edu/ontology/citation#>
        PREFIX vitro:    <http://vitro.mannlib.cornell.edu/ns/vitro/0.7#>
        SELECT DISTINCT ?json
        WHERE {
            ?uri bcite:contributorTo ?cite .
            ?cite rdfs:label ?title .
            ?cite vitro:mostSpecificType ?type .
            OPTIONAL { ?cite bcite:volume ?vol .}
            OPTIONAL { ?cite bcite:issue ?issue . }
            OPTIONAL { ?cite bcite:date ?date . }
            OPTIONAL { ?cite bcite:pages ?pages . }
            OPTIONAL { ?cite bcite:authorList ?authors . }
            OPTIONAL { ?cite bcite:publishedIn ?published_in . }
            OPTIONAL { ?cite bcite:doi ?doi . }
            OPTIONAL { ?cite bcite:pmid ?pub_med_id .}
            OPTIONAL {
                ?cite bcite:hasVenue ?venue .
                ?venue rdfs:label ?venue_name .
            }
            BIND ("|@|ATTR|&|VAL|%|" as ?template)
            BIND ( replace( replace( ?template,'ATTR', 'uri' ), 'VAL', str(?cite) ) as ?uri_ )
            BIND ( replace( replace( ?template,'ATTR', 'title' ), 'VAL', str(?title) ) as ?title_ )
            BIND ( replace( replace( ?template,'ATTR', 'type' ), 'VAL', str(?type) ) as ?type_ )
            BIND ( replace( replace( ?template,'ATTR', 'volume' ), 'VAL', IF ( bound(?vol), str(?vol), '--' ) ) as ?vol_ )
            BIND ( replace( replace( ?template,'ATTR', 'issue' ), 'VAL', IF ( bound(?issue), str(?issue), '--' ) ) as ?issue_ )
            BIND ( replace( replace( ?template,'ATTR', 'date' ), 'VAL', IF ( bound(?date), str(?date), '--' ) ) as ?date_ )
            BIND ( replace( replace( ?template,'ATTR', 'pages' ), 'VAL', IF ( bound(?pages), str(?pages), '--' ) ) as ?pages_ )
            BIND ( replace( replace( ?template,'ATTR', 'authors' ), 'VAL', IF ( bound(?authors), str(?authors), '--' ) ) as ?authors_ )
            BIND ( replace( replace( ?template,'ATTR', 'published_in' ), 'VAL', IF ( bound(?published_in), str(?published_in), '--' ) ) as ?published_in_ )
            BIND ( replace( replace( ?template,'ATTR', 'venue' ), 'VAL', IF ( bound(?venue_name), str(?venue_name), '--' ) ) as ?venue_name_ )
            BIND ( replace( replace( ?template,'ATTR', 'doi' ), 'VAL', IF ( bound(?doi), str(?doi), '--' ) ) as ?doi_ )
            BIND ( replace( replace( ?template,'ATTR', 'pub_med_id' ), 'VAL', IF ( bound(?pub_med_id), str(?pub_med_id), '--' ) ) as ?pub_med_id_ )
            BIND( CONCAT( ?uri_,?title_,?type_,?vol_,?issue_,?date_,?pages_,?authors_,?published_in_,?venue_name_,?doi_,?pub_med_id_ ) as ?json )
        }
        """ .

:documentModifier_educationJSON
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.SelectQueryDocumentModifier> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.DocumentModifier> ;
    rdfs:label "All labels are added to name fields." ;
    :hasTargetField "education_json" ;
    :hasTypeRestriction "http://xmlns.com/foaf/0.1/Person";
    :hasSelectQuery """
        PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#> 
        PREFIX vivo:<http://vivoweb.org/ontology/core#>
        PREFIX blocal:<http://vivo.brown.edu/ontology/vivo-brown/>
        SELECT DISTINCT ?json
        WHERE {
            ?uri vivo:educationalTraining ?edu .
            ?edu vivo:trainingAtOrganization ?org .
            ?edu blocal:degreeDate ?date .
            ?edu rdfs:label ?degree .
            ?org rdfs:label ?orgLabel .
            BIND(replace( '\"school_uri\":\"suri\",', 'suri', str(?org) ) as ?uriStr)
            BIND(replace( '\"date\":\"data\",', 'data', str(?date) ) as ?dateStr)
            BIND(replace( '\"school_name\":\"sname\",', 'sname', str(?orgLabel) ) as ?nameStr)
            BIND(replace( '\"degree\":\"data\"', 'data', str(?degree) ) as ?degreeStr)
            BIND(concat( '{', ?uriStr, ?dateStr, ?nameStr, ?degreeStr, '}' ) as ?json)
        }
        """ .

:documentModifier_weblinkJSON
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.SelectQueryDocumentModifier> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.DocumentModifier> ;
    rdfs:label "All labels are added to name fields." ;
    :hasTargetField "on_the_web_json" ;
    :hasTypeRestriction "http://xmlns.com/foaf/0.1/Person";
    :hasSelectQuery """
        PREFIX vivo:<http://vivoweb.org/ontology/core#>
        PREFIX blocal:<http://vivo.brown.edu/ontology/vivo-brown/>
        SELECT DISTINCT ?json
        WHERE {
            ?uri blocal:drrbWebPage ?link .
            ?link vivo:linkURI ?addr .
            OPTIONAL { ?link vivo:linkAnchorText ?text .}
            OPTIONAL { ?link vivo:rank ?rank . }
            BIND( replace( '\"uri\":\"data\",', 'data', str(?link)) as ?linkStr)
            BIND( replace( '\"url\":\"data\",', 'data', str(?addr)) as ?addrStr)
            BIND( (IF (bound(?text), replace( '\"text\":\"data\",', 'data', str(?text)), '')) as ?textStr )
            BIND( (IF (bound(?rank), replace( '\"rank\":\"data\"', 'data', str(?rank)), '')) as ?rankStr )
            BIND(concat( '{', ?linkStr, ?addrStr, ?textStr, ?rankStr, '}') as ?json)
        }
        """ .

:documentModifier_appointmentsJSON
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.SelectQueryDocumentModifier> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.DocumentModifier> ;
    rdfs:label "All labels are added to name fields." ;
    :hasTargetField "appointments_json" ;
    :hasTypeRestriction "http://xmlns.com/foaf/0.1/Person";
    :hasSelectQuery """
        PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
        PREFIX bprofile: <http://vivo.brown.edu/ontology/profile#>
        SELECT DISTINCT ?json
        WHERE {
            { SELECT ?apt (SAMPLE(?sname) as ?name) (SAMPLE(?sdept) as ?dept) (SAMPLE(?sstart) as ?start) (SAMPLE(?send) as ?end) (SAMPLE(?sorg_name) as ?org_name) (SAMPLE(?shospital_name) as ?hospital_name)
            WHERE {
            ?uri bprofile:hasAppointment ?apt .
            ?apt rdfs:label ?sname .
            ?apt bprofile:department ?sdept .
            ?apt bprofile:startDate ?sstart .
            ?apt bprofile:endDate ?send .
            OPTIONAL {
                ?apt bprofile:hasOrganization ?org .
                ?org rdfs:label ?sorg_name .
            }
            OPTIONAL {
                ?apt bprofile:hasHospital ?hospital .
                ?hospital rdfs:label ?shospital_name .
            }
            }
            GROUP BY ?apt
            }
            BIND (replace( '\"uri\":\"apt\",', 'apt', str(?apt)) as ?uriStr)
            BIND (replace( '\"name\":\"data\",', 'data', str(?name)) as ?nameStr)
            BIND (replace( '\"department\":\"data\",', 'data', str(?dept)) as ?deptStr)
            BIND (replace( '\"start_date\":\"data\",', 'data', str(?start)) as ?startStr)
            BIND (replace( '\"end_date\":\"data\",', 'data', str(?end)) as ?endStr)
            BIND( (IF (bound(?org_name), replace( '\"org_name\":\"data\",', 'data', str(?org_name)), '')) as ?orgStr )
            BIND( (IF (bound(?hospital_name), replace( '\"hospital_name\":\"data\"', 'data', str(?hospital_name)), '')) as ?hospStr )
            BIND(concat( '{', ?uriStr, ?nameStr, ?deptStr, ?startStr, ?endStr, ?orgStr, ?hospStr, '}') as ?json)
        }
        """ .

:documentModifier_credentialsJSON
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.SelectQueryDocumentModifier> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.DocumentModifier> ;
    rdfs:label "All labels are added to name fields." ;
    :hasTargetField "credentials_json" ;
    :hasTypeRestriction "http://xmlns.com/foaf/0.1/Person";
    :hasSelectQuery """
        PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
        PREFIX bprofile: <http://vivo.brown.edu/ontology/profile#>
        SELECT DISTINCT ?json
        WHERE {
            { SELECT ?crd (SAMPLE(?sname) as ?name) (SAMPLE(?snum) as ?number) (SAMPLE(?sstart) as ?start) (SAMPLE(?send) as ?end) (SAMPLE(?sgrantor_name) as ?grantor_name) (SAMPLE(?sspecialty_name) as ?specialty_name)
            WHERE {
            ?uri bprofile:hasCredential ?crd .
            ?crd rdfs:label ?sname .
            ?crd bprofile:startDate ?sstart .
            OPTIONAL { ?crd bprofile:credentialNumber ?snum . }
            OPTIONAL { ?crd bprofile:endDate ?send . }
            OPTIONAL {
                ?crd bprofile:credentialGrantedBy ?grantor .
                ?grantor rdfs:label ?sgrantor_name .
            }
            OPTIONAL {
                ?crd bprofile:hasSpecialty ?specialty .
                ?specialty rdfs:label ?sspecialty_name .
            }
            }
            GROUP BY ?crd
            }
            BIND (replace( '\"uri\":\"crd\",', 'crd', str(?crd)) as ?uriStr)
            BIND (replace( '\"name\":\"data\",', 'data', str(?name)) as ?nameStr)
            BIND (replace( '\"start_date\":\"data\",', 'data', str(?start)) as ?startStr)
            BIND( (IF (bound(?number), replace( '\"number\":\"data\",', 'data', str(?number)), '')) as ?numStr )
            BIND( (IF (bound(?end), replace( '\"end_date\":\"data\",', 'data', str(?end)), '')) as ?endStr )
            BIND( (IF (bound(?grantor_name), replace( '\"grantor_name\":\"data\",', 'data', str(?grantor_name)), '')) as ?grantStr )
            BIND( (IF (bound(?specialty_name), replace( '\"specialty_name\":\"data\"', 'data', str(?specialty_name)), '')) as ?specStr )
            BIND(concat( '{', ?uriStr, ?nameStr, ?startStr, ?endStr, ?numStr, ?grantStr, ?specStr, '}') as ?json)
        }
        """ .

:documentModifier_trainingJSON
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.SelectQueryDocumentModifier> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.DocumentModifier> ;
    rdfs:label "All labels are added to name fields." ;
    :hasTargetField "training_json" ;
    :hasTypeRestriction "http://xmlns.com/foaf/0.1/Person";
    :hasSelectQuery """
        PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
        PREFIX bprofile: <http://vivo.brown.edu/ontology/profile#>
        SELECT DISTINCT ?json
        WHERE {
            { SELECT ?trn (SAMPLE(?sname) as ?name) (SAMPLE(?scity) as ?city) (SAMPLE(?sstate) as ?state) (SAMPLE(?scountry) as ?country) (SAMPLE(?sstart) as ?start) (SAMPLE(?send) as ?end) (SAMPLE(?sorg_name) as ?org_name) (SAMPLE(?shospital_name) as ?hospital_name) (SAMPLE(?sspecialty_name) as ?specialty_name)
            WHERE {
            ?uri bprofile:hasTraining ?trn .
            ?trn rdfs:label ?sname .
            OPTIONAL { ?trn bprofile:city ?scity . }
            OPTIONAL { ?trn bprofile:state ?sstate . }
            OPTIONAL { ?trn bprofile:country ?scountry . }
            OPTIONAL { ?trn bprofile:startDate ?sstart . }
            OPTIONAL { ?trn bprofile:endDate ?send . }
            OPTIONAL {
                ?trn bprofile:hasOrganization ?org .
                ?org rdfs:label ?sorg_name .
            }
            OPTIONAL {
                ?trn bprofile:hasHospital ?hospital .
                ?hospital rdfs:label ?shospital_name .
            }
            OPTIONAL {
                ?trn bprofile:hasSpecialty ?specialty .
                ?specialty rdfs:label ?sspecialty_name .
            }
            }
            GROUP BY ?trn
            }
            BIND (replace( '\"uri\":\"trn\",', 'trn', str(?trn)) as ?uriStr)
            BIND (replace( '\"name\":\"data\",', 'data', str(?name)) as ?nameStr)
            BIND( (IF (bound(?start), replace( '\"start_date\":\"data\",', 'data', str(?start)), '')) as ?startStr )
            BIND( (IF (bound(?end), replace( '\"end_date\":\"data\",', 'data', str(?end)), '')) as ?endStr )
            BIND( (IF (bound(?city), replace( '\"city\":\"data\",', 'data', str(?city)), '')) as ?cityStr )
            BIND( (IF (bound(?state), replace( '\"state\":\"data\",', 'data', str(?state)), '')) as ?stateStr )
            BIND( (IF (bound(?country), replace( '\"country\":\"data\",', 'data', str(?country)), '')) as ?countryStr )
            BIND( (IF (bound(?org_name), replace( '\"org_name\":\"data\",', 'data', str(?org_name)), '')) as ?orgStr )
            BIND( (IF (bound(?hospital_name), replace( '\"hospital_name\":\"data\",', 'data', str(?hospital_name)), '')) as ?hospStr )
            BIND( (IF (bound(?specialty_name), replace( '\"specialty_name\":\"data\"', 'data', str(?specialty_name)), '')) as ?specStr )
            BIND(concat( '{', ?uriStr, ?nameStr, ?startStr, ?endStr, ?cityStr, ?stateStr, ?countryStr, ?orgStr, ?hospStr, ?specStr, '}') as ?json)
        }
        """ .
'''