import time
from graph import do
from queries import queries


def query_action(graph, db_uri):
    graph.open(db_uri, create=False)
    times = []
    for key, query in queries.items():
        start = time.time()
        _ = graph.query(query)
        end = time.time()
        times.append(dict(key=key, time=end - start))

    [print(t) for t in times]


do(query_action)
