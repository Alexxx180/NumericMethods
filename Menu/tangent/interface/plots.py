from numpy import linspace
from menu.tangent.interface import TangentInterface

def DrawTangent(row: list, view: TangentInterface):
    length = 100
    for index, num in enumerate(row):
        x = float(num[0]); y = float(num[1]); f = float(num[2])

        points = linspace(x - length / 2, x + length / 2, length)
        tangent = f * (points - x) + y

        view.draw_graph(points, tangent, x, y, index)
    view.output(row)
