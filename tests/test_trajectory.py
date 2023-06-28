import sys
from pathlib import Path
project_dir = str(Path(__file__).absolute().parent.parent)
sys.path.append(project_dir)

from kaist_tools.trajectory import Trajectory

def test():
    trajectory_file_path = "/home/yi/Data/KAIST_Complex_Urban_Dataset/urban33-yeouido/global_pose.csv"
    traj = Trajectory()
    traj.load(trajectory_file_path)

if __name__ == "__main__":
    test()