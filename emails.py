#!/usr/bin/env python3
from email.message import EmailMessage
import mimetypes
import smtplib
import os
def generate_email(sender,recipient,subject,body,attachment_path):
  msg = EmailMessage()
  msg['From'] = sender
  msg['To'] = recipient
  msg['Subject'] = subject
  msg.set_content(body)
  if not attachment_path == '':
      attachment_file = os.path.basename(attachment_path)
      mime_type,_ = mimetypes.guess_type(attachment_path)
      mime_type,mime_subtype = mime_type.split('/',1)
      with open(attachment_path,'rb') as ap:
        msg.add_attachment(ap.read(), maintype = mime_type, subtype = mime_subtype, filename = attachment_file)
  return msg
def send_mail(msg):
  mail_server = smtplib.SMTP('localhost')
  mail_server.send_message(msg)
  mail_server.quit()
  
