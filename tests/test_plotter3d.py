import sys
from pathlib import Path
project_dir = str(Path(__file__).absolute().parent.parent)
sys.path.append(project_dir)

import numpy as np

from kaist_tools.plotter3d import Plotter3d

def test():
    plotter = Plotter3d()

    xs = np.linspace(0, 1, 100)
    ys = np.sin(xs * 2 * np.pi) / 2 + 0.5
    zs = np.zeros(len(xs))

    plotter.plot_line(xs, ys, zs)
    plotter.show()

if __name__ == "__main__":
    test()