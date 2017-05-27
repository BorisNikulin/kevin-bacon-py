from queue import Queue
from DataClasses import *


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

    def read_csv(self, file_path, sep=','):
        file = open(file_path, 'r')
        movie_to_actors = {}

        file.readline()  # skip header

        for line in file:
            actor_movie_year = line.strip().split(sep)
            actor = Actor(actor_movie_year[0])
            movie = Movie(actor_movie_year[1], int(actor_movie_year[2]))
            if movie not in movie_to_actors:
                movie_to_actors[movie] = [actor]
            else:
                movie_to_actors[movie].append(actor)

        for movie in movie_to_actors:
            actors = movie_to_actors[movie]
            for i in range(len(actors)):
                for j in range(i + 1, len(actors)):
                    self.add_vertex_edge_undirected(actors[i], movie, actors[j])

        file.close()

    def bfs(self, start, goal):
        frontier = Queue()
        frontier.put(start)
        came_from = {}
        adj_edge = {}

        while not frontier.empty():
            current = frontier.get()

            if current == goal:
                break

            for v, e in self.get_adjacent(current):
                if v not in came_from:
                    frontier.put(v)
                    came_from[v] = current
                    adj_edge[v] = e

        result = []
        current = goal
        while current != start:
            result.append((current, adj_edge[current]))
            current = came_from[current]

        result.reverse()
        return start, result
