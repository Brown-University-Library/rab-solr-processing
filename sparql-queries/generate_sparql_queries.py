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

def build_graph_path(attr_list, used_vars=set(),
                        prev_var="?uri", text=''):
    prop = attr_list[0]
    var, used_vars = make_variable(prop, used_vars)
    q_text = '{0} {1} {2}.'.format(prev_var, prop, var)
    text += q_text
    if len(attr_list) == 1:
        return text, var
    else:
        return build_graph_path(attr_list[1:], used_vars, var, text)

## CURRENTLY SKIPPING RESEARCH AREAS
## Hand editing: research_areas
config = {  'simple': [
    {   'doc_field': 'full_name',
        'req_attr'  : ['http://www.w3.org/2000/01/rdf-schema#label']},
    {   'doc_field': 'title',
        'req_attr'  : ['http://vivoweb.org/ontology/core#preferredTitle']},
    {   'doc_field': 'department',
        'req_attr'  : ['http://vivo.brown.edu/ontology/vivo-brown/primaryOrgLabel']},
    {   'doc_field': 'overview',
        'req_attr'  : ['http://vivoweb.org/ontology/core#overview']},
    {   'doc_field': 'email',
        'req_attr'  : ['http://vivoweb.org/ontology/core#primaryEmail']},
    {   'doc_field': 'short_id',
        'req_attr'  : ['http://vivo.brown.edu/ontology/vivo-brown/shortId']},
    {   'doc_field': 'affiliations',
        'req_attr'  : ['http://vivo.brown.edu/ontology/vivo-brown/affiliations']},
    {   'doc_field': 'awards',
        'req_attr'  : ['http://vivo.brown.edu/ontology/vivo-brown/awardsAndHonors']},
    {   'doc_field': 'funded_research',
        'req_attr'  : ['http://vivo.brown.edu/ontology/vivo-brown/fundedResearch']},
    {   'doc_field': 'research_statement',
        'req_attr'  : ['http://vivo.brown.edu/ontology/vivo-brown/researchStatement']},
    {   'doc_field': 'research_overview',
        'req_attr'  : ['http://vivoweb.org/ontology/core#researchOverview']},
    {   'doc_field': 'teaching_overview',
        'req_attr'  : ['http://vivoweb.org/ontology/core#teachingOverview']},
    {   'doc_field': 'scholarly_work',
        'req_attr'  : ['http://vivo.brown.edu/ontology/vivo-brown/scholarlyWork']},
    {   'doc_field': 'affiliations',
        'attr_path'  : ['http://vivo.brown.edu/ontology/vivo-brown/hasAffiliation',
                        'http://www.w3.org/2000/01/rdf-schema#label']},
    {   'doc_field': 'teacher_for',
        'attr_path'  : ['http://vivo.brown.edu/ontology/vivo-brown/teacherFor',
                        'http://www.w3.org/2000/01/rdf-schema#label']},
    {   'doc_field': 'published_in',
        'attr_path'  : ['http://vivo.brown.edu/ontology/citation#contributorTo',
                        'http://vivo.brown.edu/ontology/citation#hasVenue',
                        'http://www.w3.org/2000/01/rdf-schema#label']},
    {   'doc_field': 'alumni_of',
        'attr_path'  : ['http://vivoweb.org/ontology/core#educationalTraining',
                        'http://vivoweb.org/ontology/core#trainingAtOrganization',
                        'http://www.w3.org/2000/01/rdf-schema#label']},
    {   'doc_field': 'research_areas',
        'attr_path'  : ['http://vivoweb.org/ontology/core#hasResearchArea',
                        'http://www.w3.org/2000/01/rdf-schema#label']}
    ],
            'nested' : [
    {   'doc_field': 'cv',
        'attr_path'  : ['http://vivo.brown.edu/ontology/vivo-brown/cv'],
        'req_attr'  : ['']},
    ]
}

class SparqlQuery(object):

    def __init__(self):
        self.doc_field = ""
        self.type_restriction = ""
        self.template = ""
        self.start_node = "?uri"
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