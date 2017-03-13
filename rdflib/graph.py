import configparser
import os
from rdflib import plugin, ConjunctiveGraph, Literal, URIRef

from rdflib.store import Store
from rdflib_sqlalchemy import registerplugins


def read_configuration_file(config_file_path):
    if not os.path.isfile(config_file_path):
        raise Exception("The config file does not exist!")
    config_parser = configparser.ConfigParser()
    config_parser.read(config_file_path)
    return config_parser


registerplugins()

config_parser = read_configuration_file('config.ini')
server = config_parser.get('POSTGRES', 'server', fallback='localhost')
port = config_parser.get('POSTGRES', 'port', fallback='5432')
database = config_parser.get('POSTGRES', 'database', fallback='benchmark')
password = config_parser.get('POSTGRES', 'password', fallback='mysecretpassword')


identifier = URIRef("benchmark")
db_uri = Literal('postgresql+psycopg2://postgres:{0}@{1}:{2}/{3}'.format(password, server, port, database))


def do(action):
    store = plugin.get("SQLAlchemy", Store)(identifier=identifier, configuration=db_uri)
    graph = ConjunctiveGraph(store)
    action(graph, db_uri)
    try:
        graph.close()
    except:
        pass


