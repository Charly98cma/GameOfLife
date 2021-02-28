# Conway's Game of Life
## Rules

1. Any live cell with two or three live neighbours survives.
2. Any dead cell with three live neighbours becomes a live cell.
3. All other live cells die in the next generation. Similarly, all other dead
   cells stay dead.

### Additional rules

- Births and deaths occur simultaneously (tick)
- Each generation is a pure function of the preceding one.


## How to use ("play" maybe)

The first thing you need is the initial layout, which is specified in a file
which you will pass as an argument to the Python script (the name of the file
is irrelevant).

This file must follow the next structure:
- The first number must be the **dimensions of the world** (it a square, so only
  one number is required).
- The next numbers will be a pair of values, separated by a coma, on each line,
  which represent the coordinates of the cells that are alive at the start of
  the program.

Save the file and run the script.
