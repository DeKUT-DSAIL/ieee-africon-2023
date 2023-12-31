import pandas as pd
import numpy as np
import os
from datetime import datetime
import torch
import matplotlib.pyplot as plt
import cv2

os.makedirs('predictions',exist_ok=True)
path = '/content/ieee-africon-2023/ml-development/dataset/images/'

def make_preds(file):
    results = model(path+file)
    print(results)
    pred = np.squeeze(results.render())
    plt.imsave('predictions/'+file,pred)

#load animal detection model
model = torch.hub.load('yolov5', 'custom', path=r'/content/ieee-africon-2023/ml-development/models/lasst.pt',source='local',force_reload=True)
print('Detection model has loaded')

#Set the confidence which you require from the model
model.conf = 0.45

images = os.listdir(path)
for i in images:
    make_preds(i)