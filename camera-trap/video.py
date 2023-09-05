from picamera2.encoders import  H264Encoder
from picamera2 import Picamera2, Preview
import time

video = Picamera2()

video_config = video.create_video_configuration(main={"size":(1920, 1080)}, lores={"size":(640,480)}, display="lores")

video.configure(video_config)
encoder = H264Encoder(bitrate=10000000)

output = '/home/pi/Desktop/video.h264'
video.start_preview()
video.start_recording(encoder, output)
time.sleep(10)
video.stop_recording()
video.stop_preview()

