import numpy as np


def set_new_game_state(grid, col, row, value):
    grid[col][row] = value


def get_matching_coordinates(grid, x):
    coordinates = np.where(grid == x)
    return [tuple(i) for i in zip(coordinates[0], coordinates[1])]


def get_tile_info_at(grid, x, y):
    return grid[y][x]


def get_tile_count_x(grid):
    pass


def get_tile_count_y(grid):
    pass


def to_string(grid):
    return "TODO"
