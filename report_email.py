#!/usr/bin/env python3
import os
import requests
import datetime
import reports
def pdf_body(path):
  pdf_content = []
  for files in os.listdir(path):
     with open (path+'/'+files) as f:
        item_name = f.readline().rstrip()
        item_weight = f.readline().rstrip()
     pdf_content.append([item_name,item_weight])
  pdf_body = ''
  for item in pdf_content:
      pdf_body += 'name:'+item[0]+'<br />'+'weight:'+item[1]+'<br />'+'<br />'
  return pdf_body
if __name__ == '__main__':
  path = 'supplier-data/descriptions'
  paragraph = pdf_body(path)
  current_date = datetime.date.today().strftime("%B %d, %Y")
  attachment = '/tmp/processed.pdf'
  title = 'Process Updated on '+ str(current_date)
  pdf = reports.generate_report(attachment, title, paragraph)
