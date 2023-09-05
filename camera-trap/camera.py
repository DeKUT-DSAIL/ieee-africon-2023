from picamera2 import Picamera, Preview
import time

camera = Picamera()
#camera.rotation = 180

camera_config = camera.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
camera.configure(camera_config)

camera.start_preview()
camera.start()
time.sleep(2)
camera.capture_file('/home/pi/Desktop/image-py.jpg') 
camera.stop_preview()