"""
Vicsek fractal
https://en.wikipedia.org/wiki/Vicsek_fractal
"""
import sys
import numpy as np
import matplotlib.pyplot as plt


def vicsek0():
    T = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
    plt.matshow(T, cmap=plt.get_cmap('hot'))
    plt.title("Viscek fractal")
    plt.show()


def vicsek1():
    T1 = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
    T2 = np.ones((3, 3))
    T3 = np.hstack((T2, T1, T2))
    T4 = np.hstack((T1, T2, T1))
    T5 = np.vstack((T4, T3, T4))
    plt.matshow(T5, cmap=plt.get_cmap('hot'))
    plt.title("Viscek fractal")
    plt.show()


def vicsek(n):
    T1 = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
    for i in range(1, n + 1):
        T2 = np.ones((3**i, 3**i))
        T3 = np.hstack((T2, T1, T2))
        T4 = np.hstack((T1, T2, T1))
        T1 = np.vstack((T4, T3, T4))
    plt.matshow(T1, cmap='hot')
    plt.title("Viscek fractal")
    plt.show()


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) == 2 else 4
    vicsek(n)
