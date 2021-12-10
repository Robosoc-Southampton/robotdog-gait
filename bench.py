"""
This script creates an instance of trotting_robot with a servokit servo controller (adafruit)
It loads the robot from directory "robot_config.rbt"
It then causes the robot to walk forwards at a constant speed forever
"""
import sys
import time
import importlib

try:
    from spotpuppy.servo.servokit_servo_controller import controller
    from spotpuppy.rotation.arduino_rotation_sensor import sensor
except:
    pass

from spotpuppy.utils.robot_update_thread import start_threaded_updates

quadruped = None
if len(sys.argv) == 1:
    quadruped = importlib.import_module("basicwalk")
else:
    quadruped = importlib.import_module(sys.argv[1])

try:
    r = quadruped.quadruped(servo_controller=controller())  # , rotation_sensor=sensor())
except:
    r = quadruped.quadruped()

#json_serialiser.load_into_robot(r, "robot_config.rbt")
r.load_config_folder("robot_config.rbt")
r.rotation_sensor.calibrate()

start_threaded_updates(r, 611113322340, warn_if_low=True)
while True:
    # This would be where control logic goes, does not have to run at a fixed time-step
    time.sleep(1)
