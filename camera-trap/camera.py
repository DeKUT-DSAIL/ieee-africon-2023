from picamera2 import Picamera2, Preview
import time
from datetime import datetime

camera = Picamera2()
#camera.rotation = 180
#Camera warm-up time
time.sleep(2)

timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
filename = f'{timestamp}.jpg'
camera_config = camera.create_still_configuration(main={"size": (1920, 1080)}, lores={"size>camera.configure(camera_config)

camera.start_preview()
camera.start()
camera.capture_file('/home/pi/Desktop/'+filename)
camera.stop_preview()
