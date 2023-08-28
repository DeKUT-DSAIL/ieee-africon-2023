### Camera Traps

### Introduction
A camera trap is a remotely activated camera that is equipped with a motion sensor, an infrared sensor, or uses a light beam as a trigger.

Camera traps are used for wildlife photography, surveillance, and ecological research.

In this tutorial, we'll show you how to set up a camera trap using a Raspberry Pi, Pi Camera, or USB webcam and Python.

We'll cover the following topics:
1. Setting up your Raspberry Pi
2. Connecting your camera
3. Installing necessary libraries
4. Writing a Python script to capture images or videos
5. Automating the process using Python, bash scripts and crontab


#### Pre-requisites
Before starting this tutorial, you will need the following:
- A Raspberry Pi (any model with a 40-pin GPIO header)
- A Pi camera or USB webcam
- A microSD card with the Raspbian operating system installed
- Access to the Raspberry Pi via SSH or its desktop interface

#### Step 1: Set up your Raspberry Pi
Make sure your Raspberry Pi is set up and running. You will need to have the Raspbian operating system installed and be able to connect to your Raspberry Pi via SSH or have access to its desktop interface.

To be able to SSH to the Raspberry Pi you will need to install the following:
1. Putty Terminal
2. VNC Viewer

If you're new to using a Raspberry Pi, you can follow [this guide](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up) to get started.


#### Step 2: Connect your camera

Connect your Pi Camera or USB webcam to your Raspberry Pi. Make sure the camera is enabled in the Raspberry Pi configuration settings.

If you're using a Pi Camera, you can follow [this guide](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera) to connect it to your Raspberry Pi and enable it in the configuration settings.

If you're using a USB webcam, simply plug it into one of the USB ports on your Raspberry Pi.


## Step 3: Install necessary libraries

You'll need to install the `picamera` library if you're using a Pi camera or the `fswebcam` library if you're using a USB webcam. You can do this by running the following commands in the terminal:

- For Pi Camera: `sudo apt-get update && sudo apt-get install python-picamera python3-picamera`
- For USB webcam: `sudo apt-get update && sudo apt-get install fswebcam`

## Step 4: Write a Python script

Next, you'll need to write a Python script to capture images or videos using the `picamera` or `fswebcam` library.

Here's an example Python script that uses the `picamera` library to capture an image using a Pi Camera and save it with a timestamped filename:


```python
from picamera import PiCamera
from time import sleep
from datetime import datetime

camera = PiCamera()

# Camera warm-up time
sleep(2)

# Capture an image and save it with a timestamped filename
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
filename = f'picamera_image_{timestamp}.jpg'
camera.capture(filename)

If you're using a USB webcam, you can use the `fswebcam` library to capture an image instead. Here's an example Python script that uses `fswebcam` to do this:

```python
import os
from datetime import datetime

# Capture an image and save it with a timestamped filename
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
filename = f'webcam_image_{timestamp}.jpg'
os.system(f'fswebcam -r 640x480 --no-banner {filename}')
```

## Step 5: Automate the process

To automate the process of capturing multiple images or videos, you can use Python, Bash scripts, and crontab.

For example, you can write a Python script that captures an image every 5 minutes and saves it with a timestamped filename. Then, you can use a Bash script to run this Python script at regular intervals using crontab.

Here's an example Bash script that runs the above Python script every 5 minutes to capture an image using a Pi Camera:

```bash
#!/bin/bash

# Change to the directory where the Python script is located
cd /home/pi/camera_trap

# Run the Python script to capture an image
python3 capture_image.py

```

Make sure to make this script executable by running `chmod +x /path/to/script.sh`. Then, you can use crontab to run this script at regular intervals. For example, to run the script every hour, you can add the following line to your crontab:

```
0 * * * * /path/to/script.sh




