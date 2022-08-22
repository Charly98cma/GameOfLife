class States:
  DEAD, ALIVE = 'D', 'A'

class Cell:

  def __init__(self, coords):
    self._coords = coords
    self.state = States.DEAD

  def get_coords(self):
    return self._coords

  def get_state(self):
    return self._state

  def switch_state(self):
    self._state = States.DEAD if self.state == States.ALIVE else States.Alive