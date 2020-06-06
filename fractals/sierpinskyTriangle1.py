"""
Sierpinsky triangle version 1
https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle
"""
import sys
from math import sqrt
import matplotlib.pyplot as plt


def sierpinskyTriangle(n, x, y, c):
    if n != 0:
        xA, yA = x, y
        xB, yB = x + c, y
        xC, yC = x + c / 2, y + c * sqrt(3)/2
        xE, yE = (xA + xB) / 2, (yA + yB) / 2
        xF, yF = (xB + xC) / 2, (yB + yC) / 2
        xG, yG = (xA + xC) / 2, (yA + yC) / 2
        # Central triangle
        plt.fill([xE, xF, xG], [yE, yF, yG], 'w')
        # Small triangles
        sierpinskyTriangle(n - 1, x, y, c / 2)
        sierpinskyTriangle(n - 1, xG, yG, c / 2)
        sierpinskyTriangle(n - 1, xE, yE, c/2)
    else:
        plt.fill([x, x + c, x + c / 2], [y, y, y + c * sqrt(3) / 2], 'b')


def sierpinskyTriangleConstruction(n):
    sierpinskyTriangle(n, 0, 0, 10)
    plt.axis("equal")
    plt.title("Sierpinsky triangle")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) == 2 else 5
    sierpinskyTriangleConstruction(n)
