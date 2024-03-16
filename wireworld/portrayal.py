def portrayCell(cell):
    """
    This function is to be called each tick for each cells
    to indicate how to draw the cell in the current state
    """
    if cell is None:
        raise AssertionError
    
    return {
        "Shape": "rect",
        "w": 1,
        "h": 1,
        "Filled": "true",
        "Layer": 0,
        "x": cell.x,
        "y": cell.y,
        "Color": ["black", "orange", "blue", "white"][cell.state],
    }