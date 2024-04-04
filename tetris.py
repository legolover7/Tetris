# Built in modules
import subprocess
import random
import json
import sys
import os

# Custom modules
import modules.draw as draw

#  Attempt to import downloadable modules, if they're not found, install them
try:
    import pygame as pyg
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', "pygame"], stdout=subprocess.DEVNULL)
    import pygame as pyg
try:
    from screeninfo import get_monitors
except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', "screeninfo"], stdout=subprocess.DEVNULL)
    from screeninfo import get_monitors

# Get screen size based on primary monitor
for m in get_monitors():
    if m.is_primary:
        WIDTH, HEIGHT = m.width, m.height

# Initialize window
pyg.init()
WINDOW = pyg.display.set_mode((WIDTH, HEIGHT))
pyg.display.set_caption("Tetris")

os.system("cls")

FPS = 60

# Main control function
def Main():
    # Global variables
    global WINDOW, WIDTH, HEIGHT, FPS
    
    # Local variables
    level = 0
    tick = 0
    mouse_pos = (0, 0)
    clock = pyg.time.Clock()

    # Initialize the tile grid
    play_state = []
    for x in range(10):
        temp = []
        for y in range(20):
            temp += [-1]
        play_state += [temp]

        
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
                play_state[curr_px - piece_size//2 + x][curr_py + y-1] = piece_map[y * piece_size + x]


    draw.draw(WINDOW, (WIDTH, HEIGHT), mouse_pos, play_state, level, next_piece)
    # Infinite loop
    while True:
        prev_p_map = piece_map
        for event in pyg.event.get():
            mouse_pos = pyg.mouse.get_pos()
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

                elif key == pyg.K_x:
                    curr_p_state += 1
                    if curr_p_state == 4:
                        curr_p_state = 0
                elif key == pyg.K_z:
                    curr_p_state -= 1
                    if curr_p_state == -1:
                        curr_p_state = 3
                        
        piece_map = piece_states[map[curr_piece]][curr_p_state]
        piece_size = int(len(piece_map) ** 0.5)
        if prev_p_map != piece_map:
            # Mask away the piece
            for y in range(piece_size):
                for x in range(piece_size):
                    play_state[curr_px - piece_size//2 + x][curr_py + y-1] = -1

        # Fall speed
        if tick >= curr_speed:
            # Mask away the piece
            for y in range(piece_size):
                for x in range(piece_size):
                    play_state[curr_px - piece_size//2 + x][curr_py + y-1] = -1
            curr_py += 1
            tick = 0
        # Redraw
        for y in range(piece_size):
            for x in range(piece_size):
                if piece_map[y * piece_size + x] != 4:
                    play_state[curr_px - piece_size//2 + x][curr_py + y-1] = piece_map[y * piece_size + x]

        # Call draw function
        draw.draw(WINDOW, (WIDTH, HEIGHT), mouse_pos, play_state, level, next_piece)
        clock.tick(FPS)
        tick += 1

# Roll 0-7, if it's 7, reroll, if a piece is passed in, reroll once if the number is the same
def roll(curr_piece=-1):
    next_piece = 7
    while (next_piece == 7):
        next_piece = random.randint(0, 7)

    if curr_piece == -1:
        return next_piece
    else:
        if next_piece == curr_piece:
            next_piece = 7
            while (next_piece == 7):
                next_piece = random.randint(0, 7)
        return next_piece


Main()