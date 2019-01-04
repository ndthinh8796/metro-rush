#!usr/bin/env python3
from io_helper import Reader
from algo import Algo


def main():
    all_moves, start, end = Reader('delhi').all_possible_moves()
    shortest_path = Algo()
    print(shortest_path.find_shortest_path(all_moves, start, end))

if __name__ == '__main__':
    main()
