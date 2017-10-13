
function confirmSingleValueForField(data) {
	if ( data.length > 1 ) {
		return [ data[0] ];
	} else {
		return data;
	}
}

function confirmFieldIsArrayType(data) {
	var sample;

	if (typeof data !== 'object') {
		return [];
	} else {
		try {
			sample = data[0];
		} catch(e) {
			return [];
		}
		return data;
	}
}

function validateFieldData(data) {
	var stringified, back_to_object;

	try {
		stringified = JSON.stringify(data);
	} catch(e) {
		return '' ;
	}
	back_to_object = JSON.parse(stringified);

	return back_to_object;	
}

function convertDelimitedStrToObj(str) {
	var key_value_pairs, obj;

	obj = {};

	key_value_pairs = str.split('|%|');
	for ( i=0; i < key_value_pairs.length; i++ ) {
		var pair = key_value_pairs[i].split('|&|');
		if (pair[0] === "") {
			continue;
		} else {
			obj[pair[0]] = pair[1];
		}
	}

	return obj;
}

function cleanObject(obj) {
	var cleaned = {};

	for (var prop in obj) {
		if (obj.hasOwnProperty(prop)) {
			if (prop === "") {
				continue;
			} else if (obj[prop] === "--") {
				continue;
			} else {
				cleaned[prop] = obj[prop];
			}
		}
	}

	return cleaned;
}

function stripRepeatedDataObjs(objList) {
	var unique_list, uri_set;

	uri_set = {};
	unique_list = [];

	for (var i=0; i < objList.length; i++) {
		var obj = objList[i];
		uri_set[obj['uri']] = obj;
	}

	for (var uri in uri_set) {
		var unique;
		if (uri_set.hasOwnProperty(uri)) {
			unique = uri_set[uri];
			unique_list.push(unique);
		}
	}

	return unique_list;
}


function processAdd(cmd) {
  var doc, id, 
  	recognized_types, rtype,
  	applicable, relevant_fields,
  	single_valued_data, delimited_data,
  	i_relv;

  logger.info("Prepping document data");

  recognized_types = ['PEOPLE','ORGANIZATION'];
  doc = cmd.solrDoc;
  rtype = doc.getFieldValues('record_type');

  if ( rtype === null || recognized_types.indexOf(rtype[0]) === -1 ) {
  	logger.info('Doc is not a recognized type. Returning');
  	return true;
  } else {
  	logger.info('Prepping document of type ' + rtype[0]);
  }


  applicable = {
  	'PEOPLE' : ['affiliations_text','awards',
		'department_t','email_s','funded_research','name_t',
		'overview_t','research_overview','research_statement',
		'scholarly_work','teaching_overview','title_t',
		'research_areas','published_in',
  		'teacher_for','alumni_of', 'affiliations',
  		'delimited_cv', 'delimited_affiliations','delimited_collaborators',
		'delimited_contributor_to','delimited_education',
		'delimited_appointments','delimited_credentials',
		'delimited_training','delimited_on_the_web'],
	'ORGANIZATION' : [
		'organization_delimited_on_the_web',
		'organization_delimited_positions',
		'organization_overview'
	]
  };

  single_valued_data = ['affiliations_text','awards',
		'department_t','email_s','funded_research','name_t',
		'overview_t','research_overview','research_statement',
		'scholarly_work','teaching_overview','title_t',
		'organization_overview'];

  // multivalued_data = ['research_areas','published_in',
  // 		'teacher_for','alumni_of', 'affiliations'];

  delimited_data = [ 'delimited_cv', 'delimited_affiliations','delimited_collaborators',
		'delimited_contributor_to','delimited_education','delimited_appointments',
		'delimited_credentials','delimited_training','delimited_on_the_web',
		'organization_delimited_positions', 'organization_delimited_on_the_web'];
  
  relevant_fields = applicable[rtype[0]];

  id = doc.getFieldValue('id');
  logger.info("Prepping: " + id);

  for (i_relv=0; i_relv < relevant_fields.length; i_relv++) {
  	var field, data,
  		is_array, cardinality_checked,
  		valid_data, prepped_data,
  		i_vld, i_dlm, i_unq, i_prp;

  	field = relevant_fields[i_relv];
  	data = doc.getFieldValues(field);

  	if ( data === null ) {
  		logger.info(id + " : " + field + " is empty");
    	continue ;
  	}

  	is_array = confirmFieldIsArrayType(data);
  	if ( is_array === [] ) {
  		logger.warn(id + " : " + field + " is not stored as an array. Continuing." )
  		continue ;
  	}

  	if ( single_valued_data.indexOf(field) !== -1 ) {
  		cardinality_checked = confirmSingleValueForField(is_array);
  		if ( cardinality_checked.length !== is_array.length ) {
  			logger.warn(id + " : " + field + ' has too many values. Returning the first');
  		}
  	} else {
  		cardinality_checked = is_array;
  	}

  	valid_data = [];
	for (i_vld=0; i_vld < cardinality_checked.length; i_vld++) {
		var validated;

		validated = validateFieldData(cardinality_checked[i_vld]);
		if (validated === '') {
			logger.warn(id + " : " + field + ' failed to validate all values');
			continue ;
		} else {
			valid_data.push(validated);
		}
	}

	if ( delimited_data.indexOf(field) !== -1 ) {
		var obj_array, unique_objs;

		obj_array = [];
	  	for (i_dlm=0; i_dlm < valid_data.length; i_dlm++) {
	  		var delimited_str, converted, data_obj;

	  		delimited_str = valid_data[i_dlm];
	  		converted = convertDelimitedStrToObj(delimited_str);
	  		data_obj = cleanObject(converted);
	  		obj_array.push(data_obj);
	  	}

	  	unique_objs = stripRepeatedDataObjs(obj_array);

	  	prepped_data = [];
	  	for (i_unq=0; i_unq < unique_objs.length; i_unq++) {
	  		prepped_data.push(JSON.stringify(unique_objs[i_unq]));
	  	}
	} else {
		prepped_data = valid_data;
	}
  	
  	logger.info(id + " : setting " + field);
  	doc.setField(field, null);
  	for (i_prp=0; i_prp < prepped_data.length; i_prp++) {
  		doc.addField(field, prepped_data[i_prp]);
  	}
  }

  logger.info("Successfully prepped " + id);
  return true;
}

function processDelete(cmd) {
}

function processMergeIndexes(cmd) {
}

function processCommit(cmd) {
}

function processRollback(cmd) {
}

function finish() {
}
