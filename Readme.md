# CARLA
## _Open-source simulator for autonomous driving research_

[![N|Solid](http://carla.org//img/logo/carla-black-m.png)](https://carla.org/)


## Installation

**REQUIRED**
- Windows or Linux OS
- Python versions 2.7, 3.6, 3.7, and 3.8


**Install the Pygame and Numpy.**

```sh
pip3 install --user pygame numpy
or
pip2 install --user pygame numpy
```

**Download CARLA repository**
(This tutorial was done and tested on version 0.9.13, but you are free to try on newer releases)
[CARLA Repository](https://github.com/carla-simulator/carla/blob/master/Docs/download.md) 


**Import additional assets (Optional)**
This adicitional assets includes the maps Town06, Town07, and Town10.

**Install CARLA Python package**
```sh
pip3 install carla
or
pip2 install carla
```

## Running CARLA

**Run the server side**
By default CARLA runs on localhost with the port 2000.
Linux
```sh
cd path/to/carla/root
./CarlaUE4.sh
```
Windows
```sh
cd path/to/carla/root
CarlaUE4.exe
```

**Configuration of the CARLA server**
```sh
cd PythonAPI\util
./config.py --no-rendering      # Disable rendering
./config.py --map Town05        # Change map
./config.py --weather ClearNoon # Change weather
./config.py --help # Check all the available configuration options
```

**Generate traffic on CARLA world**
By default will generate 30 vehicles and 10 pedestrians, but can be changed specifying the values with the arguments '-n' '-w' respectively
```sh
cd PythonAPI\examples
python generate_traffic.py
```

**Run CARLA client side**
The script 'PythonAPI\examples\manual_control.py' is able to perform a client side connection to the server and spawn a car that we are able to control or autopilot and record images from any sensor available.<br>
Decided to modify this script and create 'custom_manual_control.py' in order to be able to record any non RGB sensor simultaneously and the RGB sensor at the same time.<br>
Run the script:
```sh
cd PythonAPI\examples
python custom_manual_control.py
```
Commands:

    W            : throttle
    S            : brake
    A/D          : steer left/right
    Q            : toggle reverse
    Space        : hand-brake
    P            : toggle autopilot
    M            : toggle manual transmission
    ,/.          : gear up/down
    CTRL + W     : toggle constant velocity mode at 60 km/h

    L            : toggle next light type
    SHIFT + L    : toggle high beam
    Z/X          : toggle right/left blinker
    I            : toggle interior light

    TAB          : change sensor position
    ` or N       : next sensor
    [1-9]        : change to sensor [1-9]
    G            : toggle radar visualization
    C            : change weather (Shift+C reverse)
    Backspace    : change vehicle

    O            : open/close all doors of vehicle
    T            : toggle vehicle's telemetry

    V            : Select next map layer (Shift+V reverse)
    B            : Load current selected map layer (Shift+B to unload)

    R            : toggle recording images to disk

    CTRL + R     : toggle recording of simulation (replacing any previous)
    CTRL + P     : start replaying last recorded simulation
    CTRL + +     : increments the start time of the replay by 1 second (+SHIFT = 10 seconds)
    CTRL + -     : decrements the start time of the replay by 1 second (+SHIFT = 10 seconds)

    F1           : toggle HUD
    H/?          : toggle help
    ESC          : quit

When images are recorded from the 'custom_manual_control.py' will be saved on these predifened directories:

| Sensor | Directory |
| ------ | ------ |
| Camera RGB | 'RGB_out/' |
| Camera Depth (Raw) | 'Depth_Raw_out/'' |
| Camera Depth (Gray Scale) | 'Depth_Gray_out/' |
| Camera Depth (Logarithmic Gray Scale) | 'Depth_LogGray_out/' |
| Camera Semantic Segmentation (Raw) | 'SS_Raw_out/' |
| Camera Semantic Segmentation (CityScapes Palette) | 'SS_CityScapes_out/' |
| Camera Instance Segmentation (CityScapes Palette) | 'IS_CityScapes_out/' |
| Camera Instance Segmentation (Raw) | 'IS_Raw_out/' |
| Lidar (Ray-Cast) | 'LiDAR_out/' |
| 'Dynamic Vision Sensor' | 'Dynamic_Sensor_out/' |
| Camera RGB Distorted | 'RGB_Distorted_out/' |
| 'Optical Flow | 'OpticalFlow_out/' |

**Important Notes**
<br>
When recording is advisable to run the client script with the --sync argument, in this way the client runs synchronously with the server, having the same tickrate will help the multiple sensors capture images the same frames (most of the times).
Having the problem of two sensors recording images from different frames may invalidate the data to be used for deep learning purposes, so to solve this issue was added the behaviour that will look at both the RGB and Semantic Segmentation (CityScapes Palette) directories (by default), try find any image frame that exist only in one of them, if exists will be deleted and is triggered when the recorded is stopped during the driving simulation. If by any reason the driving simulation or the server closes during the recording of images frames, the script 'clean_saved_images.py' can be executed and will perform the same verification on two different sensor images save drectories.
