import numpy as np
class Node():
    """A* node class"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def astar(maze, start, end):

    """returns an optimal path from start point to the end point, if such a path exists"""

    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    open_list = []
    closed_list = []

    open_list.append(start_node)

    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0

        # find the cheapest node:
        for idx, node in enumerate(open_list):
            if node.f < current_node.f:
                current_index = idx
                current_node = node
        # add current node to the closed_list and remove it from the open_list:
        open_list.pop(current_index)
        closed_list.append(current_node)

        # check if find the goal, generate the path:
        if current_node == end_node:
            path = []
            c = current_node
            while c is not None:
                path.append(c.position)
                c = c.parent
            # reversed path
            return path[::-1]

        # neighbors:

        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1),
                             (1, 1)]:
            node_position = (current_node.position[0] + new_position[0],
                             current_node.position[1] + new_position[1])

            # check feasibility:
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 \
                    or node_position[1] > (len(maze[len(maze) - 1]) - 1) \
                    or node_position[1] < 0:
                continue

            # check if the node is not in the obstacle:
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # neighbor:
            new_node = Node(current_node, node_position)
            children.append(new_node)

        for child in children:
            # cost of the child:
            child.g = current_node.g + 1
            child.h = np.linalg.norm(np.asarray(child.position) - np.asarray(end_node.position))
            child.f = child.g + child.h

            for child_open in open_list:
                if child_open.position == child.position and child.g > child_open.g:
                    continue

            for child_closed in closed_list:
                if child_closed.position == child.position:
                    continue

            open_list.append(child)


def main():

    maze = [[0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (9, 9)

    path = astar(maze, start, end)
    print(path)


if __name__ == '__main__':
    main()

