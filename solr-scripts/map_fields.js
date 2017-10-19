// https://wiki.apache.org/solr/ScriptUpdateProcessor
// https://lucene.apache.org/solr/4_7_0/solr-core/org/apache/solr/update/processor/StatelessScriptUpdateProcessorFactory.html
// https://lucene.apache.org/solr/4_2_1/solr-solrj/org/apache/solr/common/SolrInputDocument.html


function processAdd(cmd) {

  var doc, id,
      recognized_types, rtype,
      applicable, relevant_fields,
      field_mappings, mappings,
      single_valued_fields,
      i_relv;

  logger.info("Building JSON data");

  recognized_types = ['PEOPLE'];
  doc = cmd.solrDoc;
  rtype = doc.getFieldValues('record_type');

  if ( rtype === null || recognized_types.indexOf(rtype[0]) === -1 ) {
    logger.info('Doc is not a recognized type. Returning');
    return true;
  } else {
    logger.info('Mapping Solr fields for document of type ' + rtype[0]);
  }

  applicable = {
    'PEOPLE' : [
      'person_shortid','person_affiliations',
      'person_primary_department','person_email','person_label',
      'person_overview','person_title','person_published_in',
      'person_research_areas','person_alumni_of'
    ]
  };

  field_mappings = {
    'PEOPLE' : {
      'person_email' : 'email_s',
      'person_title' : 'title_t',
      'person_label' : 'name_t',
      'person_primary_department' : 'department_t',
      'person_overview' : 'overview_t',
      'person_shortid' : 'short_id_s',
      'person_affiliations' : 'affiliations',
      'person_research_areas' : 'research_areas',
      'person_published_in' : 'published_in',
      'person_alumni_of' : 'alumni_of'
    }
  }

  single_valued_fields = [
    'email_s', 'short_id_s'
  ];

  relevant_fields = applicable[rtype[0]];
  mappings = field_mappings[rtype[0]];

  id = doc.getFieldValue('id');
  logger.info(id + " : mapping Solr fields");

  for (i_relv=0; i_relv < relevant_fields.length; i_relv++) {
    var field, data, mapped,
      data_count, i_map;

    field = relevant_fields[i_relv];
    mapped = mappings[field];
    data = doc.getFieldValues(field);
    logger.info(id + " : mapping " + field + " to " + mapped);

    if ( data === null ) {
      logger.info(id + " : " + field + " is empty");
      continue ;
    }

    if ( single_valued_fields.indexOf(field) !== -1 ) {
      data_count = 1;
    } else {
      data_count = data.length;
    }

    for (i_map=0; i_map < data_count; i_map++) {
      doc.addField(mapped, data[i_map]);
    }
  }

  logger.info(id + " : successfully mapped Solr fields");
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
