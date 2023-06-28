import sys
from pathlib import Path
project_dir = str(Path(__file__).absolute().parent.parent)
sys.path.append(project_dir)


from kaist_tools.trajectory import Trajectory
from utilities.logger import define_logger

import kaist_tools.plotter3d as plotter3d

LOGGER = define_logger(__name__)

if __name__ == "__main__":
    trajectory_file_path = "/home/yi/Data/KAIST_Complex_Urban_Dataset/urban33-yeouido/global_pose.csv"
    LOGGER.info("Test plot kaist trajectory...")
    traj = Trajectory()
    traj.load(trajectory_file_path)
    
