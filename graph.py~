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
        trains = deque([Train(i, path[0]) for i in range(1, n_trains + 1)])
        path[0].trains = trains.copy()
        turn = 1

        while len(path[-1].trains) < n_trains:
            print('\nTurn: {}'.format(turn))
            print('------------------------------------')

            for i in range(n_trains):
                if i > 0 and trains[i].position < len(path) - 2:
                    forward_train = trains[i - 1].station_obj
                    next_station = path[trains[i].position + 1].station_name
                    if forward_train.station_name == next_station:
                        break
                if trains[i].position < len(path) - 1:
                    path[trains[i].position].trains.remove(trains[i])
                    trains[i].position += 1
                    trains[i].station_obj = path[trains[i].position]
                    path[trains[i].position].trains.append(trains[i])



            for x in path:
                if x.trains:
                    print('{} - {}'.format(str(x), ', '.join([str(y) for y in x.trains])))
            turn += 1

    @abstractmethod
    def find_shortest_path(self):
        pass
