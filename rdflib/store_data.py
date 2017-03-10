from graph import do


def store_action(graph, db_uri):
    graph.open(db_uri, create=False)  # set to False when store exists
    graph.parse('scale10000.ttl', encoding='utf-8', format='ttl')

print('begin store data')
do(store_action)
print('end store data')
