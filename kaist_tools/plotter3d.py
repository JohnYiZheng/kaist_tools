import yaml
import numpy as np
import matplotlib.pyplot as plt
import pytransform3d.transformations as pt

class Plotter3d:
    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(projection="3d")
        self.ax.set_xlim(-2., 2.)
        self.ax.set_ylim(-2., 2.)
        self.ax.set_zlim(-2., 2.)
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")
        self.ax.set_zlabel("z")
        self.ax.legend()
        
        self.pose_scale = 0.1

    def disable_legend(self):
        self.ax.get_legend().remove()
        
    def enable_legend(self):
        self.ax.legend()

    def plot_line(self, xs, ys, zs):
        self.ax.plot(xs, ys, zs)

    def plot_pose(self, pose):
        self.ax = pt.plot_transorm(ax=self.ax, A2B=pose, s=1.)

    def show(self):
        plt.show()

