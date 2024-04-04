import pygame as pyg
import random
pyg.init()

def draw(WINDOW, size, mouse_pos, play_state, level, next_piece):
    # Unpack variables
    WIDTH, HEIGHT = size
    play_width = min(400, WIDTH // 1.75)
    play_height = play_width * 2
    piece_size = play_width // 10
    pixel_size = piece_size // 8

    # Colors
    black = (24, 24, 24)
    gray = (60, 60, 60)
    green = (87, 207, 122)
    WINDOW.fill(black)

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

    # Fonts
    title_font = pyg.font.SysFont("consolas", 15)

    # Calculate the top left edge of the play area, then print said area
    left_edge = (WIDTH - play_width)/2 - max(0, play_width // 2)
    top_edge = (HEIGHT - play_height)/2 
    pyg.draw.rect(WINDOW, gray, (left_edge - piece_size-pixel_size, top_edge - piece_size-pixel_size, play_width + piece_size*2 + pixel_size, play_height + piece_size*2 + pixel_size))
    pyg.draw.rect(WINDOW, green, (left_edge - piece_size/2-pixel_size, top_edge - piece_size/2-pixel_size, play_width + piece_size + pixel_size, play_height + piece_size + pixel_size))
    pyg.draw.rect(WINDOW, black, (left_edge - pixel_size, top_edge - pixel_size, play_width + pixel_size, play_height + pixel_size))

    for x in range(10):
        for y in range(20):
            scheme = color_schemes[level]
            piece_color = play_state[x][y]
            if piece_color == -1:
                pyg.draw.rect(WINDOW, black, (left_edge + piece_size*x, top_edge + piece_size*y, piece_size, piece_size))
                continue
            # Black right edge
            pyg.draw.rect(WINDOW, black, (left_edge + piece_size*x, top_edge + piece_size*y, piece_size, piece_size))

            # Border
            if piece_color != 1:
                pyg.draw.rect(WINDOW, scheme[2], (left_edge + piece_size*x, top_edge + piece_size*y, piece_size-pixel_size, piece_size-pixel_size))
            else:
                pyg.draw.rect(WINDOW, scheme[1], (left_edge + piece_size*x, top_edge + piece_size*y, piece_size-pixel_size, piece_size-pixel_size))

            # Inside area
            pyg.draw.rect(WINDOW, scheme[0], (left_edge + piece_size*x + pixel_size, top_edge + piece_size*y + pixel_size, piece_size-pixel_size*3, piece_size-pixel_size*3))
            pyg.draw.rect(WINDOW, scheme[piece_color], (left_edge + piece_size*x + pixel_size*3, top_edge + piece_size*y + pixel_size, pixel_size*3, pixel_size))
            pyg.draw.rect(WINDOW, scheme[piece_color], (left_edge + piece_size*x + pixel_size*2, top_edge + piece_size*y + pixel_size*2, pixel_size*4, pixel_size))
            pyg.draw.rect(WINDOW, scheme[piece_color], (left_edge + piece_size*x + pixel_size, top_edge + piece_size*y + pixel_size*3, pixel_size*5, pixel_size*3))

            # Top left white pixel
            pyg.draw.rect(WINDOW, scheme[0], (left_edge + piece_size*x, top_edge + piece_size*y, pixel_size, pixel_size))
                

    pyg.display.update()