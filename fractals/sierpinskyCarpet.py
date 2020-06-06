"""
Sierpinsky carpet
https://en.wikipedia.org/wiki/Sierpinski_carpet
"""
import sys
import numpy as np
import matplotlib.pyplot as plt


def sierpinskiCarpet(n):
    n += 1
    T = np.ones((3**n, 3**n))
    a = n
    start = 1
    step = 3
    size = 1
    while a > 0:
        for i in range(start, 3**n, step):
            for j in range(start, 3**n, step):
                for k in range(size):
                    for l in range(size):
                        T[i + k, j + l] = 0
        a -= 1
        start *= 3
        step *= 3
        size *= 3
    plt.matshow(T, cmap=plt.get_cmap('hot'))
    plt.title("Sierpinsky carpet")
    plt.show()


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) == 2 else 4
    sierpinskiCarpet(n)
