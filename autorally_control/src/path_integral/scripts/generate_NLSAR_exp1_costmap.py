# coding=utf-8
from track_generator import gen_costmap
import os

# SRC_PATH = '/catkin_ws/src/SNOW_AutoRally/autorally_control/src/path_integral/params/maps'
SRC_PATH = 'path_integral/params/maps'
racetrack_img_path = (os.path.join(SRC_PATH, 'ulaval_wt_oval/ulaval_wt_oval.png'))

# Note: The +1 on the pix_to_meter_xMin and pix_to_meter_yMin line is used compensate for the origin anchor size in
#  the Affinity designer file (ulaval_wt_oval.afdesign). See `ulaval_wt_oval_snapshot.png` for mesure in pixel.

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
    # Note on the channel0 (the red channel): Given 0=black 127.5=gray 255=white, normalizing using 127.5 bring the
    # color space intervalle in 0:2 which is interpreted by autorally costmap function as the intervalle 0:1 being on
    # the track with 0 being the unpenalized zone and greater than 1 being outside the racetrack. The other channel
    # are not use for now and are normalized so that they become close to black.
    "rNormalizer":    127.5,
    "gNormalizer":    25500.0,
    "bNormalizer":    25500.0,
    "aNormalizer":    25500.0,
    "channelMap":     [0, 1, 2, 3]
    }

if __name__ == '__main__':
    gen_costmap(racetrack_img_path, config_dict, os.path.join(SRC_PATH, 'NLSAR_exp1_costmap'))
