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

QUnit.test( "parseFieldedData splits a fielded string and returns \
				an object", function( assert ) {

		var fielded_str, obj;

		fielded_str = samples.eshih1.contributor_to[0];

		obj = parseFieldedData(fielded_str);
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

// QUnit.test( "", function( assert ) {
// 		assert.equal();
// });