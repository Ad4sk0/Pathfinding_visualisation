# Pathfinding_visualisation
This pygame script visualizes work of path-finding algorithm 

usage: main.py [-h] [--fps FPS] [--walls_ratio WALLS_RATIO] [--hide_track] [--hide_moves] [--show_fscore] [--autooff] [--distance {euclidian,manhattan}] [--educative]

Pathfinding algorithm visualization

optional arguments:
  -h, --help            show this help message and exit
  --fps FPS, -f FPS     Slows the game to the given amout of FPS
  --walls_ratio WALLS_RATIO, -w WALLS_RATIO
                        Ratio of walls. Values From 0 to 1 (default - 0.5)
  --hide_track, -t      Hide choices made by algorithm while searching for path. While running in this mode wait for algorithm to find path (default - False)
  --hide_moves, -m      Hide possible moves of the algorithm (default - False)
  --show_fscore, -s     Show fscore on considered fields (default - False)
  --autooff, -a         Stops the automatization of the algorithm. User has to press right arrow key to make next move (default - False)
  --distance {euclidian,manhattan}, -d {euclidian,manhattan}
                        Distance function (default - euclidian)
  --educative, -e       Runs the program in educative mode - slower and with smaller grid (default - False)
