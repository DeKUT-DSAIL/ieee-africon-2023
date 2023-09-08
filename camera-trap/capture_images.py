from picamera2 import Picamera2
import time
from datetime import datetime

camera = Picamera2()
#camera.rotation = 180


#several images at once
camera_config = camera.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
camera.configure(camera_config)

camera.start_preview()
camera.start()
for i in range(5):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'{timestamp}.jpg'
    time.sleep(2)
    camera.capture_file('/home/pi/Desktop/' + filename)
camera.stop_preview()
