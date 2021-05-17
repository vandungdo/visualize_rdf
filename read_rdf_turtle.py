import rdflib
import json

def rdf_2_json(rdfFile):
    g = rdflib.Graph()
    result = g.parse(rdfFile, format='turtle')
    subjects = []
    predicates = []
    objects = []
    links = []

    for subj, pred, obj in g:
        subjects.append(subj.n3())
        predicates.append(pred.n3())
        objects.append(obj.n3())
        d = {'source':subj.n3(),'target':obj.n3(),'type':pred.n3()}
        links.append(d)

    nodeNames = subjects + objects
    nodeNames = list(set(nodeNames))
    nodes = []

    for node in nodeNames:
        d = {'id':node, 'name':node}
        nodes.append(d)

    j = json.dumps({'nodes':nodes,'links':links})

    return j

