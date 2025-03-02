# Author: Jose Bianchi
# GitHub username: josebianchi7
# Description: file contains function to navigate a puzzle maze matrix
#   from a start cell to an end cell, while avoiding barriers, and finding
#   the shortest path using BFS.

class Queue:
    def __init__(self):
        self.dq = []

    def size(self):
        return len(self.dq)

    def enqueue(self, item):
        self.dq.append(item)

    def front(self):
        return self.dq[0]

    def dequeue(self):
        front = self.front()
        self.dq.pop(0)
        return front

    def is_empty(self):
        return len(self.dq) == 0


def solve_puzzle(board, source: tuple, destination: tuple):
    """
    Given a puzzle matrix of size m x n,
    where each cell contains either a
    barrier, denoted by '#' or is
    empty, denoted by '-', this function
    finds a minimum path from the given
    source position in the puzzle matrix
    to the given destination position.

    :param board: 2D matrix representing puzzle maze
    :param source: tuple (a,b) representing start position
    :param destination: tuple (x,y) representing end position

    :return: list of tuple positions used to get from source
    to destination or None if no path is possible.
    """
    if source == destination:
        return [source], ''

    # Validate source or destination is not a barrier position
    start = board[source[0]][source[1]]
    end = board[destination[0]][destination[1]]
    if start == '#' or end == '#':
        return None

    n = len(board)
    m = len(board[0])
    # Created dict to verify unvisited positions that can be visited
    can_visit = {}
    for i in range(n):
        for j in range(m):
            cell_pos = (i, j)
            cell_val = board[i][j]
            if cell_val == '#':
                can_visit[cell_pos] = False
            else:
                can_visit[cell_pos] = True

    # Traverse board via BFS with queue to check all neighbors of a cell before moving deeper
    can_visit[source] = False
    que = Queue()
    # Maintain copy of current in queue
    path = [source]
    que.enqueue((source, path, ''))
    while que.is_empty() is False:
        cell_pos, path, directions = que.dequeue()

        # Get viable path options based on current cell position
        path_options = _valid_neighbor_cells(n, m, cell_pos, can_visit)
        for cell_data in path_options:
            new_cell, turn = cell_data[0], cell_data[1]
            new_path = path[:]
            new_path.append(new_cell)
            new_directions = directions + turn
            # Return path that found destination cell first
            if new_cell == destination:
                return new_path, new_directions
            que.enqueue((new_cell, new_path, new_directions))
    return None


def _valid_neighbor_cells(row_max: int, col_max: int, curr_cell: tuple, unvisited_dict: dict) -> object:
    """
    Returns list of valid neighbor cells with direction for current cell.
    """
    valid_neighbors = []

    cell_row = curr_cell[0]
    cell_col = curr_cell[1]

    # Get right square
    right_cell = (cell_row, cell_col + 1)
    if cell_col + 1 < col_max and unvisited_dict[right_cell]:
        unvisited_dict[right_cell] = False
        valid_neighbors.append((right_cell, 'R'))

    # Get bottom square
    down_cell = (cell_row + 1, cell_col)
    if cell_row + 1 < row_max and unvisited_dict[down_cell]:
        unvisited_dict[down_cell] = False
        valid_neighbors.append((down_cell, 'D'))

    # Get top square
    up_cell = (cell_row - 1, cell_col)
    if cell_row - 1 >= 0 and unvisited_dict[up_cell]:
        unvisited_dict[up_cell] = False
        valid_neighbors.append((up_cell, 'U'))

    # Get left square
    left_cell = (cell_row, cell_col - 1)
    if cell_col - 1 >= 0 and unvisited_dict[left_cell]:
        unvisited_dict[left_cell] = False
        valid_neighbors.append((left_cell, 'L'))

    return valid_neighbors


if __name__ == '__main__':
    b1 = [['-', '-', '-', '-', '-'],
          ['-', '-', '#', '-', '-'],
          ['-', '-', '-', '-', '-'],
          ['#', '-', '#', '#', '-'],
          ['-', '#', '-', '-', '-']]
    s1, e1 = (0, 2), (2, 2)
    s2, e2 = (0, 0), (4, 4)
    s3, e3 = (0, 0), (4, 0)
    s4, e4 = (0, 0), (0, 0)
    print(solve_puzzle(b1, s2, e2))

