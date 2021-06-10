# Pathfinding_visualisation
This pygame script visualizes work of path-finding algorithm. 

usage: main.py [-h] [--fps FPS] [--walls_ratio WALLS_RATIO] [--hide_track] [--hide_moves] [--show_fscore] [--autooff] [--distance {euclidian,manhattan}] [--educative]

optional arguments:<br />
  &emsp;-h, --help            show this help message and exit<br />
  &emsp;--fps FPS, -f FPS     Slows the game to the given amout of FPS<br />
  &emsp;--walls_ratio WALLS_RATIO, -w WALLS_RATIO
                        Ratio of walls. Values From 0 to 1 (default - 0.5)<br />
  &emsp;--hide_track, -t      Hide choices made by algorithm while searching for path. While running in this mode wait for algorithm to find path (default - False)<br />
  &emsp;--hide_moves, -m      Hide possible moves of the algorithm (default - False)<br />
  &emsp;--show_fscore, -s     Show fscore on considered fields (default - False)<br />
  &emsp;--autooff, -a         Stops the automatization of the algorithm. User has to press right arrow key to make next move (default - False)<br />
  &emsp;--distance {euclidian,manhattan}, -d {euclidian,manhattan}
                        Distance function (default - euclidian)<br />
  &emsp;--educative, -e       Runs the program in educative mode - slower and with smaller grid (default - False)
