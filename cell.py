class Cell:
    def __init__(self, coords, state):
        self._coords = coords
        self._state = state

    def getCoords(self):
        return self._coords

    def getState(self):
        return self._state

    def setState(self, state):
        self._state = state
