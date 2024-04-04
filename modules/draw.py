# Import statements
import pygame as pyg
pyg.init()

from modules.classes import Globals

def draw():
    # Unpack variables
    WIDTH, HEIGHT = Globals.WIDTH, Globals.HEIGHT
    VID_BUFFER = Globals.VID_BUFFER

    play_width = min(400, WIDTH // 1.75)
    play_height = play_width * 2
    piece_size = play_width // 10
    pixel_size = piece_size // 8

    # Colors
    black = (24, 24, 24)
    gray = (60, 60, 60)
    green = (87, 207, 122)
    VID_BUFFER.fill(black)

    # Fonts
    title_font = pyg.font.SysFont("consolas", 15)

    # Calculate the top left edge of the play area, then print said area
    left_edge = (WIDTH - play_width)/2 - max(0, play_width // 2)
    top_edge = (HEIGHT - play_height)/2 
    pyg.draw.rect(VID_BUFFER, gray, (left_edge - piece_size-pixel_size, top_edge - piece_size-pixel_size, play_width + piece_size*2 + pixel_size, play_height + piece_size*2 + pixel_size))
    pyg.draw.rect(VID_BUFFER, green, (left_edge - piece_size/2-pixel_size, top_edge - piece_size/2-pixel_size, play_width + piece_size + pixel_size, play_height + piece_size + pixel_size))
    pyg.draw.rect(VID_BUFFER, black, (left_edge - pixel_size, top_edge - pixel_size, play_width + pixel_size, play_height + pixel_size))

    for x in range(10):
        for y in range(20):
            scheme = Globals.color_schemes[Globals.level]
            piece_color = Globals.board_grid[x][y]
            if piece_color == -1:
                pyg.draw.rect(VID_BUFFER, black, (left_edge + piece_size*x, top_edge + piece_size*y, piece_size, piece_size))
                continue
            # Black right edge
            pyg.draw.rect(VID_BUFFER, black, (left_edge + piece_size*x, top_edge + piece_size*y, piece_size, piece_size))

            # Border
            if piece_color != 1:
                pyg.draw.rect(VID_BUFFER, scheme[2], (left_edge + piece_size*x, top_edge + piece_size*y, piece_size-pixel_size, piece_size-pixel_size))
            else:
                pyg.draw.rect(VID_BUFFER, scheme[1], (left_edge + piece_size*x, top_edge + piece_size*y, piece_size-pixel_size, piece_size-pixel_size))

            # Inside area
            pyg.draw.rect(VID_BUFFER, scheme[0], (left_edge + piece_size*x + pixel_size, top_edge + piece_size*y + pixel_size, piece_size-pixel_size*3, piece_size-pixel_size*3))
            pyg.draw.rect(VID_BUFFER, scheme[piece_color], (left_edge + piece_size*x + pixel_size*3, top_edge + piece_size*y + pixel_size, pixel_size*3, pixel_size))
            pyg.draw.rect(VID_BUFFER, scheme[piece_color], (left_edge + piece_size*x + pixel_size*2, top_edge + piece_size*y + pixel_size*2, pixel_size*4, pixel_size))
            pyg.draw.rect(VID_BUFFER, scheme[piece_color], (left_edge + piece_size*x + pixel_size, top_edge + piece_size*y + pixel_size*3, pixel_size*5, pixel_size*3))

            # Top left white pixel
            pyg.draw.rect(VID_BUFFER, scheme[0], (left_edge + piece_size*x, top_edge + piece_size*y, pixel_size, pixel_size))
                
    Globals.WINDOW.blit(pyg.transform.scale(VID_BUFFER, (Globals.WINDOW_WIDTH, Globals.WINDOW_HEIGHT)), (0, 0))
    pyg.display.update()