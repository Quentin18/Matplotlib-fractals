"""
Pythagoras tree
https://en.wikipedia.org/wiki/Pythagoras_tree_(fractal)
"""
import sys
from math import sin, cos, pi
import matplotlib.pyplot as plt


def pythagorasTree(x, y, length, alpha, angle, order, counter):
    dx = length * sin(alpha)
    dy = length * cos(alpha)

    X, Y = [x], [y]

    x1 = x + dx
    y1 = y - dy
    X.append(x1)
    Y.append(y1)

    x2 = x + dx - dy
    y2 = y - dy - dx
    X.append(x2)
    Y.append(y2)

    x3 = x - dy
    y3 = y - dx
    X.append(x3)
    Y.append(y3)

    x4 = x - dy + length * cos(angle) * sin(alpha - angle)
    y4 = y - dx - length * cos(angle) * cos(alpha - angle)

    plt.fill(X, Y, color=(0, counter / color_index, 0))
    plt.axis('equal')

    if order > 0:
        pythagorasTree(
            x4, y4, length * sin(angle), alpha - angle + pi / 2,
            angle, order - 1, counter + 1)
        pythagorasTree(
            x3, y3, length * cos(angle), alpha - angle,
            angle, order - 1, counter + 1)


if __name__ == "__main__":
    x, y = 0, 0
    length = 1
    order = int(sys.argv[1]) if len(sys.argv) == 2 else 4
    angle = pi / int(sys.argv[2]) if len(sys.argv) == 3 else pi / 3
    alpha = -pi / 2
    color_index = order + 1

    pythagorasTree(x - 1, y - 1, length, -pi / 2, angle * 3 / 4, order, 1)
    plt.title("Pythagoras tree")
    plt.tight_layout()
    plt.show()
