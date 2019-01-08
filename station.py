from collections import deque

class Station:
    def __init__(self, line_id, line_name, station_name, conn=None):
        self.line_id = line_id
        self.line_name = line_name
        self.station_name = station_name
        self.conn = conn
        self.trains = deque([])

    def __repr__(self):
        return '{}({}:{})'.format(self.station_name,
                                  self.line_name, self.line_id)

    def __str__(self):
        return '{}({}:{})'.format(self.station_name,
                                  self.line_name, self.line_id)
