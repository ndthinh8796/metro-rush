class Reader:
    def __init__(self, file):
        self.file = file

    def read_file(self):
        '''
            return all lines in file
        '''

        with open(self.file) as f:
            return [line.rstrip() for line in f]

    def all_possible_moves(self):
        '''
            return a dictionary
            with key is each station
            and values are possible move
        '''

        map_dict = {}
        lines = self.read_file()
        for i in range(len(lines) - 4):
            if lines[i].startswith('#'):
                key = lines[i][1:]
            else:
                line = lines[i].split(':')
                index = line[0].strip()
                station = line[1].strip()
                map_dict[(index, station, key)] = []
                self.append_moves(map_dict[(index, station, key)], key, lines, i, 0, False)
                if i > 1:
                    self.append_moves(map_dict[(index, station, key)], key, lines, i, -1)
                self.append_moves(map_dict[(index, station, key)], key, lines, i, 1)
        start, end = self.get_conditions(lines[-3:], map_dict)
        return map_dict, start, end

    def append_moves(self, value, key, lines, i, k, no=True):
        if not lines[i + k].startswith('#') and lines[i + k]:
            if not lines[i + k].count(':') > 1:
                if no:
                    index1, station1 = lines[i + k].split(':')
                    value.append((index1.strip(), station1.strip(), key.strip()))
            else:
                index1, station1, trash, rail_color1 = lines[i + k].split(':')
                if no:
                    value.append((index1.strip(), station1.strip(), key.strip()))
                for x in lines:
                    if station1 in x and rail_color1 not in x:
                        index2 = x.split(':')[0]
                        value.append((index2.strip(), station1.strip(), rail_color1.strip()))
                        break
        return value

    def get_conditions(self, lst, map):
        start = tuple(lst[0].split('=')[1].split(':'))
        end = tuple(lst[1].split('=')[1].split(':'))
        for x in map:
            if x[0] == start[1] and x[2] == start[0]:
                start = x
            if x[0] == end[1] and x[2] == end[0]:
                end = x
        return start, end
