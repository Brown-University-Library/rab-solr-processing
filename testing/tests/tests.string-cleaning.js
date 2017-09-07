for (var i = 0; i < scholarlyWorks.length; i++) {
	(function (i) {
		QUnit.test( "validateStringData ensures text input \
					parses and unparses as JSON",
				function( assert ) {
		var data_obj = scholarlyWorks[i];
		var fac = data_obj.fac.value;
		var to_parse = data_obj.work.value;

		var out = validateStringData(to_parse);
		assert.ok( !out.startsWith("\""), 
					'string does not start with an escaped quote');
		assert.ok( !out.endsWith("\""), 
					'string does not end with an escaped quote');
		});
	})(i);
}

QUnit.test( "removeTrailingComma should remove trailing commas \
				from unparsed JSON strings", function( assert ) {
		var bad_with_comma;

		bad_with_comma = '{ \"foo\": \"bar\",}';
		cleaned = removeTrailingComma(bad_with_comma);
		assert.ok( cleaned.endsWith('\"}'),
			"string ends with escaped quotechar" );
		assert.equal( typeof JSON.parse(cleaned), "object", 
			"string parses as JSON object" );

		good_no_comma = '{ \"foo\": \"bar\"}';
		cleaned = removeTrailingComma(good_no_comma);
		assert.equal( cleaned, good_no_comma,
			"function passes strings without ending comma" );
});