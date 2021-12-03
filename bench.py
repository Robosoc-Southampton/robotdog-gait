"""
This script creates an instance of trotting_robot with a servokit servo controller (adafruit)
It loads the robot from directory "robot_config.rbt"
It then causes the robot to walk forwards at a constant speed forever
"""

import basicwalk
import time
from spotpuppy.servo.servokit_servo_controller import controller
from spotpuppy.utils import json_serialiser
from spotpuppy.rotation.arduino_rotation_sensor import sensor
from spotpuppy.utils.robot_update_thread import start_threaded_updates

r = basicwalk.quadruped(servo_controller=controller())
json_serialiser.load_into_robot(r, "robot_config.rbt")

r.rotation_sensor.calibrate()

start_threaded_updates(r, 60, warn_if_low=True)
while True:
    # This would be where control logic goes, does not have to run at a fixed timestep
    time.sleep(1)