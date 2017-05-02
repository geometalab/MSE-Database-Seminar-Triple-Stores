import time
from graph import do
from queries import queries


def query_action(graph, db_uri):
    graph.open(db_uri, create=False)
    for key, query in queries.items():
        start = time.time()
        query_result = graph.query(query)
        number_of_entries = 0
        for _ in query_result:
            number_of_entries = number_of_entries + 1
        end = time.time()
        print("Query: {0} , Count: {1}, Time: {2:.3f}s".format(key, number_of_entries, end - start))


print('begin query data')
do(query_action)
print('begin query data')
