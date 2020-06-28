from functools import partial
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from Coh_Pt_Drift import RigidRegistration
import numpy as np


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
    fish_target = np.loadtxt('../data/fish_target.txt')
    X = np.zeros((fish_target.shape[0], fish_target.shape[1] + 1))
    X[:, :-1] = fish_target

    fish_source = np.loadtxt('../data/fish_source.txt')
    Y = np.zeros((fish_source.shape[0], fish_source.shape[1] + 1))
    Y[:, :-1] = fish_source

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    callback = partial(visualize, ax=ax)

    reg = RigidRegistration(**{'X': X, 'Y': Y})
    reg.register(callback)
    plt.show()


if __name__ == '__main__':
    main()
