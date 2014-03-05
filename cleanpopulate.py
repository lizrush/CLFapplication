#!/usr/bin/env python

#Note this script must be run after running on the database:
#(i) Drop database SQL
#(ii) Create database SQL
#(iii) python manage.py syncdb

#Note that syncdb ONLY adds new tables. Does not modify existing tables. SQLclear command isn't doing it either.

import os
from django.contrib.auth.models import User
from clfapplication.models import Applicant, Recommender, Evaluator, Recommendation, Evaluation, Staff
import csv


#Add cities
ifile = open('clfsampledata.csv', "rb")
reader = csv.reader(ifile)
for row in reader:
	u = User.objects.create_user(username = row[3], password = row[4],email = row[3])
	u.save()
	u = User.objects.get(email = row[3])
	u.first_name = row[1]
	u.last_name = row[2]
	role = int(row[0])
	if role==1:
		a = Applicant(user = u, role = 1)
		a.save()
	if role==2:
		r = Recommender(user = u, role =2)
		r.title = row[5]
		r.organization = row[6]
		r.save()
	if role==3:
		e = Evaluator(user = u, role =3)
		e.save()
	if role==4:
		s = Staff(user = u, role = 4, title ="")
		s.save()
	u.save()
