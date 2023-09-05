from picamera2 import Picamera2
import time

camera = Picamera2()
#camera.rotation = 180
#several images at once
camera_config = camera.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
camera.configure(camera_config)

camera.start_preview()
camera.start()
for i in range(5):
    time.sleep(5)
    camera.capture('/home/pi/Desktop/image%s.jpg' % i)
camera.stop_preview()