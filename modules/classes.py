# Import statements
import pygame as pyg
pyg.init()

class Globals:
    WINDOW = None
    WIDTH, HEIGHT = (1920, 1080)
    WINDOW_WIDTH, WINDOW_HEIGHT = (0, 0)
    VID_BUFFER = pyg.surface.Surface((WIDTH, HEIGHT))

    FPS = 60
    mouse_position = (0, 0)

    level = 0
    board_grid = []

    color_schemes = [
        [(255, 255, 255), (101, 188, 251), (69, 83, 246), (0, 0, 0)],
        [(255, 255, 255), (187, 251, 47), (52, 172, 16), (0, 0, 0)],
        [(255, 255, 255), (242, 116, 248), (210, 0, 204), (0, 0, 0)],
        [(255, 255, 255), (107, 219, 91), (69, 83, 246), (0, 0, 0)],
        [(255, 255, 255), (116, 251, 155), (218, 0, 96), (0, 0, 0)],
        [(255, 255, 255), (122, 134, 251), (116, 251, 155), (0, 0, 0)],
        [(255, 255, 255), (127, 127, 127), (236, 60, 34), (0, 0, 0)],
        [(255, 255, 255), (162, 0, 45), (119, 58, 250), (0, 0, 0)],
        [(255, 255, 255), (236, 60, 34), (69, 83, 246), (0, 0, 0)],
        [(255, 255, 255), (243, 163, 80), (236, 60, 34), (0, 0, 0)]
    ]