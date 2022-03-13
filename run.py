#!/usr/bin/env python3
import os
import requests
import json
path = 'supplier-data/descriptions/'
im_path = 'supplier-data/images'
dict_desc = {}
url = 'http://[linux-instance-external-IP]/fruits'
for files in os.listdir(path):
  with open(path+'/'+files) as f:
    dict_desc['name'] = files.readline().rstrip()
    dict_desc['weight'] = files.readline().rstrip().split()[0]
    dict_desc['description'] = files.readline().rstrip()
    dict_desc['image_name'] = im_path+'/'+files.split('.')+'.jpeg'
  r = requests.post(url,json = dict_desc)
    
    
