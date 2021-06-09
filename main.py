import argparse

def main():
    parser = argparse.ArgumentParser(description='Pathfinding algorithm visualization')

    parser.add_argument('--fps', '-f', action='store',
                    help='Slows the game to the given amout of FPS', type=int)
    parser.add_argument('--walls_ratio', '-w', action='store', type=float, default=0.5,
                    help='Ratio of walls. Values From 0 to 1 (default - 0.5)')
    parser.add_argument('--hide_track', '-t', action='store_true',
                    help='Hide choices made by algorithm while searching for path. While running in this mode wait for algorithm to find path (default - False)')
    parser.add_argument('--hide_moves', '-m', action='store_true',
                    help='Hide possible moves of the algorithm (default - False)')
    parser.add_argument('--show_fscore', '-s', action='store_true',
                    help='Show fscore on considered fields (default - False)')
    parser.add_argument('--autooff', '-a', action='store_true',
                    help='Stops the automatization of the algorithm. User has to press right arrow key to make next move (default - False)')
    parser.add_argument('--distance', '-d', action='store', default='euclidian', choices=['euclidian', 'manhattan'],
                    help='Distance function (default - euclidian)')
    parser.add_argument('--educative', '-e', action='store_true',
                    help='Runs the program in educative mode - slower and with smaller grid (default - False)')

    args = parser.parse_args()

    if args.walls_ratio > 1:
        args.walls_ratio = 1
    if args.walls_ratio < 0:
        args.walls_ratio = 0

    from game import game   
    game(args)

if __name__ == "__main__":
    main()