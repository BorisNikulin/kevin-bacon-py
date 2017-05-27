from DijkstraTable import *
from AdjacencyList import *
from DataClasses import *
from os import path
import pickle


def search_to_string(start_vertex, path_with_edges):
    path_string = ['{:s}'.format(str(start_vertex))]
    for v, e in path_with_edges:
        path_string.append('[{:s}] --> {:s}'.format(str(e), str(v)))
    return ' -- '.join(path_string)


def path_to_bacon_number(path):
    return len(path)


def main():
    graph_serialized_filename = 'graph.pickle'
    dijkstra_table_serialized_filename = 'dijkstra_table.pickle'
    dijkstra_table = DijkstraTable(Actor('BACON, KEVIN (I)'))

    if not path.isfile(dijkstra_table_serialized_filename):
        graph = ALGraph()
        # since i have the dijkstra_pickle i could just not serialize the graph
        if not path.isfile(graph_serialized_filename):
            with open(graph_serialized_filename, 'wb') as f:
                graph.read_csv('movie_casts.tsv', '\t')
                pickle.dump(graph, f, 4)
        else:
            with open(graph_serialized_filename, 'rb') as f:
                graph = pickle.load(f)

        with open(dijkstra_table_serialized_filename, 'wb') as f:
            dijkstra_table.generate_table(graph)
            pickle.dump(dijkstra_table, f, 4)
    else:
        with open(dijkstra_table_serialized_filename, 'rb') as f:
            dijkstra_table = pickle.load(f)

    ends = ['BACON, KEVIN (I)', 'ABDOO, ROSE', 'BERGEN, CANDICE', 'HITLER, ADOLF', 'NITU, GELU', 'TABAKIN, RALPH']

    for end in ends:
        print(search_to_string(dijkstra_table.start, dijkstra_table.get_path_to(Actor(end))))
    print()

    bacon_counts = {i: 0 for i in range(6)}
    for v in dijkstra_table:
        bacon_counts[path_to_bacon_number(dijkstra_table.get_path_to(v))] += 1

    print('Bacon Number Table')
    for num, count in bacon_counts.items():
        if count != 0:
            print('{:d}: {:d}'.format(num, count))

if __name__ == "__main__":
    # import cProfile
    # cProfile.run('main()')
    main()
