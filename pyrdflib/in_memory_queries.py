import os
import argparse
import time
import rdflib
from queries import queries


def parse(file):
    graph = rdflib.Graph()
    start = time.time()
    print('Start parsing')
    graph.parse(file, format="nt")
    end = time.time()
    print('Finished parsing')
    print("Parse time: {0:.3f}s".format(end - start))
    return graph


def do_queries(graph):
    for key, query in queries.items():
        start = time.time()
        query_result = graph.query(query)
        number_of_entries = 0
        for _ in query_result:
            number_of_entries += 1
        end = time.time()
        print("Query: {0} , Count: {1}, Time: {2:.3f}s".format(key, number_of_entries, end - start))


def main_function():
    parser = argparse.ArgumentParser(description='SPARQL Queries with rdflib.', )
    parser.add_argument(
        '-f',
        '--file',
        action='store',
        dest='file',
        required=True,
        help='Data file (.nt).'
    )
    args = parser.parse_args()

    if os.path.isfile(args.file):
        graph = parse(args.file)
        do_queries(graph)
    else:
        print('{0} is not a existing file.'.format(args.file))


if __name__ == "__main__":
    main_function()
