#!/usr/bin/env python3
import os
from PIL import Image
new_dir = '/opt/icons'
for files in os.listdir("images"):
  new_filename = os.path.splitext(files)[0]
  try:
    with Image.open(files).convert('RGB') as im:
      im.rotate(270).resize((128,128)).save(new_dir +'/'+ new_filename, format = 'jpeg')
  except OSError:
    pass
