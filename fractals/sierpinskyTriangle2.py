"""
Sierpinsky triangle version 2
https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle
"""
import sys
import random
import matplotlib.pyplot as plt


def mid(a, b):
    return ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)


def sierpinskyTriangle(n):
    X = [0, 100, 50]
    Y = [0, 0, 100]
    plt.plot(X, Y, '.', markersize=7, color='red')
    dot = (random.random() * 100, random.random() * 100)
    x, y = [dot[0]], [dot[1]]
    for _ in range(n):
        r = random.random()
        if r < 1/3:
            dot = mid((0, 0), dot)
        elif r < 2/3:
            dot = mid((100, 0), dot)
        else:
            dot = mid((50, 100), dot)
        x.append(dot[0])
        y.append(dot[1])
    plt.plot(x, y, '.', markersize=2)
    plt.axis([-10, 110, -10, 110])
    plt.title("Sierpinsky triangle")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) == 2 else 10000
    sierpinskyTriangle(n)
