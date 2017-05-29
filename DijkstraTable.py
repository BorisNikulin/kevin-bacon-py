from queue import PriorityQueue


class DijkstraTable:

    def __init__(self, start):
        self.start = start
        # v -> (pred, edge, cost)
        self.__table = {}

    def generate_table(self, vertices, adj_func, edge_weight_func):
        """ Generates a dijkstra table given an iterator of vertices,
        a function for getting an iterator of adjacent vertices which
        is a tuple of the adjacent vertex and the edge, and a function
        for given an edge to give back a weight
        that can be added to floats."""
        visited = PriorityQueue()

        for v in vertices:
            self.__table[v] = (None, None, float('inf'))

        self.__table[self.start] = (None, None, 0.0)
        visited.put((0.0, self.start))

        while not visited.empty():
            cost, v = visited.get()

            for adj_v, e in adj_func(v):
                new_cost = cost + edge_weight_func(e)
                if new_cost < self.__table[adj_v][2]:
                    self.__table[adj_v] = (v, e, new_cost)
                    visited.put((new_cost, adj_v))

    def path_to(self, goal):
        """ Generates a list of vertex edge pairs from
        one past the start all the way to the end."""
        path = []
        current = goal
        while current != self.start:
            current, edge, _ = self.__table[current]
            path.append((current, edge))

        path.reverse()
        return path

    def len_to(self, goal):
        """ Counts the length of the path or number
        of edges from the start to the goal."""
        path_len = 0
        current = goal
        while current != self.start:
            path_len += 1
            current, _, _ = self.__table[current]
        return path_len

    def __len__(self):
        return len(self.__table)

    def __iter__(self):
        return iter(self.__table)

    def items(self):
        return self.__table.items()

    def __getitem__(self, item):
        return self.__table[item]
