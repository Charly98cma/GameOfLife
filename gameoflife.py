import pygame
from pygame.locals import QUIT

from sys   import exit
from time  import time, sleep
from numpy import empty as npEmpty

from cell import Cell
import gen_changes

FPS = 30
FramePerSec = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH  = 720
HEIGHT = 720
CAPTION = "The Game of Life"

class GameOfLife:

    def __init__(self, dims):
        # Params and values
        self.nth_gen = 1
        self.dims = dims
        self.world = npEmpty((dims, dims), Cell)
        self.changes = []
        # Pygame parameters initialization
        self.screen = None
        # Running methods
        try:
            self.genWorld(self.userInput())
            self.loop()
        except KeyboardInterrupt:
            pass
        print("\n--- Number of generations: %s" % self.nth_gen)

    def userInput(self):
        print("\nEnter the coordinates of the living cells [Format => X,Y]")
        print("-- Write DONE to finish --")
        livingCells = []
        while True:
            try:
                userInput = input()
                if userInput == "" or userInput == "DONE":
                    print("\nLiving cells ->", livingCells)
                    return livingCells
                coords = userInput.split(',')
                livingCells.append((int(coords[0]), int(coords[1])))
            except (ValueError, IndexError):
                print("The coordinates must be on the format \"X,Y\"")

    def genWorld(self, livingCells):
        for i in range(self.dims):
            # Fill each position with a dead cell
            for j in range(self.dims):
                self.world[i,j] = Cell((i,j),
                                       'L' if (i,j) in livingCells else 'D')
        self.initGrid(livingCells)

    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            FramePerSec.tick(FPS)
            # start_time = time.time()
            self.changes = gen_changes.newGen(self.world, self.dims)
            # PREMATURE EXIT FOR TESTING
            # if len(self.changes) == 0:
            #     return
            self.nth_gen += 1
            gen_changes.tick(
                self.world,
                self.changes
            )
            self.drawGrid(self.changes)
            # print("--- New gen transition in: %s seconds ---"
            #       % (time.time() - start_time))

    def initGrid(self, livingCells):
        # Pygame thingys
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.screen.fill(WHITE)
        pygame.display.set_caption(CAPTION)
        # Read coords of living cells
        for x,y in livingCells:
            pygame.draw.rect(
                self.screen,
                BLACK,
                (
                    x*WIDTH//self.dims, y*HEIGHT//self.dims, # Coordinates to place
                      WIDTH//self.dims,   HEIGHT//self.dims   # Dimensions (AxB)
                )
        )
        pygame.display.update()
        sleep(0.25)

    def drawGrid(self, changes):
        for chg in changes:
            x,y   = chg["coords"]
            state = chg["state"]
            pygame.draw.rect(
                self.screen,
                BLACK if state == 'L' else WHITE,
                (
                    x*WIDTH//self.dims, y*HEIGHT//self.dims, # Coordinates to place
                      WIDTH//self.dims,   HEIGHT//self.dims   # Dimensions (AxB)
                )
            )
        pygame.display.update()
        sleep(0.05)
