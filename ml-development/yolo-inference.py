#file and folder libraries
#!pip install pandas
import pandas as pd
import numpy as np

#!pip install torchvision
import os
from datetime import datetime

#Mapping libraries
#!pip install geopandas
#import geopandas as gpd
#!pip install pyshape
#from shapely.geometry import Point, Polygon

#Import specific function 'from_epsg' from fiona module
#from fiona.crs import from_epsg

#pytorch related
#!pip install torch
#!pip install matplotlib
#!pip install opencv-python
import torch
import matplotlib.pyplot as plt
import cv2


def detect_and_verify(source):
    img = (source)#('dataset/images/a.jpg')
    results = model(img)
    print(results)

    #%matplotlib inline 
    plt.imshow(np.squeeze(results.render()))
    plt.show()
    
def detect_class(source):
    '''
    returns filename, impala_count, zebra_count, other_count
    '''
    img = (source)
    results = model(img)
    print(results)
    #%matplotlib inline 
    plt.imshow(np.squeeze(results.render()))
    plt.show()

    r = str(results).split()
    impala_count = 0
    zebra_count = 0
    other_count = 0
    if 'impala' in r or 'impala,' in r:
        impala_count = 1
    if 'impalas' in r:
        index = r.index('impalas')
        impala_count = r[index-1]
    if 'impalas,' in r:
        index = r.index('impalas,')
        impala_count = r[index-1]
    if 'zebra' in r or 'zebra,' in r :
        zebra_count = 1
    if 'zebras' in r:
        index = r.index('zebras')
        zebra_count = r[index-1]
    if 'zebras,' in r:
        index = r.index('zebras,')
        zebra_count = r[index-1]
    if 'other' in r or 'other,' in r :
        other_count = 1
    if 'others' in r:
        index = r.index('others')
        other_count = r[index-1]
    if 'others,' in r:
        index = r.index('others,')
        other_count = r[index-1]

    return source, impala_count, zebra_count, other_count

#this is a open source pretrained model
#!git clone https://github.com/ultralytics/yolov5

#load animal detection model
model = torch.hub.load('ultralytics/yolov5', 'custom', path=r'models/lasst.pt',verbose=False)
print('Detection model has loaded')

#Set the confidence which you require from the model
model.conf = 0.45

detect_and_verify('dataset/images/impala.jpg')
detect_and_verify(r'dataset\images\tortoise.jpg')
detect_and_verify('dataset/images/waterbuck.jpg')
detect_and_verify('dataset/images/impalas-warthogs.jpg')
detect_and_verify('dataset/images/DSC_0007.JPG')

#on multiple images
start = datetime.now()
#400 images with impalas or zebras
df_auto = pd.DataFrame()
Species = []
source = './dataset/data/processing/'
Filenames = os.listdir(source)
files = []
impalas = []
zebras = []
others = []

for image in Filenames[:]:
    try:
        _,b,c,d = detect_class(source+image)
        files.append(image)
        impalas.append(b)
        zebras.append(c)
        others.append(d)
        print(image,'  ',b,' Impalas ',c,' Zebras ',d,' Others\n')
    except:
        pass
df_auto['Filename'] = files
df_auto['Impala_count'] = impalas
df_auto['Zebra_count'] = zebras
df_auto['Other_count'] = others
end = datetime.now()
print('Timetaken : ',end-start,' HH:MM:SS')
print('Files processed',df_auto.shape[0])
df_auto.head(25)

df_sightings = pd.DataFrame()
df = pd.read_excel('dataset/camera_trap_dataset_annotation.xlsx')
file_longitude = {}
file_latitude = {}
for i, row in df.iterrows():
    file_latitude[row['Filename']] = row['Latitude']
    file_longitude[row['Filename']] = row['Longitude']

#add location
longs = []
lats = []
for i, row in df_auto.iterrows():
    lats.append(file_latitude[row['Filename']])
    longs.append(file_longitude[row['Filename']])
df_auto['Latitude'] = lats 
df_auto['Longitude'] = longs

#Lets look at our data before we save it
df_auto.head()

df_auto.to_csv('csvs/dekut_animal_counts.csv',index=False)