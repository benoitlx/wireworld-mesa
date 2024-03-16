import mesa

from .model import WireWorld
from .portrayal import portrayCell

canvas_element = mesa.visualization.CanvasGrid(portrayCell, 50, 50, 250, 250)

server = mesa.visualization.ModularServer(
    WireWorld, [canvas_element], "WireWorld", {"height": 50, "width": 50}
)