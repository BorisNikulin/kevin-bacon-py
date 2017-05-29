from queue import Queue


class ALGraph:
    
    def __init__(self):
        self.__graph = {}
    
    def add_vertex_edge(self, v1, e, v2):
        if v1 not in self.__graph:
            self.__graph[v1] = []
        else:
            self.__graph[v1].append((v2, e))
    
    def add_vertex_edge_undirected(self, v1, e, v2):
        self.add_vertex_edge(v1, e, v2)
        self.add_vertex_edge(v2, e, v1)
    
    def get_adjacent(self, v):
        return self.__graph[v]
    
    def __iter__(self):
        return iter(self.__graph.items())

    def vertices(self):
        return iter(self.__graph)

    def __getitem__(self, item):
        return self.get_adjacent(item)

    def __len__(self):
        return len(self.__graph)

    def read_csv(self, file_path, vertex_class, edge_class, sep=','):
        """ Reads a csv file with 3 columns (not checked)
        that has a vertex, then a an edge label,
        and a float weight"""
        with open(file_path, 'r') as file:
            movie_to_actors = {}

            file.readline()  # skip header

            for line in file:
                vertex_edge_weight = line.strip().split(sep)
                vertex = vertex_class(vertex_edge_weight[0])
                edge = edge_class(vertex_edge_weight[1], float(vertex_edge_weight[2]))
                if edge not in movie_to_actors:
                    movie_to_actors[edge] = [vertex]
                else:
                    movie_to_actors[edge].append(vertex)

            for edge in movie_to_actors:
                actors = movie_to_actors[edge]
                for i in range(len(actors)):
                    for j in range(i + 1, len(actors)):
                        self.add_vertex_edge_undirected(actors[i], edge, actors[j])

    def bfs(self, start, goal):
        frontier = Queue()
        frontier.put(start)
        # v -> (pred, edge)
        came_from = {}

        while not frontier.empty():
            current = frontier.get()

            if current == goal:
                break

            for v, e in self.get_adjacent(current):
                if v not in came_from:
                    frontier.put(v)
                    came_from[v] = (current, e)

        result = []
        current = goal
        while current != start:
            current, adj_edge = came_from[current]
            result.append((current, adj_edge[current]))

        result.reverse()
        return start, result
