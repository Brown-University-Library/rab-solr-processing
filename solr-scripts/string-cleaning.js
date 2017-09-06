// to handle:
// * line feed \n => \\n
// * tab \t => \\t
// * carriage return \r => \\r
// * quotes " => \\\"
// * Unicode characters 
// ** "{\"uri\":\"http://vivo.brown.edu/individual/n45889\",\"title\":\"\"O colégio eleitoral norte-americano: um anacronismo problemático\"\",\"type\":\"http://vivo.brown.edu/ontology/citation#Article\",\"issue\":\"10/28/2004\",\"date\":\"2004-01-01\",\"authors\":\"Valente, Luiz Fernando\",\"published_in\":\"Folha de São Paulo, Caderno Mundo\",}" 
// ** "{\"uri\":\"http://vivo.brown.edu/individual/n31270\",\"title\":\"The Self-cultivation of Technocrats: Tang Ying’s (1682–1756) Cultural Production and Skill Acquisition 一位技術官僚的自我修養—督陶官唐英的文化創作和技藝習得\",\"type\":\"http://vivo.brown.edu/ontology/citation#Article\",\"issue\":\"364\",\"date\":\"2013-01-01\",\"pages\":\"92-102\",\"published_in\":\"The National Palace Museum Monthly \",}"
// Examples
//
// "<p>Corresponding author publications:</p>\n\n<p>Gamradt P, Xu Y, Gratz N, Duncan K, Kobzik L, Högler S, Kovarik P, Decker T, <u>Jamieson AM</u>. <a href=\"https://vivo.brown.edu/display/n99628\">The Influence of Programmed Cell Death in Myeloid Cells on Host Resilience to Infection with Legionella pneumophila or Streptococcus pyogenes.</a> PLoS pathogens. 2016; 12 (12) : e1006032 </p>\n\n<p><u>Jamieson. A.M.,</u> Pasman, L., Yu, S., Gamradt, P., Homer, R.J., Decker, T., Medzhitov, R.M. Role of Tissue Protection in Lethal Respiratory Viral-Bacterial Coinfection. Science. Epub 2013 Apr 25 PMCID:PMC3933032.</p>\n\n<p>Jamieson AM. <a href=\"http://www.ncbi.nlm.nih.gov/pubmed/26090701\">Influence of the microbiome on response to vaccination.</a> Hum Vaccin Immunother. 2015 Jun 19:0. [Epub ahead of print] PubMed PMID: 26090701.</p>\n\n<p>Jamieson AM. Host Resilience to Emerging Coronaviruses <em>Future Virology</em>. 2016.</p>\n\n<p> </p>\n" 
// "<ul>\n\t<li>Rizza, G, and Blume J. Area Preserving Plane Deformations Generated from a Given Rotation Field along a Prescribed Curve. In preparation.</li>\n\t<li>Rizza, G, and Blume J. Twinned Finite Plane Deformations Generated by Prescribed Rotation Fields. To appear in Journal of Elasticity, DOI 10.1007/s10659-013-9455-0, 2013.</li>\n\t<li>Rizza, G, and Blume J. Plane Deformations Generated by a Prescribed Finite Rotation Field<em>. </em>Journal of Elasticity February 2013, Volume 110, Issue 2, pp 141-158</li>\n\t<li>Blume, J. An Undergraduate Teacher Education Program For Engineering Students. Proceedings<em>,</em> PTEC Annual Conference series, American Physical Society, Boulder CO: March, 2007.</li>\n\t<li>Pedersen, L, Blume, J, and Bordac, S. Using Patents Databases to Teach Information Finding Skills to Engineering Undergraduates<em>.</em> Proceedings ASEE Annual meeting in June of 2007.</li>\n\t<li>Crisco, J, Blume, J, Teeple, E, Fleming, B, and Jay, G. Assuming Exponential Decay by incorporating viscous damping improves the prediction of the coefficient of friction in pendulum tests of whole articular joints. Journal of Engineering in Medicine, Volume 221, Number 3 / 2007.<br>\n\t </li>\n</ul>\n"


// TO DO
// determine nature of field: str to be parsed as JSON, or simple string?
// JSON:
// * remove trailing comma
// * parse attribute name, value
// **? test, log attribute names, based on Solr field name
// All values:
// * based on expected value (date, str, etc), test formatting
// * escape special chars
// * handle unicode
// Error handling and logging
// * remove any field value which throws an error
// * log removal: parent uri, field, ?data uri
function cleanSpecialChars(str) {
	return 	str.replace(/\n/g, "\\n")
               .replace(/\\'/g, "\\'")
               .replace(/\\"/g, '\\"')
               .replace(/\r/g, "\\r")
               .replace(/\t/g, "\\t");
}

function removeTrailingComma(unparsedJsonStr) {
	if ( unparsedJsonStr.endsWith('\",}') ) {
		return unparsedJsonStr.substr(0, unparsedJsonStr.length - 2) + '}';
	} else if ( unparsedJsonStr.endsWith('\"}') ) {
		return unparsedJsonStr;
	} else {
		return '';
	}
}

function validateJSON(data) {
    try {
        JSON.parse(data);
        return true;
    } catch (e) {
        return false;
    }	
}

function processAdd(cmd) {
  var doc, id, front_end_fields;
	
	front_end_fields = ['URI','URI','THUMBNAIL_URL','affiliations_text','awards',
		'department_t','email_s','funded_research','name_t',
		'overview_t','research_overview','research_statement',
		'scholarly_work','teaching_overview','title_t','published_in',
		'published_in','research_areas', 'research_areas','teacher_for',
		'teacher_for','cv_json','affiliations_json','collaborators_json',
		'contributor_to_json','education_json','appointments_json',
		'credentials_json','training_json','on_the_web_json', 'on_the_web'];

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
