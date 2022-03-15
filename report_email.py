#!/usr/bin/env python3
import os
import requests
import datetime
import reports
from emails import generate_email,send_email
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
  sender = 'automation@example.com'
  recipient = 'username@example.com'
  subject = 'Upload Completed - Online Fruit Store'
  body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
  attachment_path = '/tmp/processed.pdf'
  email = generate_email(sender,recipient,subject,body,attachment_path)
  send_email(email)
