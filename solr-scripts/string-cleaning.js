
function confirmSingleValueForField(data, log) {
	if (typeof data !== 'object') {
		log.error('Expected a multivalued Solr field');
		return '';
	} else if ( data.length > 1 ) {
		log.warn('Field has too many values. Returning the first');
		return data[0];
	} else {
		return data[0];
	}
}

function validateFieldData(data) {
	var stringified, back_to_object;

	stringified = JSON.stringify(data);
	back_to_object = JSON.parse(stringified);

	return back_to_object;	
};

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
};

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
};

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

function gateKeeper(data, docId, func) {
	var jdata;

	try {
		jdata = JSON.stringify(data);
	} catch (e) {
		func(e, docId, data);
		jdata = false;
	}

	return jdata;
}

function processAdd(cmd) {
  var doc, id, simple_data, fielded_data;
	
  // Omitted: 'URI','THUMBNAIL_URL'
  simple_data = ['affiliations_text','awards',
		'department_t','email_s','funded_research','name_t',
		'overview_t','research_overview','research_statement',
		'scholarly_work','teaching_overview','title_t','published_in',
		'teacher_for'];

  delimited_data = [ 'delimited_cv', 'delimited_affiliations','delimited_collaborators',
		'delimited_contributor_to','delimited_education','delimited_appointments',
		'delimited_credentials','delimited_training','delimited_on_the_web',
		'delimited_research_areas' ];

  doc = cmd.solrDoc;
  id = doc.getFieldValue('URI');

  logger.info("Adding Solr Doc for: " + id);

  for (var i=0; i < simple_data.length; i++) {
  	var field, data, valid, out;

  	field = simple_data[i];
  	logger.info(id + " : " + field);

  	data = doc.getFieldValues(field);
  	if ( data === null ) {
  		logger.info(id + " : " + field + " is empty");
    	continue ;
  	}

  	confirmed = confirmSingleValueForField(data, logger);
  	valid = validateFieldData(confirmed);
  	out = gateKeeper(confirmed, id, logger.error)

  	if (out !== false) {
  		doc.setField(field, out);
  	}
  }

  for (var i=0; i < delimited_data.length; i++) {
  	var field, data,
  		obj_list, unique_list,
  		out, json_field;

  	field = delimited_data[i];
  	data = doc.getFieldValues(field);
  	if ( data === null ) {
     continue ;
  	}

  	obj_list = [];
  	for (var d=0; d < data.length; d++) {
  		var delimited_str, data_obj;

  		delimited_str = data[d];
  		valid = validateFieldData(delimited_str);
  		converted = convertDelimitedStrToObj(valid);
  		data_obj = cleanObject(converted);
  		obj_list.push(data_obj);
  	}

  	unique_list = stripRepeatedDataObjs(obj_list);
  	out = gateKeeper(unique_list, id, logger.error)

  	if (out !== false) {
  		json_field = field.substring(10) + '_json';
  		doc.addField(json_field, out);
  		doc.removeField(field);
  	}
  }

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
