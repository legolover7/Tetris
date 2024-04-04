# Built in modules
import pygame as pyg
import random
import json
import sys
import os

# Custom modules
import modules.draw as draw
from modules.classes import Globals

# Initialize window
pyg.init()
info_object = pyg.display.Info()
Globals.WINDOW_WIDTH, Globals.WINDOW_HEIGHT = info_object.current_w, info_object.current_h
Globals.WIDTH, Globals.HEIGHT = (1920, 1080)
Globals.WINDOW = pyg.display.set_mode((Globals.WINDOW_WIDTH, Globals.WINDOW_HEIGHT))
pyg.display.set_caption("Tetris")
os.system("cls")

# Main control function
def Main():    
    # Local variables
    tick = 0
    clock = pyg.time.Clock()

    # Initialize the tile grid
    for x in range(10):
        temp = []
        for y in range(20):
            temp += [-1]
        Globals.board_grid += [temp]

        
    map = {
        0: "T",
        1: "J",
        2: "Z",
        3: "O",
        4: "S",
        5: "L",
        6: "I",
        7: "Reroll"
    }
    curr_piece = roll()
    next_piece = roll(curr_piece)
    curr_p_state = 0
    curr_px, curr_py = 5, 0
    curr_speed = 8
    
    # Load piece rotations
    file = open("data/piece_rotations.json", "r")
    piece_states = json.load(file)
    file.close()

    # Display piece
    piece_map = piece_states[map[curr_piece]][curr_p_state]
    piece_size = int(len(piece_map) ** 0.5)
    if curr_piece == 0:
        curr_py += 1
    for y in range(piece_size):
        for x in range(piece_size):
            if piece_map[y * piece_size + x] != 4:
                Globals.board_grid[curr_px - piece_size//2 + x][curr_py + y-1] = piece_map[y * piece_size + x]

    while True:
        prev_p_map = piece_map
        Globals.mouse_position = pyg.mouse.get_pos()

        # Get events
        for event in pyg.event.get():
            # Window closed
            if event.type == pyg.QUIT:
                pyg.quit()
                sys.exit()

            # Key pressed
            elif event.type == pyg.KEYDOWN:
                key = event.key
                # Exit key
                if key == pyg.K_F1:
                    pyg.quit()
                    sys.exit()


        # Call draw function
        draw.draw()
        clock.tick(Globals.FPS)
        tick += 1

# Roll 0-6, if a piece is passed in, reroll once if the number is the same
def roll(curr_piece=-1):
    next_piece = random.randint(0, 6)

    if curr_piece == -1:
        return next_piece
    elif next_piece == curr_piece:
        next_piece = random.randint(0, 6)

    return next_piece


Main()