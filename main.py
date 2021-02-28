from lib import gameoflife as GoL
from sys import argv as sysArgv

def main():
    print("""Welcome to my...

     ██████   █████  ███    ███ ███████      ██████  ███████     ██      ██ ███████ ███████
     ██       ██   ██ ████  ████ ██          ██    ██ ██          ██      ██ ██      ██
      ██   ███ ███████ ██ ████ ██ █████       ██    ██ █████       ██      ██ █████   █████
       ██    ██ ██   ██ ██  ██  ██ ██          ██    ██ ██          ██      ██ ██      ██
         ██████  ██   ██ ██      ██ ███████      ██████  ██          ███████ ██ ██      ███████
    """)
    # Try-except in case the user press Ctr-C
    try:
        # Reading the init file
        with open(sysArgv[1], 'r') as f:
            layout_str = [line.rstrip('\n').split(',') for line in f]
        # Dimensions of the world
        dims = (int(layout_str[0][0]))
        # Coords of the initial layout
        layout_coords = [(int(x),int(y)) for x,y in layout_str[1:]]
        # Let the game begin :D
        GoL.GameOfLife(dims, layout_coords)
    except ValueError:
        print("--- Error reading the layout file ---")
        print("Check the values are on the correct format")
        exit(1)
    except KeyboardInterrupt:
        pass
    exit(0)

if __name__ == "__main__":
    main()
