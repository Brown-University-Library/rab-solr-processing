QUnit.test( "validateJSON ensures text input parses as JSON",
			function( assert ) {
		var out = validateJSON(scholarlyWorks);
		assert.ok( typeof out, 'object', 'valid JSON');
});

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