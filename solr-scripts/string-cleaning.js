

function validateDataField(data) {
	var stringified, back_to_object;

	stringified = JSON.stringify(data);
	back_to_object = JSON.parse(stringified);

	return back_to_object;	
};

function parseFieldedData(str) {
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

function processAdd(cmd) {
  var doc, id, simple_data, fielded_data;
	
  simple_data = ['URI','URI','THUMBNAIL_URL','affiliations_text','awards',
		'department_t','email_s','funded_research','name_t',
		'overview_t','research_overview','research_statement',
		'scholarly_work','teaching_overview','title_t','published_in',
		'published_in','research_areas', 'research_areas','teacher_for',
		'teacher_for','cv_json','affiliations_json','collaborators_json',
		'contributor_to_json','education_json','appointments_json',
		'credentials_json','training_json','on_the_web_json', 'on_the_web'];

  fielded_data = [ 'cv_json', 'affiliations_json','collaborators_json',
		'contributor_to_json','education_json','appointments_json',
		'credentials_json','training_json','on_the_web_json' ];

  doc = cmd.solrDoc;

  json_txt = '';
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
