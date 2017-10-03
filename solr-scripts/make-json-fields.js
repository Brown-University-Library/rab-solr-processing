// https://wiki.apache.org/solr/ScriptUpdateProcessor
// https://lucene.apache.org/solr/4_7_0/solr-core/org/apache/solr/update/processor/StatelessScriptUpdateProcessorFactory.html
// https://lucene.apache.org/solr/4_2_1/solr-solrj/org/apache/solr/common/SolrInputDocument.html


function retrieveData(doc, field) {
  var raw_str, data;

  raw_str = doc.getFieldValue(field);
  data = JSON.parse(raw_str);

  return data;

}

function buildJSONObj(rabData, field_config) {

  var out, conf, data, data_obj;

  data_obj = {};

  for (var i=0; i < field_config.length; i++) {
    conf = field_config[i];
    data = rabData[conf[0]];
    data_obj[conf[1]] = data;
  }

  return data_obj;
}

function processAdd(cmd) {

  var doc, id, field_config, json_obj, json_txt,
      rab_data, local_data;

  doc = cmd.solrDoc;

  field_config = [
    // ['URI', 'id'],
    // ['URI', 'uri'],
    // ['THUMBNAIL_URL', 'thumbnail'],
    ['affiliations_text', 'affiliations_text'],
    ['awards', 'awards'],
    ['department_t', 'org_label'],
    ['email_s', 'email'],
    ['funded_research', 'funded_research'],
    ['name_t', 'name'],
    ['overview_t', 'overview'],
    ['research_overview', 'research_overview'],
    ['research_statement', 'research_statement'],
    ['scholarly_work', 'scholarly_work'],
    ['teaching_overview', 'teaching_overview'],
    ['title_t', 'title'],
    // ['published_in', 'published_in'],
    // ['research_areas', 'research_areas'],
    // ['teacher_for', 'teacher_for'],
    ['delimited_cv', 'cv'],
    ['delimited_affiliations', 'affiliations'],
    ['delimited_collaborators', 'collaborators'],
    ['delimited_contributor_to', 'contributor_to'],
    ['delimited_education', 'education'],
    ['delimited_appointments', 'appointments'],
    ['delimited_credentials', 'credentials'],
    ['delimited_training', 'training'],
    ['delimited_on_the_web', 'on_the_web']
  ];

  rab_data = doc.getFieldValue('rab_data');
  json_obj = buildJSONObj(JSON.parse(rab_data), field_config);

  json_obj['uri'] = doc.getFieldValue('URI');
  json_obj['id'] = doc.getFieldValue('URI');
  json_obj['thumbnail'] = doc.getFieldValue('THUMBNAIL_URL');
  json_obj['research_areas'] = [];
  json_obj['published_in'] = [];
  json_obj['teacher_for'] = [];

  local_data = doc.getFieldValues('research_areas');
  if ( local_data !== null) {
    for (var i=0; i < local_data.length; i++ ) {
      var d = local_data[i];
      json_obj['research_areas'].push(d);

    }
  }

  local_data = doc.getFieldValues('published_in');
  if ( local_data !== null) {
    for (var i=0; i < local_data.length; i++ ) {
      var d = local_data[i];
      json_obj['published_in'].push(d);
    }
  }

  local_data = doc.getFieldValues('teacher_for');
  if ( local_data !== null) {
    for (var i=0; i < local_data.length; i++ ) {
      var d = local_data[i];
      json_obj['teacher_for'].push(d);

    }
  }

  json_txt = JSON.stringify(json_obj);

  doc.addField( 'json_txt', json_txt );
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
