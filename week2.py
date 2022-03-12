#!/usr/bin/env python3
import os
import requests
dict = {}
path = "/data/feedback"
for files in os.listdir(path):
  with open(path+'/'+files) as txt_file:
   dict['title'] = txt_file.readline().rstrip()
   dict['name'] = txt_file.readline().rstrip()
   dict['date'] = txt_file.readline().rstrip()
   dict['feedback'] = txt_file.readline().rstrip()
  response = requests.post("http://35.202.30.75/feedback/",json=dict)
  if response.status_code == 201:
    print("Post to site successful for : ",dict["title"])
  else:
    print("Error while posting : " + dict['title'] + ", error code : " + str(response.status_code))
