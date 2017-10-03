// https://wiki.apache.org/solr/ScriptUpdateProcessor
// https://lucene.apache.org/solr/4_7_0/solr-core/org/apache/solr/update/processor/StatelessScriptUpdateProcessorFactory.html
// https://lucene.apache.org/solr/4_2_1/solr-solrj/org/apache/solr/common/SolrInputDocument.html


function convertObjectListToData(objList, dataAttr, log) {
  var data_list;

  data_list = [];


  if (typeof objList !== 'object') {
    log.error('Expected list');
  }
  else if (objList.length === 0) {
    log.info('No values in list');
    return [];
  }

  for (var i=0; i < objList.length; i++) {
    var obj, data_val, e;

    obj = objList[i];
    try {
      data_val = obj[dataAttr];
    } catch(e) {
      log.error(e);
      data_val = '';
    }

    data_list.push(data_val);
  }

  return data_list;
}

// https://stackoverflow.com/questions/9229645/remove-duplicates-from-javascript-array
// https://stackoverflow.com/questions/971312/why-avoid-increment-and-decrement-operators-in-javascript
function removeDuplicatesFromList(list) {
    var seen = {};
    var out = [];
    var len = list.length;
    var j = 0;
    for(var i = 0; i < len; i++) {
         var item = list[i];
         if(seen[item] !== 1) {
               seen[item] = 1;
               out[j++] = item;
         }
    }
    return out;
}

function addDataToObject(data, attrName, obj) {
  
}


function processAdd(cmd) {

  var doc, id, field_config, json_obj, json_txt;

  doc = cmd.solrDoc;


  json_str = doc.getFieldValue('rab_data');
  rab_data = JSON.parse(json_str);

  field_config = [
    ['delimited_contributor_to', 'published_in'],
    ['delimited_education', 'alumni_of'],
    ['delimited_research_areas', 'research_areas'],
    ['delimited_teacher_for', 'teacher_for'],
    ['delimited_affiliations', 'affiliations']
  ];

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
