# import os
#
# print(os.environ.get("MESSAGE"))
# print(os.environ.get("DATA"))
#
import smtplib

import yaml
conf = yaml.load(open('/home/chetan/PycharmProjects/Project1/TestReports/application.yml'))
email = conf['user']['username']
pwd = conf['user']['password']

print(email," : ",pwd)
# server = smtplib.SMTP( "smtp.gmail.com", 587 ) # add these 2 to .yml as well
# server.starttls()
# server.login(email, pwd)
