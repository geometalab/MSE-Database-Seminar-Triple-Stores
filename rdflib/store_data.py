import os
import time
from rdflib import ConjunctiveGraph
from graph import do, read_configuration_file


def store_action(graph, db_uri):
    graph.open(db_uri, create=True)  # set to False when store exists
    config_parser = read_configuration_file('config.ini')
    path = config_parser.get('DATA', 'path', fallback='scale10000.nt')
    if not os.path.isfile(path):
        raise Exception("The data file {0} does not exist!".format(path))
    parse_graph = ConjunctiveGraph()
    print('Start parsing')
    start = time.time()
    parse_graph.parse(path, format='nt')
    end = time.time()
    print('end parsing, time spent {0}s'.format(end-start))
    graph.addN(parse_graph)


print('begin store data')
do(store_action)
print('end store data')
