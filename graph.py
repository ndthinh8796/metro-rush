from abc import ABC, abstractmethod
from train import Train
from collections import deque


class Graph(ABC):
    def __init__(self, map, start, end):
        self.map = map
        self.start = start
        self.end = end
        self.shortest_path = []

    @staticmethod
    def run_train(n_trains, path):
        trains = deque([Train(i) for i in range(1, n_trains + 1)])
        path[0].trains = trains.copy()
        turn = 1

        while len(path[-1].trains) < n_trains:
            print('\nTurn: {}'.format(turn))
            print('------------------------------------')
            for i in range(len(path)):
                if (not path[i].trains and not path[-1].trains) or i == len(path) - 1:
                    for j in range(i - 1, -1, -1):
                        if path[j].trains:
                            train = path[j].trains.popleft()
                            path[j + 1].trains.append(train)
                        else:
                            break
                    break
            for x in path:
                if x.trains:
                    print('{} - {}'.format(str(x), ', '.join([str(y) for y in x.trains])))
            turn += 1

    @abstractmethod
    def find_shortest_path(self):
        pass
