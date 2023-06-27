import random, pygame, sys
from pygame.locals import*

FPS, gap_size, board_height,window_width,window_height,reveal_speed, box_size, board_width= 30,10,7,640, 480, 8, 40, 10
assert(board_width * board_height)%2 == 0, 'bpoard needs to have an even number of boxes of pair of matches.'
x_margin = int((window_width - (board_width * (box_size + gap_size)))/ 2)
y_margin= int((window_height - (board_height * (box_size + gap_size)))/2)
gray = (100, 100, 100)
navy_blue = (60, 60, 100)
red, white= (255, 0, 0),(255,255,255)
green = (0, 255, 0)
blue = (0,0,255)
yellow = (255, 255, 0)
orange = (255, 128, 0)
purple = (255, 0, 255)
cyan = (0, 255, 255)

bg_color, light_bg_color, box_color, highlight_color = navy_blue, gray, white, blue
donut = 'donut'
square = 'square'
diamond,lines,oval = 'diamond','lines','oval'

all_colors = (red, white, blue, yellow, orange, purple, green)
all_shapes = (donut, square, diamond, lines, oval)
assert len(all_colors)*(all_shapes)*2 >= board_width*board_height, 'Board is too big for the numbers of shapes/colors defined.'




def  generate_Revealed_boxes_Data(val):
    revealed_boxes=[]
    for i in range(board_width):
        revealed_boxes.append([val]*board_height)
    return revealed_boxes


def get_Randomized_Board():
    icons = []
    for color in all_colors:
        for shape in all_shapes:
            icons.append((shape, color))
    
    random.shuffle(icons)
    num_icons_used = int(board_width*board_height *2)
    icons = icons[:num_icons_used]*2
    random.shuffle(icons)

    board = []
    for x in range(board_width):
        column = []
        for y in range(board_height):
            column.append(icons[0])
            del icons[0]
        board.append(column)
    return board

def split_into_groups_of(group_size, the_list):
    result =[]
    for i in range(0, len(the_list), group_size):
        result.append(the_list[i:i+group_size])
    return result
def left_top_coords_of_box(box_x, box_y):
    left = box_x*(box_size + gap_size)+x_margin
    top = box_y*( box_size + gap_size) + y_margin
    return (left, top)
def draw_icon(shape, color, box_x, box_y):
    quarter = int(box_size*0.25)
    half = int(box_size*0.5)

    left, top = left_top_coords_of_box(box_x, box_y)

    if shape == donut:
        pygame.draw.circle(window_screen, color, (left+half, top+half), half-5)
        pygame.draw.circle(window_screen, bg_color, (left + half, top+half), quarter-5)
    elif shape == square :
        pygame.draw.polygon(window_screen, color,((left+half, top), (left + box_size-1, top+half, box_size-half)))
    elif shape == lines:
        for i in range(0, box_size, 4):
            pygame.draw.line(window_screen, color, (left, top+i), (left + i,top))
            
def draw_board(board, revealed):
    for box_x in range(board_width):
        for box_y in range(board_height):
            left, top = left_top_coords_of_box(box_x, box_y)
            if not revealed[box_x][box_y]:
                pygame.draw.rect(window_screen, box_color, (left, top, box_size, box_size))
            else:
                shape, color = get_shape_and_color(board, box_x, box_y)
                draw_icon(shape, color, box_x, box_y)



def start_game_animation():
    covered_Boxes  = generate_Revealed_boxes_Data(False)
    boxes = []
    for x in range(board_width):
        for y in range(board_height):
            boxes.append((x,y))
    random.shuffle(boxes)
    box_groups = split_into_groups_of(8, boxes)

    draw_board(board, covered_Boxes)


def main():
    global fps_clock, window_screen
    pygame.init()
    fps_clock = pygame.time.Clock()
    window_screen = pygame.display.set_mode(window_width, window_height)
    mouse_xaxis , mouse_yaxis = 0,0
    pygame.display.set_caption("Memory Game")
    main_board = get_Randomized_Board()
    revealed_boxes = generate_Revealed_boxes_Data(False)
    first_selection = None
    window_screen.fill(bg_color)
    start_game_animation(main_board)
    while True:
        mouse_clicked = False
        window_screen.fill(bg_color)
        drawBoard(main_board, revealed_boxes)



