#!/usr/bin/env python3
import requests
import os
path = '/supplier-data/images'
url = 'https://localhost/upload/'
for files in os.listdir(path):
  if files as '.jpeg':
    with open(path+'/'+files,'rb') as opened:
      r = requests.post(url,files={'file':opened})
