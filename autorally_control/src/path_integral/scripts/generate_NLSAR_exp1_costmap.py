# coding=utf-8
from track_generator import gen_costmap
import os

# SRC_PATH = '/catkin_ws/src/SNOW_AutoRally/autorally_control/src/path_integral/params/maps'
SRC_PATH = '/Users/redleader/PycharmProjects/SNOW_AutoRally/autorally_control/src/path_integral/params/maps'
racetrack_img_path = (os.path.join(SRC_PATH, 'ulaval_wt_oval/ulaval_wt_oval.png'))

pix_to_meter_xMin = (539.8+1)/60.
pix_to_meter_xMax = 1140./60.
pix_to_meter_yMin = (220.9+1)/60.
pix_to_meter_yMax = 858.8/60.

config_dict = {
    "xBounds":        [-pix_to_meter_xMin, pix_to_meter_xMax],
    "yBounds":        [-pix_to_meter_yMin, pix_to_meter_yMax],
    "pixelsPerMeter": 60.0,
    "imageRotation":  0.0,
    "flip":           False,
    "rOffset":        0.0,
    "gOffset":        0.0,
    "bOffset":        0.0,
    "aOffset":        0.0,
    "rNormalizer":    12.75,
    # "rNormalizer":    1.0,
    "gNormalizer":    1.0,
    "bNormalizer":    1.0,
    "aNormalizer":    1.0,
    "channelMap":     [0, 1, 2, 3]
    }

if __name__ == '__main__':
    gen_costmap(racetrack_img_path, config_dict, os.path.join(SRC_PATH, 'NLSAR_exp1_costmap'))
