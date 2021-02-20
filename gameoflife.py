"""
Returns the changes that must be applied on the next generation as a tick

Parameters
----------
prev_gen : [[Cell, ...], ...]

Returns
-------
changes : [{"coords" : (X,Y) , "state" : 'L|D'}]
"""
def new_gen(prev_gen) -> list:
    # Empty list of changes
    changes = []
    # Check each cell on the system
    for cell in [item for row in prev_gen for item in row]:
        x,y = cell.getCoords()
        adj_coords = [(x-1, y-1), (x, y-1), (x+1, y-1),
                      (x-1, y  ),           (x+1, y  ),
                      (x-1, y-1), (x, y+1), (x+1, y+1)]
        adj_cells = [(a,b) for a,b in adj_coords if a > 0 and b > 0]
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
        changes = add_change(changes, (x,y), 'L' if n_neigh in [2,3] else 'D')
    return changes

"""
Given the changes list, appends the new change with the given parameters.
(Used to make the code much more readable)

Parameters
----------
changes : list(dict) -> List of dictionaries stating the changes on the system
coords : tuple  -> Coordinated of the cell => (X,Y)
state  : string -> New state of the cell   => 'L' (lives) OR 'D' (dies)

Returns
-------
changes : list(dict) -> List of dictionaries with the new changed
"""
def add_change(changes, coords, state) -> list:
    changes.append(
        {
            "coords" : coords,
            "state"  : state
        }
    )
    return changes
