import time
from graph import do
from queries import queries


def query_action(graph, db_uri):
    graph.open(db_uri, create=False)
    times = []
    for key, query in queries.items():
        start = time.time()
        query_result = graph.query(query)
        end = time.time()
        times.append(dict(key=key, time=end - start, result=query_result))

    for entry in times:
        count = 0
        for _ in entry['result']:
            count = count + 1
        print("Query: {0} , Count: {1}, Time: {2}s".format(entry['key'], count, entry['time']))


print('begin query data')
do(query_action)
print('begin query data')
