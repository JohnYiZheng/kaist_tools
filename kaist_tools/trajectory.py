import os
import sys

# directory reach
directory = os.path.dirname(os.path.abspath("__file__"))
sys.path.append(os.path.dirname(os.path.dirname(directory)))

import numpy as np
import pandas as pd

import utilities.logger as logger

LOGGER = logger.define_logger(__name__)

class TrajectoryPoint:
    def __init__(self):
        self.timestamp = 0.0
        self.pose = []

class Trajectory:
    def __init__(self):
        self.__dataframe = None
        self.__trajectory = []

    def load(self, path):
        if not os.path.exists(path):
            LOGGER.error("Path: %s does not exists!", path)
            return False
        LOGGER.info("load kaist trajectory at path: %s", path)
        self.__dataframe = pd.read_csv(path, names=[
            "timestamp",
            "p00", "p01", "p02", "p03",
            "p10", "p11", "p12", "p13",
            "p20", "p21", "p22", "p23"
        ])
        LOGGER.info("trajectory dataframe: %s \n", self.__dataframe)
        self.parse_pose()
        return True
    
    def parse_pose(self):
        for i, row in self.__dataframe.iterrows():
            traj_pt = TrajectoryPoint()
            traj_pt.timestamp = row.timestamp
            traj_pt.pose = np.array([
                [row.p00, row.p01, row.p02, row.p03],
                [row.p10, row.p11, row.p12, row.p13],
                [row.p20, row.p21, row.p22, row.p23],
                [    0.0,     0.0,     0.0,     0.1]
                ])
            if i < 10:
                LOGGER.debug("load trajectory point, index: %s, timestamp: %d, pose: %s",
                             i, traj_pt.timestamp, traj_pt.pose)
            self.__trajectory.append(traj_pt)
