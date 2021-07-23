# coding=utf-8
import numpy as np
import os


# os.getcwd()


def print_costmap_eda(costmap_path):
    costmap_data = np.load(costmap_path)

    spacer = "  "
    print os.path.basename(costmap_path)
    # print spacer, "costmap_data keys: ", costmap_data.keys(), "\n"
    print "costmap_data keys: "

    for each_i, each_v in costmap_data.items():
        if each_i == 'pixelsPerMeter' or each_i == 'xBounds' or each_i == 'yBounds':
            print spacer, each_i, each_v
        else:
            print spacer, each_i, ": shape=", each_v.shape, "min=", each_v.min(), "max=", each_v.max()

    print "\n"
    costmap_data.close()
    return None


if __name__ == '__main__':
    gaz_map_path = (
        '/catkin_ws/src/SNOW_AutoRally/autorally_control/src/path_integral/params/maps/gazebo/gazebo_map.npz')
    gaz_costmap_path = (
        '/catkin_ws/src/SNOW_AutoRally/autorally_control/src/path_integral/params/maps/gazebo_costmap_05_22_2016.npz')
    mar_costmap_path = (
        '/catkin_ws/src/SNOW_AutoRally/autorally_control/src/path_integral/params/maps/marietta_costmap_09_08_2018.npz')

print_costmap_eda(gaz_map_path)
print_costmap_eda(gaz_costmap_path)
print_costmap_eda(mar_costmap_path)
