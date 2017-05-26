from DijkstraTable import *
from AdjacencyList import *
from DataClasses import *
from os import path
import pickle


def search_to_string(start_vertex, path_with_edges):
    string = '{:s} -- '.format(str(start_vertex))
    path_string = []
    for v, e in path_with_edges:
        path_string.append('[{:s}] --> {:s}'.format(str(e), str(v)))
    string += ' -- '.join(path_string)
    return string


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

    ends = [Actor('HITLER, ADOLF'), Actor('HODDER, KANE'), Actor('NITU, GELU'), Actor('BERGEN, CANDICE')]

    for end in ends:
        print(search_to_string(dijkstra_table.start, dijkstra_table.get_path_to(end)))

if __name__ == "__main__":
    import cProfile
    cProfile.run('main()')
