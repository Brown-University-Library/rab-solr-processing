# Researchers@Brown Solr Scripting
A suite of scripts for customizing Solr indexing of [VIVO/Vitro](https://github.com/vivo-project) data

## /solr-schema
Customizations to the standard Solr configuration files: `schema.xml`,`solrconfig.xml`, and `solrconfig-searcher.xml`.

File path: /__VitroBaseDir__/solr/homeDirectoryTemplate/conf/

+ `schema.xml` includes the custom fields that Vitro writes to a Solr document during indexing.
+ `solrconfig.xml` adds `updateRequestProcessorChain`, which calls a sequence of Javascript scripts for reformatting the data stored in Solr document fields prior to indexing
+ `solrconfig-searcher.xml` points to a replicated Solr instance, the location of which is installation-dependent

## /solr-scripts
A series of Javascript processes for reformatting data passed from VIVO/Vitro to Solr. Solr has a built-in feature for executing scripts during the indexing process: [ScriptUpdateProcessor](https://cwiki.apache.org/confluence/display/solr/ScriptUpdateProcessor)
These are called in sequence in the `updateRequestProcessorChain` defined in `solrconfig.xml`:

File path: /__VitroBaseDir__/solr/homeDirectoryTemplate/conf/

+ `derive_fields.js`
+ `prep_data.js`
+ `make_json_fields.js`
+ `map_fields.js`
+ `delet_fields.js`

## /sparql-queries
VIVO/Vitro runs SPARQL queries against its triplestore to generate data for populating Solr documents. The queries are found in `searchIndexerConfigurationVitro.n3`. Every time a particular resource is updated, VIVO/Vitro runs these SPARQL queries with the resource URI as the query subject. By convention, the URI is defined as `?uri` in the SPARQL queries; the variable name is stripped and substituted with the correct URI at runtime. The destination Solr document field for the query results is defined by the `hasTargetField` property.

File path: /__VitroBaseDir__/rdf/display/everytime/

+ `searchIndexerConfigurationVitro.n3` contains SPARQL queries for populating Solr documents
+ `searchProhibited.n3` defines RDF classes which should be excluded from Solr indexing. Any resource which is a member of one of these classes will not be used as a subject when running the queries in `searchIndexerConfigurationVitro.n3`