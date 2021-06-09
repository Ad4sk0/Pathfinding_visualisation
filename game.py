# TODO implement other pathfinding algorithms DFS, BFS, Dijkstra
import pygame
import random
from a_star import AStar

COLORS = {
    "white": (255, 255, 255),
    "gray": (200, 200, 200),
    "black": (0, 0, 0),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "yellow": (255, 255, 0),
    "orange": (235, 174, 52),
    "blue": (0, 0, 255)
}

# Window object
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Path finding")
pygame.font.init()

# Background object
BACKGROUND = pygame.Rect(0, 0, WIDTH, HEIGHT)
BACKGROUND_COLOR = COLORS['gray']
pygame.draw.rect(WIN, BACKGROUND_COLOR, BACKGROUND)

# Grid settings
GRID_LINE_WIDTH = 0

# Settings
S = {
    "fps" : False,
    "walls_ratio" : 0.5,
    "hide_track" : False,
    "hide_moves" : False,
    "show_fscore" : False,
    "autooff" : False,
    "rows_n": 60,
    "cols_n": 60,
    "distance": 'euclidian'
}

# Fonts
SCORE_FONT = pygame.font.SysFont('Arial', WIDTH // 70)

def settings(args):
    """Change settings accordingly to passed initial parameters""" 
    for arg, value in vars(args).items():
        if value:
            S[arg] = value
    
    if args.educative:
        S['rows_n'] = 20
        S['cols_n'] = 20
        S['fps'] = 5
        S['show_fscore'] = True
        global GRID_LINE_WIDTH
        GRID_LINE_WIDTH = 1

class Spot:
    def __init__(self, row, col):
        self.g = 0 # g score is the cost of the path from the start node to this object
        self.h = 0 # h score is heuristic function that estimates the cost of the cheapest path from this object to the goal
        self.f = 0 # f score g + h
        self.row = row
        self.col = col
        self.coords = (row, col)
        self.color = BACKGROUND_COLOR
        self.neighbours = []
        self.is_wall = False
        self.is_start = False
        self.is_end = False
        self.considered = False
        self.is_current = False
        self.previous = False
        self.is_path = False

    def add_neighbor(self,neighbor):
        self.neighbours.append(neighbor)

def create_grid():
    """Creates grid for the algorithm fieled with Spot objects"""
    rows = S['rows_n']
    cols = S['cols_n']

    grid = [[Spot(row, col) for row in range(rows)] for col in range(cols)]

    # Add neighbours
    for col in range(cols):
        for row in range(rows):
            if row > 0:
                grid[col][row].add_neighbor(grid[col][row-1])  # above
            if row < rows-1:
                grid[col][row].add_neighbor(grid[col][row+1])  # below
            if col < cols - 1:
                grid[col][row].add_neighbor(grid[col+1][row])  # right
            if col > 0:
                grid[col][row].add_neighbor(grid[col-1][row])  # left
            if col > 0 and row > 0:
                grid[col][row].add_neighbor(grid[col-1][row-1]) # left above
            if col < cols - 1 and row > 0:
                grid[col][row].add_neighbor(grid[col+1][row-1]) # right above
            if col > 0 and row < rows - 1:
                grid[col][row].add_neighbor(grid[col-1][row+1]) # left below
            if col < cols - 1 and row < rows - 1:
                grid[col][row].add_neighbor(grid[col+1][row+1]) # right below
    return grid

def draw_rectangles(area, grid, surface=WIN):
    """Add color to Spot objects"""
    rows = S['rows_n']
    cols = S['cols_n']

    col_size = area.w / cols
    row_size = area.h / rows
    for col in range(cols):
        for row in range(rows):
            square = pygame.Rect(area.x + col * col_size, area.y + row * row_size, col_size, row_size)

            # Color possible moves
            if not S['hide_moves'] and grid[col][row].considered:
                grid[col][row].color = COLORS['orange'] 

            # Color current choosen field
            if not S['hide_track'] and grid[col][row].is_current:
                grid[col][row].color = COLORS['blue']  

            # Color final path 
            if grid[col][row].is_path:
                grid[col][row].color = COLORS['yellow']

            # Color start field
            if grid[col][row].is_start:
                grid[col][row].color = COLORS['green'] 
            
            # Color end field
            if grid[col][row].is_end:
                grid[col][row].color = COLORS['red'] 
            
            pygame.draw.rect(surface, grid[col][row].color, square)

            # Add f score string to considered fields
            if S['show_fscore'] and grid[col][row].considered:
                f_score_string = str(round(grid[col][row].f))
                score_text = SCORE_FONT.render(f_score_string, True, COLORS['black'])
                WIN.blit(score_text, (area.x + col * col_size, area.y + row * row_size))

def draw_grid(area, surface=WIN, line_color = COLORS['white']):
    """Draws grid fitted within area object"""
    rows = S['rows_n']
    cols = S['cols_n']
    line_width=GRID_LINE_WIDTH
    
    col_size = area.width / cols
    row_size = area.height / rows

    for col in range(1, cols):
        # dont draw last line
        if col == cols:
            continue
        pygame.draw.line(surface, line_color, (area.x + col * col_size, area.y),
                         (area.x + col * col_size, area.y + area.height), line_width)

    for row in range(1, rows):
        # dont draw last line
        if row == rows:
            continue
        pygame.draw.line(surface, line_color, (area.x, area.y + row * row_size),
                         (area.x + area.width, area.y + row * row_size), line_width)

def generate_walls(grid, walls_ratio, start, end):
    """takes grid object and appends walls"""
    cols = len(grid)
    for col in range(cols):
        rows_with_walls_indicies = random.sample(range(0, cols), k=int(cols*walls_ratio)) # same number of walls in each column
        #if random.random() > walls_ratio: # alternative way for creating walls with random number of walls in each column 
        for row in rows_with_walls_indicies:
            if col not in [start[0], start[1], end[0], end[1]]:
                grid[col][row].is_wall = True
                grid[col][row].color = COLORS['black']
    return grid

def draw_window(grid):
    draw_rectangles(BACKGROUND, grid)
    draw_grid(BACKGROUND)
    pygame.display.update()

def game(args):
    settings(args)
    start = (0, 0)
    end = (S['rows_n'] -1, S['cols_n'] -1)
    clock = pygame.time.Clock()
    run = True
    is_searching = True
    grid = create_grid()
    grid = generate_walls(grid, S['walls_ratio'], start, end)

    grid[start[0]][start[1]].is_start = True
    grid[end[0]][end[1]].is_end = True

    algorithm = AStar(grid, start, end, S['distance'])

    while run:
        if S['fps']:
            clock.tick(S['fps'])
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and S['autooff'] and is_searching:
                    is_searching = algorithm.check_next_field()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        if not S['autooff'] and is_searching:
            is_searching = algorithm.check_next_field()
        draw_window(grid)
            
    pygame.quit()