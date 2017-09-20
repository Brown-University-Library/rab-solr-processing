QUnit.test( "confirmSingleValueForField gets the contents of a Solr field\
				and confirms that it is a multivalued field, \
				with only one value", function( assert ) {

		var data, logger, confirmed, array_required, many_to_one;

		logger = mock.logger;
		data = samples.tkniesch.scholarly_work;	
		confirmed = confirmSingleValueForField(data, logger);
		assert.equal(typeof confirmed, 'string',
			'takes array with one string value and returns the string');

		data = samples.tbewes.scholarly_work;
		array_required = confirmSingleValueForField(data, logger);
		assert.equal( array_required, '', 'Bad input returns empty string');
		assert.ok(logger.log().includes('Expected a multivalued Solr field'),
			'type error logs message');

		data = samples.annenberg.label;
		many_to_one = confirmSingleValueForField(data, logger);
		assert.equal( typeof many_to_one, 'string',
			'Passing array with multiple values returns only the first');
		assert.ok(logger.log().includes('Field has too many values'),
			'length error logs message');

});

QUnit.test( "validateDataField ensures field input \
					parses and unparses as JSON",
				function( assert ) {
		var to_parse, parsed, list_data, str_data;

		list_data = ['a','b','c'];
		str_data = 'sample string';

		to_parse = samples.tbewes.scholarly_work;
		parsed = validateDataField(to_parse);
		assert.ok( !parsed.startsWith("\""), 
					'string does not start with an escaped quote');
		assert.ok( !parsed.endsWith("\""), 
					'string does not end with an escaped quote');

		assert.deepEqual( validateDataField(list_data),
			['a','b','c'], 'lists are left alone');
		assert.equal( validateDataField(str_data),
			'sample string', 'strings are left alone');
});

QUnit.test( "convertDelimitedStrToObj splits a fielded string and returns \
				an object", function( assert ) {

		var fielded_str, obj;

		fielded_str = samples.eshih1.contributor_to[0];

		obj = convertDelimitedStrToObj(fielded_str);
		assert.equal( typeof obj, "object", "output is JS object");
		assert.equal( Object.keys(obj).length, 12 ,
			"function parses correct number of fields");
		assert.equal( obj['published_in'], "--",
			"function handles empty fields correctly");
});

QUnit.test( "cleanObject checks for bad key/value pairs \
				in object and removes them", function( assert ) {
		var clean, dirty;

		dirty = { '' : 'bad key', 'bad val' : '--', 'okay' : 'fine'};

		clean = cleanObject(dirty);
		assert.notOk( '' in clean,
			'empty strings not allowed as properties');
		assert.notOk('bad val' in clean,
			'values with the -- flag are removed');
		assert.ok( 'okay' in clean,
			'acceptable keys are left alone');
		assert.equal(clean['okay'], 'fine',
			'acceptable values are left alone');
});

QUnit.test( "stripRepeatedDataObjs removes data objects \
				with the same uri", function( assert ) {

		var obj_list, stripped;

		obj_list = samples.isarkar.contributor_to;
		assert.equal(obj_list.length, 7,
			"starts with 7 citations, 4 of which have \
			the same URI");

		stripped = stripRepeatedDataObjs(obj_list);
		assert.equal(stripped.length, 4,
			"After cleaning, only 4 objects remain");
});

// QUnit.test( "gateKeeper returns a JSON string, \
// 				or calls a function and returns false", function( assert ) {

// 		var fake_id, bad_data, stub_func;

// 		bad_data =  ( {
// 		    a: String.fromCharCode(0x2028),
// 		    b: String.fromCharCode(0x2029)
// 		} );
// 		fake_id = "fake";
// 		stub_func = function(exception, id, data) { return undefined; };
// 		out = gateKeeper(bad_data, fake_id, stub_func);
// 		assert.equal(out, false, "gateKeeper returns false for bad data");
// });

// QUnit.test( "", function( assert ) {
// 		assert.equal();
// });