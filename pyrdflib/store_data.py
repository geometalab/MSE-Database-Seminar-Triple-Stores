import os
from graph import do, read_configuration_file


def store_action(graph, db_uri):
    graph.open(db_uri, create=True)  # set to False when store exists
    config_parser = read_configuration_file('config.ini')
    path = config_parser.get('DATA', 'path', fallback='scale10000.nt')
    if not os.path.isfile(path):
        raise Exception("The data file {0} does not exist!".format(path))
    graph.parse(path, format='nt')


print('begin store data')
do(store_action)
print('end store data')
