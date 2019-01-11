from abc import ABC, abstractmethod
from train import Train
from collections import deque


class Graph(ABC):
    def __init__(self, map, start, end):
        self.map = map
        self.start = start
        self.end = end
        self.path = []

    def __get_current_state(self):
        current_state = []
        for x in self.path:
            if x.trains:
                current_state.append('{}-{}'.format(str(x),
                                     ','.join([str(y) for y in x.trains])))
        return '|'.join(current_state)

    def run_train(self, n_trains):
        # get a list of trains objects
        trains = deque([Train(i, self.start)for i in range(1, n_trains + 1)])
        self.start.trains = trains.copy()
        turn = 1

        while len(self.end.trains) < n_trains:
            print('\nTurn: {}'.format(turn))
            print('------------------------------------')

            # loop through all trains
            for i in range(n_trains):

                # if index > 0 and current train position < end - 1
                if i > 0 and trains[i].position < len(self.path) - 2:
                    forward_train, next_station = (trains[i - 1].station_obj,
                                                   self.path[trains[i].position + 1])

                    # break if the train ahead is in
                    # a station with the same station name
                    # as the station ahead of current train
                    if forward_train.station_name == next_station.station_name:
                        break

                # move train if train position < end
                if trains[i].position < len(self.path) - 1:
                    self.path[trains[i].position].trains.remove(trains[i])
                    trains[i].position += 1
                    trains[i].station_obj = self.path[trains[i].position]
                    self.path[trains[i].position].trains.append(trains[i])

            print(self.__get_current_state())

    @abstractmethod
    def find_shortest_path(self):
        pass
