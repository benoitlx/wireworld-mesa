import mesa

class Cell(mesa.Agent):

    VOID = 0
    COPPER = 1
    HEAD = 2
    TAIL = 3

    def __init__(self, pos, model, init_state=VOID):
        """
        Create a cell, in the given state, at the given x, y position
        """
        super().__init__(pos, model)
        self.x, self.y = pos
        self.state = init_state
        self.nextState = None

    @property
    def neighbors(self):
        return self.model.grid.iter_neighbors((self.x, self.y), True)

    def step(self):
        pass
