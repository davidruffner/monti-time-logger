#!/usr/bin/python
# Adapted from https://gist.github.com/dbieber/5146518
# Adapted from http://kutuma.blogspot.com/2007/08/sending-emails-via-gmail-with-python.html

import getpass
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os
import time
import ruamel.yaml as yaml

def getCredentials():
   """
   Gets credentials of email server account and the information 
   of the user (form and phoneAddress)
   """
   
   # Get user name and password of email account to send messages
   with open('gmailInfo.yml', 'r') as f:
      gmailInfo = yaml.load(f)
   
   global gmail_user, gmail_pwd
   gmail_user = gmailInfo['gmail_user']
   gmail_pwd = gmailInfo['gmail_pwd']

   # Load user information (quiz link, and phone address)
   with open('userInfo.yml', 'r') as f:
      userInfo = yaml.load(f)

   global quizLink, phoneAddress
   quizLink = userInfo['quizLink']
   phoneAddress = userInfo['phoneAddress']

def login(user):
   global gmail_user, gmail_pwd
   gmail_user = user
   gmail_pwd = getpass.getpass('Password for %s: ' % gmail_user)

def mail(to, subject, text, attach=None):
   """
   Sends email using gmail. Requires a username and password of the server account as globals.
   """
   msg = MIMEMultipart()
   msg['From'] = gmail_user
   msg['To'] = to
   msg['Subject'] = subject
   msg.attach(MIMEText(text))
   if attach:
      part = MIMEBase('application', 'octet-stream')
      part.set_payload(open(attach, 'rb').read())
      Encoders.encode_base64(part)
      part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
      msg.attach(part)
   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(gmail_user, gmail_pwd)
   mailServer.sendmail(gmail_user, to, msg.as_string())
   mailServer.close()

def sendForm():
   """ Send an email as a text message with a link to the google form"""
   # Record the local time
   localtime = time.localtime()
   hour = localtime.tm_hour
   minute = localtime.tm_min
   
   # Create the quiz link with the local time
   # If the quiz link is any longer then it won't fit into a single text
   # message and will be broken
   quizLinkUpdated = quizLink.format(hour, minute)

   
   # Send it to phone in a text
   mail(phoneAddress, '', quizLinkUpdated)
   print 'Sent message!', quizLinkUpdated

if __name__ == '__main__':
   getCredentials()
   sendForm()
