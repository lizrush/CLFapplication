#!/usr/bin/env python

#Note this script must be run after running on the database:
#(i) Drop database SQL
#(ii) Create database SQL
#(iii) python manage.py syncdb

#Note that syncdb ONLY adds new tables. Does not modify existing tables. SQLclear command isn't doing it either.

import os
from clfapplication.models import User, Recommendation, Evaluation
import csv


#Add cities
ifile = open('clfsampledata.csv', "rb")
reader = csv.reader(ifile)
for row in reader:
	role = int(row[0])
	if row[5]:
		title = row[5]
	else:
		title = ""
	if row[6]:
		organization = row[6]
	else:
		organization=""
	c = User(role=role, firstname = row[1], lastname = row[2], email = row[3], password = row[4], title = title, organization=organization)
	c.save()
