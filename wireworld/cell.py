import mesa

class Cell(mesa.Agent):

    VOID = 0
    COPPER = 1
    HEAD = 2
    TAIL = 3

    def __init__(self, pos, model, init_state=VOID) -> None:
        """
        Create a cell, in the given state, at the given x, y position
        """
        super().__init__(pos, model)
        self.x, self.y = pos
        self.state = init_state
        self._nextState = None

    @property
    def neighbors(self) -> iter:
        return self.model.grid.iter_neighbors((self.x, self.y), True)

    @property
    def isHead(self) -> bool:
        return self.state == self.HEAD

    def step(self) -> None:
        """
        Compute the nextState according to the rules of wireworld
        """
        match self.state:
            case self.VOID:
                self._nextState = self.VOID
            case self.HEAD:
                self._nextState = self.TAIL
            case self.TAIL:
                self._nextState = self.COPPER
            case self.COPPER:
                n_heads = sum(n.isHead for n in self.neighbors)
                if n_heads == 1 or n_heads == 2:
                    self._nextState = self.HEAD
                else:
                    self._nextState = self.COPPER


    def advance(self) -> None:
        self.state = self._nextState