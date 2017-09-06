builtins = '''
:documentModifier_AllNames
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.SelectQueryDocumentModifier> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.DocumentModifier> ;
    rdfs:label "All labels are added to name fields." ;
    :hasTargetField "nameRaw" ;
    :hasSelectQuery """
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
		SELECT ?label 
		WHERE {
			?uri rdfs:label ?label .
	    }
        """ .

:documentModifier_NameFieldBooster
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.FieldBooster> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.DocumentModifier> ;
    :hasTargetField "nameRaw" ;
    :hasTargetField "nameLowercase" ;
    :hasTargetField "nameUnstemmed" ;
    :hasTargetField "nameStemmed" ;
    :hasBoost "1.2"^^xsd:float .

:documentModifier_thumbnailImageUrl
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.ThumbnailImageURL> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.documentBuilding.DocumentModifier> .
'''