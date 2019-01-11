from graph import Graph
from collections import deque

class BFS(Graph):
    def find_shortest_path(self):
        # if start == end return immidiately
        if self.start == self.end:
            return [self.start]

        visited = {self.start}
        queue = deque([(self.start, [])])

        while queue:
            # get current station and path list from start to station
            current, path = queue.popleft()

            # add station to visited
            visited.add(current)

            # parse through neighbor stations of current station
            for neighbor in self.map[current]:

                # return if one of the neighbor is end point
                if neighbor == self.end:
                    return path + [current, neighbor]

                # continue if neighbor already visited
                if neighbor in visited:
                    continue

                # append neighbor station, path to wait list
                queue.append((neighbor, path + [current]))
                # add neighbor station to visited
                visited.add(neighbor)

        # if no path found
        return None
