def make_variable(p, used_vars):
    prop_name = p.split(':')[1]
    idx = 0
    var = '?'+prop_name[idx]
    while var in used_vars:
        idx += 1
        if idx == len(prop_name):
            var = '?' + p.replace(':','_')
            break
        else:
            var += prop_name[idx]
    used_vars.add(var)
    return (var, used_vars)

def build_graph_path(p_chain, prev_var="?uri", used_vars=set()):
    prop = p_chain[0]
    var, used_vars = make_variable(prop, used_vars)
    q_text = '{0} {1} {2}.'.format(prev_var, prop, var)
    if len(p_chain) == 1:
        return q_text
    else:
        return q_text + build_graph_chain(p_chain[1:], var, used_vars)

## CURRENTLY SKIPPING RESEARCH AREAS}
## Hand editing: research_areas
config = {  'simple': [
    {   'solr_field': 'full_name',
        'rab_attr'  : ['http://www.w3.org/2000/01/rdf-schema#label']},
    {   'solr_field': 'title',
        'rab_attr'  : ['http://vivoweb.org/ontology/core#preferredTitle']},
    {   'solr_field': 'department',
        'rab_attr'  : ['http://vivo.brown.edu/ontology/vivo-brown/primaryOrgLabel']},
    {   'solr_field': 'overview',
        'rab_attr'  : ['http://vivoweb.org/ontology/core#overview']},
    {   'solr_field': 'email',
        'rab_attr'  : ['http://vivoweb.org/ontology/core#primaryEmail']},
    {   'solr_field': 'short_id',
        'rab_attr'  : ['http://vivo.brown.edu/ontology/vivo-brown/shortId']},
    {   'solr_field': 'affiliations',
        'rab_attr'  : ['http://vivo.brown.edu/ontology/vivo-brown/affiliations']},
    {   'solr_field': 'awards',
        'rab_attr'  : ['http://vivo.brown.edu/ontology/vivo-brown/awardsAndHonors']},
    {   'solr_field': 'funded_research',
        'rab_attr'  : ['http://vivo.brown.edu/ontology/vivo-brown/fundedResearch']},
    {   'solr_field': 'research_statement',
        'rab_attr'  : ['http://vivo.brown.edu/ontology/vivo-brown/researchStatement']},
    {   'solr_field': 'research_overview',
        'rab_attr'  : ['http://vivoweb.org/ontology/core#researchOverview']},
    {   'solr_field': 'teaching_overview',
        'rab_attr'  : ['http://vivoweb.org/ontology/core#teachingOverview']},
    {   'solr_field': 'scholarly_work',
        'rab_attr'  : ['http://vivo.brown.edu/ontology/vivo-brown/scholarlyWork']},
    {   'solr_field': 'affiliations',
        'rab_attr'  : ['http://vivo.brown.edu/ontology/vivo-brown/hasAffiliation',
                        'http://www.w3.org/2000/01/rdf-schema#label']},
    {   'solr_field': 'teacher_for',
        'rab_attr'  : ['http://vivo.brown.edu/ontology/vivo-brown/teacherFor',
                        'http://www.w3.org/2000/01/rdf-schema#label']},
    {   'solr_field': 'published_in',
        'rab_attr'  : ['http://vivo.brown.edu/ontology/citation#contributorTo',
                        'http://vivo.brown.edu/ontology/citation#hasVenue',
                        'http://www.w3.org/2000/01/rdf-schema#label']},
    {   'solr_field': 'alumni_of',
        'rab_attr'  : ['http://vivoweb.org/ontology/core#educationalTraining',
                        'http://vivoweb.org/ontology/core#trainingAtOrganization',
                        'http://www.w3.org/2000/01/rdf-schema#label']},
    {   'solr_field': 'research_areas',
        'rab_attr'  : ['http://vivoweb.org/ontology/core#hasResearchArea',
                        'http://www.w3.org/2000/01/rdf-schema#label']}
    ],
            'nested' : [
    {   'solr_field': 'cv',
        'sbj_attr'  : ['http://vivo.brown.edu/ontology/vivo-brown/cv'],
        'req_attr'  : ['']},
    ]
}

class SparqlQuery(object):

    def __init__(self):
        self.solr_field = ""
        self.type_restriction = ""
        self.template = ""
        self.namespaces = []
        self.required = []
        self.optional = []
        self.complex = []
        self.simple = []
        self.body = ""
        self.vars = set()

    def write(self):
        for p in required:
            if p in self.optional:
                q_str = "OPTIONAL{{{0}}}"
            else:
                q_str = "{0}"
            if p in self.complex:
                prop_str = "?uri{1}{2}.".format(p, prop_name)
            else:
                prop_str = "?uri{1}{2}.".format(p, prop_name)
            self.body += q_str.format(prop_str)