from queue import PriorityQueue


class DijkstraTable:

    def __init__(self, start, graph=None):
        self.start = start
        # v -> (pred, edge, cost)
        self.__table = {}
        if graph is not None:
            self.generate_table(graph)

    def generate_table(self, graph):
        visited = PriorityQueue()

        for v in graph.vertices():
            if v != self.start:
                self.__table[v] = (None, None, float('inf'))

        self.__table[self.start] = (None, None, 0)
        visited.put((0.0, self.start))

        while not visited.empty():
            cost, v = visited.get()

            for adj_v, e in graph.get_adjacent(v):
                new_cost = cost + e.get_weight()
                if new_cost < self.__table[adj_v][2]:
                    self.__table[adj_v] = (v, e, new_cost)
                    visited.put((new_cost, adj_v))

    def get_path_to(self, goal):
        path = []
        current = goal
        while current != self.start:
            pred, edge, cost = self.__table[current]
            path.append((current, edge))
            current = pred

        path.reverse()
        return path

    def __iter__(self):
        return iter(self.__table)

    def items(self):
        return self.__table.items()
