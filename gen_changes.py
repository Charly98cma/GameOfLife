"""
Returns the changes that must be applied on the next generation as a tick

Parameters
----------
prev_gen : [[Cell, ...], ...]
dims     : integer - Number of cells on each row

Returns
-------
changes : [{"coords" : (X,Y) , "state" : 'L|D'}]
"""
def newGen(prev_gen, dims) -> list:
    # Empty list of changes
    changes = []
    # Check each cell on the system
    for cell in [item for row in prev_gen for item in row]:
        x,y = cell.getCoords()
        adj_coords = [(x-1, y-1), (x, y-1), (x+1, y-1),
                      (x-1, y  ),           (x+1, y  ),
                      (x-1, y+1), (x, y+1), (x+1, y+1)]
        adj_cells = [(a,b) for a,b in adj_coords
                     if a in range(dims) and b in range(dims)]
        # Alive neighbour cell counter
        n_neigh = 0
        # Iterate trought the neighbours cells
        for neigh_x, neigh_y in adj_cells:
            # Get neighbour cell
            neigh_cell = prev_gen[neigh_x][neigh_y]
            # Check neighbour cell state
            if neigh_cell.getState() == 'L':
                n_neigh += 1
        # Kill cell if overpopulation or starvation
        if n_neigh not in [2,3] and cell.getState() == 'L':
            add_change(changes, (x,y), 'D')
        # Revive a cell with exactly 3 neighbours
        elif n_neigh == 3 and cell.getState() == 'D':
            add_change(changes, (x,y), 'L')
    return changes

"""
Given the changes list, appends the new change with the given parameters.
(Used to make the code much more readable)

Parameters
----------
changes : list(dict) -> List of dictionaries stating the changes on the system
coords : tuple  -> Coordinated of the cell => (X,Y)
state  : string -> New state of the cell   => 'L' (lives) OR 'D' (dies)

"""
def add_change(changes, coords, state) -> list:
    changes.append(
        {
            "coords" : coords,
            "state"  : state
        }
    )


"""
Applies the generational changes to each cell that will change its state

Parameters
----------
prev_gen : [[Cell, ...], ...]
changes : [{"coords" : (X,Y) , "state" : 'L|D'}]
"""
def tick(prev_gen, changes):
    for chg in changes:
        x,y = chg["coords"]
        prev_gen[x][y].setState(chg["state"])
