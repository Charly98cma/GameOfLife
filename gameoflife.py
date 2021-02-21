from sys import exit
from time import time

from cell import Cell
import gen_changes

class GameOfLife:

    def __init__(self, dims):
        self.dims = dims
        self.world = []
        self.genWorld()
        self.loop()

    def genWorld(self):
        for i in range(self.dims):
            # Generate row
            self.world.append([])
            # Fill each position with a dead cell
            for j in range(self.dims):
                self.world[i].append(Cell((i,j),'D'))

    def loop(self):
        while True:
            # start_time = time.time()
            gen_changes.tick(
                self.world,
                gen_changes.newGen(self.world, self.dims)
            )
            # print("--- New gen transition in: %s seconds ---"
            #       % (time.time() - start_time))


def main():
    print("""Welcome to my...

     ██████   █████  ███    ███ ███████      ██████  ███████     ██      ██ ███████ ███████
     ██       ██   ██ ████  ████ ██          ██    ██ ██          ██      ██ ██      ██
      ██   ███ ███████ ██ ████ ██ █████       ██    ██ █████       ██      ██ █████   █████
       ██    ██ ██   ██ ██  ██  ██ ██          ██    ██ ██          ██      ██ ██      ██
         ██████  ██   ██ ██      ██ ███████      ██████  ██          ███████ ██ ██      ███████
    """)

    dims = int(input("Now, please, enter the dimensions: "))
    GameOfLife(dims)

if __name__ == "__main__":
    main()
