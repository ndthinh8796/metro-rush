from graph import Graph
from collections import deque

class BFS(Graph):
    def find_shortest_path(self):
        if self.start == self.end:
            return [self.start]
        visited = {self.start}
        queue = deque([(self.start, [])])

        while queue:
            current, path = queue.popleft()
            visited.add(current)
            for neighbor in self.map[current]:
                if neighbor == self.end:
                    return path + [current, neighbor]
                if neighbor in visited:
                    continue
                queue.append((neighbor, path + [current]))
                visited.add(neighbor)
        return None
