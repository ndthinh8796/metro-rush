#!usr/bin/env python3
from algo import BFS
from graph import Graph
from station import Station
from collections import defaultdict


class MetroRush:
    def __init__(self, file):
        self.file = file
        self.lines = self.__read_file()

# ---------------------------------------------------------------------

    def __read_file(self):
        '''
            return all lines in file
        '''

        with open(self.file) as f:
            return [line.rstrip() for line in f]

# ---------------------------------------------------------------------

    def __create_station(self, line, string):
        '''
            check if station have connect point
            then return a station object
        '''

        station_elements = string.split(':')
        if len(station_elements) > 2:
            id, station, _, conn = station_elements
            return Station(id, line, station, conn.strip())
        else:
            id, station = station_elements
            return Station(id, line, station)

# ---------------------------------------------------------------------

    def __add_moves(self, stations, index, map):
        '''
            append possible moves of current station
        '''

        current = stations[index]

        if (index > 0
            and stations[index - 1].line_name == current.line_name):
            # add the station before to possible moves of current train
            map[current].append(stations[index - 1])

        if (index < len(stations) - 4
            and stations[index + 1].line_name == current.line_name):
            # add the next station to possible moves of current train
            map[current].append(stations[index + 1])

        if current.conn is not None:
            # add the connect point to possible moves
            for station in stations:
                if (current.station_name == station.station_name
                    and current.conn == station.line_name):
                    map[current].append(station)
                    break
        return map

# ---------------------------------------------------------------------

    def __create_map(self):
        '''
            create stations object and return a list
        '''
        stations = []
        for i in range(len(self.lines) - 4):
            if self.lines[i].startswith('#'):
                key = self.lines[i][1:]
            else:
                stations.append(self.__create_station(key, self.lines[i]))
        return stations

# ---------------------------------------------------------------------

    def __check_file(self):
        '''
            validate file
        '''
        from os import access, R_OK
        from os.path import isfile

        # check passed argument is file or able to read
        if not isfile(self.file) or not access(self.file, R_OK):
            stderr.write('Unable to read file!\n')
            exit(1)

        # check for 3 conditions
        if ('START' not in self.lines[-3] and
            'END' not in self.lines[-2] and
            'TRAINS' not in self.lines[-1]):
            stderr.write('Missing conditions!\n')
            exit(1)

        # check content
        for i in range(len(self.lines) - 4):
            line = self.lines[i].split(':')
            try:
                int(line[0])
            except ValueError:
                break
            if ((len(line) == 1 and not line.startswith('#'))
                or (not line.startswith('#') and i == 0)):
                break
            elif len(line) not in [2, 4]:
                break
        else:
            stderr.write('Wrong content!\n')
            exit(1)

# ---------------------------------------------------------------------

    def all_possible_moves(self):
        '''
            find all possible moves for each station
            and return a dictionary with key is station
            and value is a list of possible moves
        '''
        self.__check_file()
        moves = defaultdict(list)
        list_stations = self.__create_map()
        count = 0

        while count < len(list_stations) - 4:
            moves = self.__add_moves(list_stations, count, moves)
            count += 1
        return moves

# ---------------------------------------------------------------------

    def get_conditions(self, map):
        '''
            return start point, end point and number of trains
        '''

        start = tuple(self.lines[-3].split('=')[1].split(':'))
        end = tuple(self.lines[-2].split('=')[1].split(':'))
        trains = int(self.lines[-1].split('=')[1])
        for station in map:
            if station.line_id == start[1] and station.line_name == start[0]:
                start = station
                break
        for station in map:
            if station.line_id == end[1] and station.line_name == end[0]:
                end = station
                break
        return start, end, trains


def main():
    metrorush1 = MetroRush('delhi')
    all_moves = metrorush1.all_possible_moves()
    start, end, trains = metrorush1.get_conditions(all_moves)
    bfs = BFS(all_moves, start, end)
    path = bfs.find_shortest_path()
    bfs.run_train(trains, path)

if __name__ == '__main__':
    main()
