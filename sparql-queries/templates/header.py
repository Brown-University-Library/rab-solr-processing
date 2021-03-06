header = """
@prefix : <http://vitro.mannlib.cornell.edu/ns/vitro/ApplicationSetup#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

#
# configure the SearchIndexer
#

# Individuals with these types will be excluded from the search index
:searchExcluder_typeExcluder
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.exclusions.ExcludeBasedOnType> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.exclusions.SearchIndexExcluder> ;
    :excludes
        "http://www.w3.org/2002/07/owl#AnnotationProperty" ,
        "http://www.w3.org/2002/07/owl#DatatypeProperty" ,
        "http://www.w3.org/2002/07/owl#ObjectProperty" .

# Individuals with types from these namespaces will be excluded from the search index.
:searchExcluder_namespaceExcluder
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.exclusions.ExcludeBasedOnNamespace> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.exclusions.SearchIndexExcluder> ;
    :excludes
        "http://vitro.mannlib.cornell.edu/ns/vitro/0.7#" ,
        "http://vitro.mannlib.cornell.edu/ns/vitro/public#" ,
        "http://vitro.mannlib.cornell.edu/ns/bnode#" ,
        "http://www.w3.org/2002/07/owl#" .

# Individuals with URIs in these namespaces will be excluded from the search index.
:searchExcluder_typeNamespaceExcluder
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.exclusions.ExcludeBasedOnTypeNamespace> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.exclusions.SearchIndexExcluder> ;
    :excludes
        "http://vitro.mannlib.cornell.edu/ns/vitro/role#public" .

:searchExcluder_syncingTypeExcluder
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.exclusions.SyncingExcludeBasedOnType> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.exclusions.SearchIndexExcluder> .

# ------------------------------------

:uriFinder_forDataProperties
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.indexing.IndexingUriFinder> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.indexing.AdditionalURIsForDataProperties> .

:uriFinder_forObjectProperties
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.indexing.IndexingUriFinder> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.indexing.AdditionalURIsForObjectProperties> .

:uriFinder_forTypeStatements
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.indexing.IndexingUriFinder> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.indexing.AdditionalURIsForTypeStatements> .

:uriFinder_forClassGroupChange
    a   <java:edu.cornell.mannlib.vitro.webapp.searchindex.indexing.IndexingUriFinder> ,
        <java:edu.cornell.mannlib.vitro.webapp.searchindex.indexing.URIsForClassGroupChange> .

# ------------------------------------
"""