import setup_path
import airsim
import cv2
import numpy as np
import os
import time
import tempfile

# connect to the AirSim simulator
client = airsim.CarClient()
client.confirmConnection()
client.enableApiControl(True)
print("API Control enabled: %s" % client.isApiControlEnabled())
car_controls = airsim.CarControls()

tmp_dir = os.path.join(tempfile.gettempdir(), "airsim_car")
print ("Saving images to %s" % tmp_dir)
try:
    os.makedirs(tmp_dir)
except OSError:
    if not os.path.isdir(tmp_dir):
        raise

client.startRecording()

for idx in range(3):
    # get state of the car
    car_state = client.getCarState()
    print("Speed %d, Gear %d" % (car_state.speed, car_state.gear))

    # go forward
    car_controls.throttle = 50
    car_controls.steering = 1
    car_controls.manual_gear = 1
    client.setCarControls(car_controls)

    print("Speed %d, Gear %d" % (car_state.speed, car_state.gear))
    time.sleep(10)   # let car drive a bit

    car_controls.throttle = 50
    car_controls.steering = 1
    car_controls.manual_gear = 2
    client.setCarControls(car_controls)

    print("Speed %d, Gear %d" % (car_state.speed, car_state.gear))
    
    time.sleep(10)   # let car drive a bit

    car_controls.throttle = 50
    car_controls.steering = 1
    car_controls.manual_gear = 3
    client.setCarControls(car_controls)

    print("Speed %d, Gear %d" % (car_state.speed, car_state.gear))
    time.sleep(10)   # let car drive a bit
    
    car_controls.throttle = 50
    car_controls.steering = 1
    car_controls.manual_gear = 4
    client.setCarControls(car_controls)

    print("Speed %d, Gear %d" % (car_state.speed, car_state.gear))

    time.sleep(10)   # let car drive a bit

client.stopRecording()

client.reset()

client.enableApiControl(False)
