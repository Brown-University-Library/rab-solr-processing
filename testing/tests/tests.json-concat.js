QUnit.test( "retrieveData retrieves a single field name\
					and parses the string field value as JSON",
				function( assert ) {
		var doc, field_name, str_data, obj_data;

		// doc is imported aa global variable,
		// mocking behavior of Solr's Java SolrInputDocument class
		// https://lucene.apache.org/solr/4_2_1/solr-solrj/org/apache/solr/common/SolrInputDocument.html

		doc = mock.solrDoc;
		field_name = 'scholarly_work';
		str_data = retrieveData(doc, field_name);
		assert.equal( typeof str_data, "string",
					'querying Scholarly Works field returns a string');

		field_name = 'contributor_to_json';
		obj_data = retrieveData(doc, field_name);
		assert.equal( typeof obj_data, "object",
					'querying Contributor To field returns an object');
});

QUnit.test( "buildJSONObj takes a list of fields and their aliases \
					and returns an object using field values and aliases",
				function( assert ) {
		var doc, field_list, data_obj, sample_keys;

		doc = mock.solrDoc;
		field_list = [	['awards', 'awards'],
    					['department_t', 'org_label'],
    					['email_s', 'email'] ];
    	data_obj = buildJSONObj(doc, field_list);
		assert.ok(field_list[0][1] in data_obj, 'alias key in object');
		assert.notOk('scholarly_work' in data_obj,
			'unexpected keys not in object');
		assert.equal( Object.keys(data_obj).length, field_list.length,
			'object has as many keys as the list is long');

		sample_keys = field_list[1];
		data_val = retrieveData(doc, sample_keys[0]);
		assert.equal(data_obj[sample_keys[1]], data_val,
			'doc field value is mapped to object using alias');
});

// QUnit.test( "", function( assert ) {
// 		assert.equal();
// });