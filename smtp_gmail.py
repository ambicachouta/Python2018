#!/usr/bin/python
import smtplib
gmail_user = 'onlineucator@gmail.com'
gmail_password = 'Redhat@007'

from_1=gmail_user

to = ['devops.keshav@gmail.com','vinayb9090@gmail.com','tchaitanya.2288@gmail.com','ambica.chouta@gmail.com','patelbrij1786@gmail.com','rajbasha96@gmail.com']

subject = 'Sending Email using GMAIL Mail Server'  
body = 'Hi, \n  This is a Email Test \n Thanks, \nRoot.'

email_text = """\  
From: %s  
To: %s  
Subject: %s

%s
""" % (from_1, ", ".join(to), subject, body)

try:  
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(from_1, to, email_text)
    server.close()
    print ('Email sent!')
except:  
    print ('Something went wrong...')





