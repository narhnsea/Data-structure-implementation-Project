# Date of completion : 12-06-2023
# Author : Wobo Nancy
# Supporters: Malnika Shrestha,Sudin Adhikari
# section: ZDD

from maze import Maze

"""
    Finds a path from the 'from_cell' to the 'to_cell' in the given maze.

    Args:
        maze (Maze): An instance of the Maze class representing the maze.
        from_cell (int): The starting cell ID.
        to_cell (int): The destination cell ID.

    Returns:
        list: A list of cell IDs representing the path from 'from_cell' to 'to_cell',
              or an empty list if no path is found.
"""
def find_path(maze, from_cell, to_cell):
    # Check if starting cell is the same as destination cell
    if from_cell == to_cell:
        return [from_cell]

    # Mark the starting cell as visited
    maze.mark_cell(from_cell)

    # Helper function to check if a neighbor cell is unmarked
    def mark(neighbour):
        if maze.get_is_marked(neighbour) == False:
            return True

    # Helper function to check if a neighbor cell is the destination cell
    def equal_cell(neighbour):
        if neighbour == to_cell:
            return [from_cell, neighbour]

    # Check the right neighbor cell
    to_right = maze.get_right(from_cell)
    if to_right != -1 and mark(to_right):
        equal_cell(to_right)
        path = find_path(maze, to_right, to_cell)
        if path:
            path = [from_cell] + path
            return path

    # Check the left neighbor cell
    to_left = maze.get_left(from_cell)
    if to_left != -1 and mark(to_left):
        equal_cell(to_left)
        path = find_path(maze, to_left, to_cell)
        if path:
            path = [from_cell] + path
            return path

    # Check the up neighbor cell
    to_up = maze.get_up(from_cell)
    if to_up != -1 and mark(to_up):
        equal_cell(to_up)
        path = find_path(maze, to_up, to_cell)
        if path:
            path = [from_cell] + path
            return path

    # Check the down neighbor cell
    to_down = maze.get_down(from_cell)
    if to_down != -1 and mark(to_down):
        equal_cell(to_down)
        path = find_path(maze, to_down, to_cell)
        if path:
            path = [from_cell] + path
            return path

    # No valid path found, return an empty list
    return []
