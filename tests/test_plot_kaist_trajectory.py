from kaist_tools.trajectory import Trajectory
from utilities.logger import define_logger

import plotter3d

LOGGER = define_logger(__name__)

if __name__ == "__main__":
    trajectory_file_path = "/Users/zhengyi/Data/KAIST/urban39-pankyo/global_pose.csv"
    LOGGER.info("Test plot kaist trajectory...")
    traj = Trajectory()
    traj.load(trajectory_file_path)
    
