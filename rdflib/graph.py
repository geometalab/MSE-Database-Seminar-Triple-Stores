from rdflib import plugin, ConjunctiveGraph, Literal, URIRef

from rdflib.store import Store
from rdflib_sqlalchemy import registerplugins

registerplugins()
identifier = URIRef("benchmark")
db_uri = Literal('postgresql+psycopg2://postgres:mysecretpassword@localhost:5432/benchmark')


def do(action):
    store = plugin.get("SQLAlchemy", Store)(identifier=identifier, configuration=db_uri)
    graph = ConjunctiveGraph(store)
    action(graph, db_uri)
    try:
        graph.close()
    except:
        pass
