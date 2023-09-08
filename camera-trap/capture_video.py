from picamera2.encoders import  H264Encoder
from picamera2 import Picamera2, Preview
import time
from datetime import datetime

video = Picamera2()

timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
filename = f'{timestamp}.h264'

video_config = video.create_video_configuration(main={"size":(1920, 1080)}, lores={"size": (640, 480)}, display="lores")

video.configure(video_config)
encoder = H264Encoder(bitrate=10000000)

output = '/home/pi/Desktop/' + filename
video.start_preview()
video.start_recording(encoder, output)
time.sleep(10)
video.stop_recording()
video.stop_preview()
