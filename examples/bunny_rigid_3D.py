from functools import partial
import matplotlib.pyplot as plt
from Coh_Pt_Drift import RigidRegistration
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def visualize(iteration, error, X, Y, ax):
    plt.cla()
    ax.scatter(X[:, 0],  X[:, 1], X[:, 2], color='red', label='Target')
    ax.scatter(Y[:, 0],  Y[:, 1], Y[:, 2], color='blue', label='Source')
    ax.text2D(0.87, 0.92, 'Iteration: {:d}\nQ: {:06.4f}'.format(
        iteration, error), horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize='x-large')
    ax.legend(loc='upper left', fontsize='x-large')
    plt.draw()
    plt.pause(0.001)


def main():
    X = np.loadtxt('../data/bunny_target.txt')
    # synthetic data, equaivalent to X
    Y = np.loadtxt('../data/bunny_source.txt')

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    callback = partial(visualize, ax=ax)

    reg = RigidRegistration(**{'X': X, 'Y': Y, 'max_iterations' : 100}, ops=[True, True, False])
    reg.register(callback)
    plt.show()


if __name__ == '__main__':
    main()
