// https://wiki.apache.org/solr/ScriptUpdateProcessor
// https://lucene.apache.org/solr/4_7_0/solr-core/org/apache/solr/update/processor/StatelessScriptUpdateProcessorFactory.html
// https://lucene.apache.org/solr/4_2_1/solr-solrj/org/apache/solr/common/SolrInputDocument.html


function retrieveData(doc, field) {
  var raw_str, data;

  raw_str = doc.getFieldValue(field);
  data = JSON.parse(raw_str);

  return data;

}

function buildJSONObj(doc, field_config) {

  var out, conf, data, data_obj;

  data_obj = {};

  for (var i=0; i < field_config.length; i++) {
    conf = field_config[i];
    data = retrieveData(doc, conf[0]);
    data_obj[conf[1]] = data;
  }

  return data_obj;
}

function processAdd(cmd) {

  var doc, id, field_config, json_obj, json_txt;

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
    ['published_in', 'published_in'],
    ['research_areas', 'research_areas'],
    ['teacher_for', 'teacher_for'],
    ['cv_json', 'cv'],
    ['affiliations_json', 'affiliations'],
    ['collaborators_json', 'collaborators'],
    ['contributor_to_json', 'contributor_to'],
    ['education_json', 'education'],
    ['appointments_json', 'appointments'],
    ['credentials_json', 'credentials'],
    ['training_json', 'training'],
    ['on_the_web_json', 'on_the_web']
  ];

  json_obj = buildJSONObj(doc, field_config);

  json_obj['uri'] = doc.getFieldValue('URI');
  json_obj['id'] = doc.getFieldValue('URI');
  json_obj['thumbnail'] = doc.getFieldValue('THUMBNAIL_URL');

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
