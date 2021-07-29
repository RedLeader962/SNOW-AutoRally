# coding=utf-8

import numpy as np
from PIL import Image
import argparse


def gen_costmap(input_img, config_file, output_name):
    """ Take an image of the race track plus a configuration file and output a costmap file in .npz

    The size of the `input_img` in pixels: $pixelsPerMeter^2 * (x_max - x_min) * (y_max - y_min)$

    `input_img` is a bird eye view picture of the race track. For the autorally case, the image must be oriented such
        that the origin is in the top left corner. Note: The `origin` is the starting lane of the real racetrack or the
        respawn location of the robot when run in simulation.

    `config_file` is a dictionary requiring the following keys:
        - `xBounds`: [x_min:float, x_max:float] horizontal bounds of the costmap, described in meters from the origin
            (aka distance beetwen the origin and the edge of the input_img)
        - `yBounds`: [y_min:float, y_max:float] vertical bounds of the costmap, described in meters from the origin
        - `pixelsPerMeter`: float The number of pixels in a meter
        - `imageRotation`: int angle in degrees counter clockwise.
        - `flip`: bool switch up/down
        - `rOffset`, `gOffset`, `bOffset` and `aOffset`: used to offset the color space per channel
        - `rNormalizer`, `gNormalizer`, `bNormalizer` and `aNormalizer`: used to change the amplitude of the color space
            per channel eg. 0:255 with rNormalizer=127.5 give a color space on the intervalle 0:2
        - `channelMap`: Used change chanell assignement

    Note:
        - The `channel0` key is added by the script and represent are of the race track. Values of zero indicate
        the track centerline, and values of 1.0 indicate the track boundary. Anything between 0 and 1 is a location
        on the track, and anything above 1.0 defines a region outside the boundaries.
        - The `channel1`, `channel2` and `channel3` keys are set to zeros but can be modified to add more data used by
         other classes.
        - Channel correspondance:
            `channel0` <==> red
            `channel1` <==> green
            `channel2` <==> blue
            `channel3` <==> alpha

    ref: https://github.com/RedLeader962/SNOW_AutoRally/tree/SNOW-melodic-devel/autorally_control/src/path_integral
    /params/maps


    :param input_img: the image of the race circuit
    :param config_file: costmap configuration file
    :type config_file: dict or path to a .txt file
    :param output_name: the name of the outputed costmap
    :type output_name: str
    :rtype: None
    """
    dict_file = config_file

    if type(dict_file) is dict:
        config_dict = dict_file
    else:
        with open(dict_file, 'r') as inf:
            config_dict = eval(inf.read())

    data = Image.open(input_img)

    #Rotate the image so that the origin is in the top left corner.
    data = data.rotate(config_dict["imageRotation"])

    #Cast image to numpy array
    data = np.array(data, dtype=np.float32)

    data[:, :, 0] = (data[:, :, 0] + config_dict["rOffset"])/config_dict["rNormalizer"]
    data[:, :, 1] = (data[:, :, 1] + config_dict["gOffset"])/config_dict["gNormalizer"]
    data[:, :, 2] = (data[:, :, 2] + config_dict["bOffset"])/config_dict["bNormalizer"]
    data[:, :, 3] = (data[:, :, 3] + config_dict["aOffset"])/config_dict["aNormalizer"]

    costmap = np.copy(data)
    for i in range(4):
        costmap[:, :, config_dict["channelMap"][i]] = data[:, :, i]

    if (config_dict["flip"]):
        for i in range(4):
            costmap[:, :, i] = np.flipud(costmap[:, :, i])

    #Save data to numpy array, each channel is saved individually as an array in row major order.
    track_dict = {
        "xBounds":        np.array(config_dict["xBounds"], dtype=np.float32),
        "yBounds":        np.array(config_dict["yBounds"], dtype=np.float32),
        "pixelsPerMeter": np.array(config_dict["pixelsPerMeter"], dtype=np.float32),
        "channel0":       costmap[:, :, 0].flatten(),
        "channel1":       costmap[:, :, 1].flatten(),
        "channel2":       costmap[:, :, 2].flatten(),
        "channel3":       costmap[:, :, 3].flatten()
        }

    np.savez(output_name, **track_dict)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, help="Image to generate costmap with")
    parser.add_argument("-c", "--config", type=str, help="Costmap configuration file")
    parser.add_argument("-o", "--output", type=str, help="File to save map to", default="map.npz")
    args = vars(parser.parse_args())
    gen_costmap(args["input"], args["config"], args["output"])
