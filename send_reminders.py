#!/usr/bin/env python3

import csv
import datetime
import email
import smtplib
import sys


def usage():
  print("send_reminders: Send meeting reminders")
  print()
  print("invacation:")
  print("    send_reminders 'date|Meeting Title|emails' ")
  return 1

def dow(date):
  dateobj = datetime.datetime.strptime(date, r"%Y-%m-%d")
  return dateobj.strftime("%A")

def message_template(date, title, name):
  message = email.message.EmailMessage()
  weekday = dow(date)
  message['Subject'] = f'Meeting reminder: "{title}"'
  message.set_content(f'''
Hi {name}!

This is a quick mail to remind you all that we have a meeting about:
 "{title}"
the {weekday} {date}.

See you there.
''')
 
#Create a dictionary from reading the csvfile
  def read_names(contacts):
    name = {}
    with open(contacts) as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
        if row in reader:
          names[row[1]] = row[1]
    return names
  
  def send_message(date, title, emails, contacts):
    smtp = smtplib.SMPT('localhost')
    names = read_names(contacts)#call it before the for loop so that it only reads it once
    for email in emails.split(','):
      name = names[email]
      message = message_template(date, title, name)
      message['From'] = 'noreply@example.com'
      message['To'] = email
      smtp.send_message(message)
    smtp.quit()
    pass
  
  
  
  
  
  
