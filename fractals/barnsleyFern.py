"""
Barnsley fern
https://en.wikipedia.org/wiki/Barnsley_fern
"""
import sys
import numpy as np
import random
import matplotlib.pyplot as plt


def f1(x, y):
    return np.array([[0, 0], [0, 0.16]]).dot(np.array([x, y]))


def f2(x, y):
    return (np.array([[0.85, 0.04], [-0.04, 0.85]]).dot(np.array([x, y]))
            + np.array([0, 1.6]))


def f3(x, y):
    return (np.array([[0.20, -0.26], [0.23, 0.22]]).dot(np.array([x, y]))
            + np.array([0, 1.6]))


def f4(x, y):
    return (np.array([[-0.15, 0.28], [0.26, 0.24]]).dot(np.array([x, y]))
            + np.array([0, 0.44]))


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) == 2 else 100000
    x, y = [0], [0]
    for _ in range(n):
        r = random.random()
        if r < 0.01:
            dot = f1(x[-1], y[-1])
        elif r < 0.86:
            dot = f2(x[-1], y[-1])
        elif r < 0.93:
            dot = f3(x[-1], y[-1])
        else:
            dot = f4(x[-1], y[-1])
        x.append(dot[0])
        y.append(dot[1])
    plt.plot(x, y, '.', markersize=2, color='g')
    plt.title("Barnsley fern")
    plt.tight_layout()
    plt.show()
