import os
from datetime import datetime

# Capture an image and save it with a timestamped filename
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
filename = f'webcam_image_{timestamp}.jpg'
os.system(f'fswebcam -r 1280x720 --no-banner {filename}')