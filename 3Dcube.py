import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patheffects as path_effects

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
stickercolors = ["#ffffff", "#00008f", "#ff6f00", "#ffcf00", "#009f0f", "#cf0000"]
ax.set_aspect(True)

def simple_cube(r):
    X, Y = np.meshgrid(r, r)
    ax.plot_surface(X, Y, 3, color='black', alpha=0.9)
    ax.plot_surface(X, Y, 0, color='black', alpha=0.9)
    ax.plot_surface(X, 0, Y, color='black', alpha=0.9)
    ax.plot_surface(X, 3, Y, color='black', alpha=0.9)
    ax.plot_surface(3, X, Y, color='black', alpha=0.9)
    ax.plot_surface(0, X, Y, color='black', alpha=0.9)


def plot_edge_Z(z, color_index, alpha=0.8):
    X, Y = np.meshgrid([0, 1], [0, 1])
    X1, Y1 = np.meshgrid([1, 2], [1, 2])
    X2, Y2 = np.meshgrid([2, 3], [2, 3])

    ax.plot_surface(X, Y, z, alpha=alpha, color=stickercolors[color_index[0]], shade=None)
    ax.plot_surface(X1, Y, z, alpha=alpha, color=stickercolors[color_index[1]], shade=None)
    ax.plot_surface(X2, Y, z, alpha=alpha, color=stickercolors[color_index[2]], shade=None)

    ax.plot_surface(X, Y1, z, alpha=alpha, color=stickercolors[color_index[3]], shade=None)
    ax.plot_surface(X1, Y1, z, alpha=alpha, color=stickercolors[color_index[4]], shade=None)
    ax.plot_surface(X2, Y1, z, alpha=alpha, color=stickercolors[color_index[5]], shade=None)

    ax.plot_surface(X, Y2, z, alpha=alpha, color=stickercolors[color_index[6]], shade=None)
    ax.plot_surface(X1, Y2, z, alpha=alpha, color=stickercolors[color_index[7]], shade=None)
    ax.plot_surface(X2, Y2, z, alpha=alpha, color=stickercolors[color_index[8]], shade=None)


def plot_edge_X(z, color_index, alpha=0.8):
    X, Y = np.meshgrid([0, 1], [0, 1])
    X1, Y1 = np.meshgrid([1, 2], [1, 2])
    X2, Y2 = np.meshgrid([2, 3], [2, 3])

    ax.plot_surface(z, X, Y, alpha=alpha, color=stickercolors[color_index[0]], shade=None)
    ax.plot_surface(z, X1, Y, alpha=alpha, color=stickercolors[color_index[1]], shade=None)
    ax.plot_surface(z, X2, Y, alpha=alpha, color=stickercolors[color_index[2]], shade=None)

    ax.plot_surface(z, X, Y1, alpha=alpha, color=stickercolors[color_index[3]], shade=None)
    ax.plot_surface(z, X1, Y1, alpha=alpha, color=stickercolors[color_index[4]], shade=None)
    ax.plot_surface(z, X2, Y1, alpha=alpha, color=stickercolors[color_index[5]], shade=None)

    ax.plot_surface(z, X, Y2, alpha=alpha, color=stickercolors[color_index[6]], shade=None)
    ax.plot_surface(z, X1, Y2, alpha=alpha, color=stickercolors[color_index[7]], shade=None)
    ax.plot_surface(z, X2, Y2, alpha=alpha, color=stickercolors[color_index[8]], shade=None)


def plot_edge_Y(z, color_index, alpha=0.8):
    X, Y = np.meshgrid([0, 1], [0, 1])
    X1, Y1 = np.meshgrid([1, 2], [1, 2])
    X2, Y2 = np.meshgrid([2, 3], [2, 3])

    ax.plot_surface(X, z, Y, alpha=alpha, color=stickercolors[color_index[0]], shade=None)
    ax.plot_surface(X1, z, Y, alpha=alpha, color=stickercolors[color_index[1]], shade=None)
    ax.plot_surface(X2, z, Y, alpha=alpha, color=stickercolors[color_index[2]], shade=None)

    ax.plot_surface(X, z, Y1, alpha=alpha, color=stickercolors[color_index[3]], shade=None)
    ax.plot_surface(X1, z, Y1, alpha=alpha, color=stickercolors[color_index[4]], shade=None)
    ax.plot_surface(X2, z, Y1, alpha=alpha, color=stickercolors[color_index[5]], shade=None)

    ax.plot_surface(X, z, Y2, alpha=alpha, color=stickercolors[color_index[6]], shade=None)
    ax.plot_surface(X1, z, Y2, alpha=alpha, color=stickercolors[color_index[7]], shade=None)
    ax.plot_surface(X2, z, Y2, alpha=alpha, color=stickercolors[color_index[8]], shade=None)


plot_edge_Z(3, color_index=[0, 1, 0, 4, 1,3, 2, 5, 2], alpha=1.0)
plot_edge_Z(0, color_index=[5, 1, 5, 2, 4, 1, 3, 0, 3], alpha=1.0)

plot_edge_X(0, color_index=[2, 1, 2, 4, 3, 0, 4, 3, 2], alpha=1.0)
plot_edge_X(3, color_index=[3, 0, 3, 1, 4, 4, 0, 5, 3], alpha=1.0)

plot_edge_Y(0, color_index=[4, 0, 4, 5, 2, 5, 0, 1, 4], alpha=1.0)
plot_edge_Y(3, color_index=[2, 1, 3, 0, 0, 2, 4, 1, 5], alpha=1.0)
plt.axis('off')
plt.show()
