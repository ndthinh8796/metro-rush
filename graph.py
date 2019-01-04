from abc import ABC, abstractmethod


class Graph(ABC):
    def __init__(self):
        self.path = []

    @abstractmethod
    def find_shortest_path(graph, start, end, path):
        pass
