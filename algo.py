from graph import Graph

class Algo(Graph):
    def find_shortest_path(self, graph, start, end, path=[]):
        # path = path + [start]
        # print(path)
        # if start == end:
        #     return path
        # if not start in graph:
        #     return None
        # shortest = None
        # for node in graph[start]:
        #     if node not in path:
        #         newpath = self.find_shortest_path(graph, node, end, path)
        #         if newpath:
        #             if not shortest or len(newpath) < len(shortest):
        #                 shortest = newpath
        # return shortest
        path = path + [start]
        if start == end:
            return path
        if not start in graph:
            return None
        for node in graph[start]:
            if node not in path:
                newpath = self.find_shortest_path(graph, node, end, path)
                if newpath: return newpath
        return None
