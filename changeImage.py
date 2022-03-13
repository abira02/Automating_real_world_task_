#!/usr/bin/env python3
import os
from PIL import Image
path = '/supplier-data/images'
for files in os.listdir(path):
  try:
     with Image.open(path+'/'+files).convert('RGB') as im:
        new_filename = files.split('.')[0]
        im.resize((600,400)).save(path+'/'+new_filename+'.jpeg')
  except OSError:
    pass
    
