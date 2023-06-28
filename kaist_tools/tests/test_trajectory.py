import os
import sys
# directory reach
directory = os.path.dirname(os.path.abspath("__file__"))
sys.path.append(os.path.dirname(os.path.dirname(directory)))

from kaist_tools.trajectory import Trajectory

def test():
    trajectory_file_path = "/Users/zhengyi/Data/KAIST/urban39-pankyo/global_pose.csv"
    traj = Trajectory()
    traj.load(trajectory_file_path)

if __name__ == "__main__":
    test()