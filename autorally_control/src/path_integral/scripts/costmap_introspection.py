# coding=utf-8
import numpy as np
import os
from PIL import Image
import matplotlib.pyplot as plt


# os.getcwd()


def print_costmap_eda(costmap_path):
    with np.load(costmap_path) as costmap_data:

        spacer = "  "
        path = os.path.basename(costmap_path)
        print path
        # print spacer, "costmap_data keys: ", costmap_data.keys(), "\n"
        print "costmap_data keys: "

        for each_i, each_v in costmap_data.items():
            w = int((float(costmap_data['xBounds'][1]) - float(costmap_data['xBounds'][0]))*float(
                costmap_data['pixelsPerMeter']))
            h = int((float(costmap_data['yBounds'][1]) - float(costmap_data['yBounds'][0]))*float(
                costmap_data['pixelsPerMeter']))

            if each_i == 'pixelsPerMeter' or each_i == 'xBounds' or each_i == 'yBounds':
                print spacer, each_i, each_v
            elif each_i == 'channel0':
                print spacer, each_i, ": shape=", each_v.shape, "min=", each_v.min(), "max=", each_v.max()

                channel = costmap_data['channel0']
                img = channel.reshape((w, h))
                # img = np.array(img*255, dtype=np.uint8)
                img = np.array(img, dtype=np.uint8)
                img = Image.fromarray(img)
                img.save("channel_preview/" + path[:-4] + "_channel0.jpg")
            elif each_i == 'channel1':
                print spacer, each_i, ": shape=", each_v.shape, "min=", each_v.min(), "max=", each_v.max()

                channel = costmap_data['channel1']
                img = channel.reshape((w, h))
                img = np.array(img, dtype=np.uint8)
                img = Image.fromarray(img)
                img.save("channel_preview/" + path[:-4] + "_channel1.jpg")
            else:
                print spacer, each_i, ": shape=", each_v.shape, "min=", each_v.min(), "max=", each_v.max()

        print "\n"

    return None


if __name__ == '__main__':

    # SRC_PATH = '/catkin_ws/src/SNOW_AutoRally/autorally_control/src/path_integral/params/maps'
    SRC_PATH = '/Users/redleader/PycharmProjects/SNOW_AutoRally/autorally_control/src/path_integral/params/maps'

    gaz_map_path = (os.path.join(SRC_PATH, 'gazebo/gazebo_map.npz'))
    mar_costmap_2018_path = (os.path.join(SRC_PATH, 'marietta_costmap_09_08_2018.npz'))
    # gaz_costmap_path = (os.path.join(SRC_PATH, 'gazebo_costmap_05_22_2016.npz'))
    # mar_costmap_2015_path = (os.path.join(SRC_PATH, 'marietta_costmap_12_06_2015.npz'))
    # ccrf_costmap_2017_path = (os.path.join(SRC_PATH, 'ccrf_costmap_09_29_2017.npz'))
    NLSAR_exp1_costmap_path = (os.path.join(SRC_PATH, 'NLSAR_exp1_costmap.npz'))

    print_costmap_eda(gaz_map_path)
    print_costmap_eda(mar_costmap_2018_path)
    print_costmap_eda(NLSAR_exp1_costmap_path)
    # print_costmap_eda(gaz_costmap_path)
    # print_costmap_eda(mar_costmap_2015_path)
    # print_costmap_eda(ccrf_costmap_2017_path)
