from flask.ext.wtf import Form
from app import db
from models import User, Recommendation
from wtforms import TextField, PasswordField, IntegerField, TextAreaField, RadioField, BooleanField, SelectField
from wtforms.validators import Required, Email, EqualTo, Length, ValidationError, Optional

def unique_user(form, field):
     users = User.query.filter_by(email=field.data)
     if users and users.count() > 0:
         raise ValidationError('The email address you provided is already in use.')

class LoginForm(Form):
	email = TextField('email', validators = [Required(message="We need to know your email address.")])
	password = PasswordField('password', validators = [Required(message="We need your password.")])

	def validate_email(self, field):
		user = self.get_user()
		if user is None:
			raise ValidationError('Invalid User')
		if user.password != self.password.data:
			raise ValidationError('Invalid Password')

	def get_user(self):
		return db.session.query(User).filter_by(email=self.email.data).first()

	def validate_password(self, field):
		user = self.get_user()

		if not user and self.password.data == '':
			raise ValidationError("Please enter a password")

		# hack to prevent overwrite of password with blank on profile update
		if user and (self.password.data == '' or self.password.data == None):
			self.password.data = user.password
			self.retypepassword.data = user.password

		if self.password.data != self.retypepassword.data:
			raise ValidationError("Your passwords don't match - try retyping them.")

		if len(self.password.data) < 8:
			raise ValidationError("Your password is a little short - pick one that's at least 8 characters long.")

	def get_user(self):
		return db.session.query(User).filter_by(email=self.email.data).first()

class ProfileForm(Form):
	firstname = TextField('firstname', validators = [Required(message='We need to know your first name!')])
	firstname2 = TextField('firstname2', validators = none)
	middlename = TextField('middlename', validators = none)
	lastname = TextField('lastname', validators = [Required(message='We need to know your last name!')])
	lastname2 = TextField('lastname', validators = none)
	email = TextField('email', validators = [unique_user, Required(message="We need your email address!"), Email(message="Hmm, your email address doesn't look like an email address.")])
	password = PasswordField('password')
	retypepassword = PasswordField('retypepassword')
	phone = TextField('phone', validators = [Required(message="We need your phone number!")])
	phonetype = SelectField('inspire', choices=[('1', 'Cell'),('2', 'Home'),('3', 'Work')], validators = [Required()])
	address = TextField('address', validators = [Required(message="We need your address!")])
	city = TextField('city', validators = [Required(message="We'd like to know what city you live in.")])
	state = TextField('state', validators = [Required(message="We'd like to know what state you live in.")])
	zipcode = IntegerField('zipcode', validators = [Required(message="We need your zipcode!")])
	permanentaddress = TextField('permanentaddress', validators = [Required(message="We need your permanent address!")])
	permanentcity = TextField('permanentcity', validators = [Required(message="We'd like to know your permanent address city.")])
	permanentstate = TextField('permanentstate', validators = [Required(message="We'd like to know your permanent address state.")])
	permanentzipcode = IntegerField('permanentzipcode', validators = [Required(message="We need your permanent address zipcode!")])



	def validate_password(self, field):
		user = self.get_user()

		if not user and self.password.data == '':
			raise ValidationError("Please enter a password")

		# hack to prevent overwrite of password with blank on profile update
		if user and (self.password.data == '' or self.password.data == None):
			self.password.data = user.password
			self.retypepassword.data = user.password

		if self.password.data != self.retypepassword.data:
			raise ValidationError("Your passwords don't match - try retyping them.")

		if len(self.password.data) < 8:
			raise ValidationError("Your password is a little short - pick one that's at least 8 characters long.")

	def get_user(self):
		return db.session.query(User).filter_by(email=self.email.data).first()

class SchoolForm(Form):
	ged = SelectField('ged', choices=[('1', 'No'),('2', 'Yes')], validators = [Required()])
   	highschoolname = TextField('highschoolname', validators = [Required(message="We'd like to know what high school you attended.")])
    	highschoolcity = TextField('highschoolcity', validators = [Required(message="We'd like to know what city the high school you attended was in.")])
    	highschoolstate =TextField('highschoolstate', validators = [Required(message="We'd like to know what state the high school you attended was in.")])
    	highschoolyear =TextField('highschoolyear', validators = [Required(message="We'd like to know what year you graduated.")])
    	currentcollegename =TextField('currentcollegename')
    	currentcollegecity = TextField('currentcollegecity')
    	currentcollegestate = TextField('currentcollegestate')
    	currentcollegetype = SelectField('currentcollegetype', choices=[('1', 'Community College'),('2', 'Four-year College') ('3', 'Graduate School'), ('4', 'Professional/Technical')])
    	communitycollegelevel = SelectField('communitycollegelevel', choices=[('1', 'Freshman'),('2', 'Sophomore'),('3', '3rd year or more')])
    	traditionalcollegelevel = SelectField('traditionalcollegelevel', choices=[('1', 'Freshman'),('2', 'Sophomore'),('3', 'Junior'),('4','Senior'),('5','Graduating Senior')])
    	gradlevel = SelectField('gradlevel', choices=[('1', 'Coursework'),('2', 'Internship'),('3', 'Thesis'),('4','Dissertation')])
  	techproflevel = SelectField('techproflevel', choices=[('1', 'Coursework/Thesis/Internship'),('2', 'Dissertation'),('3', 'Other'))
    	major = TextField('major')
    	gpa = TextField('gpa')
    	studentid = TextField('studentid')

class ScholarshipForm(Form):
	awardcycle = TextField('awardcycle'), validators = [Required(message="We'd like to know which award cycle you are applying for.")])
	referral = TextField('referral')
    	plannedcollegename =TextField('currentcollegename'), validators = [Required(message="We'd like to know what college you plan to attend.")])
    	plannedcollegecity = TextField('currentcollegecity'), validators = [Required(message="We'd like to know what city the school you plan to attend is in.")])
    	plannedcollegestate = TextField('currentcollegestate'), validators = [Required(message="We'd like to know what state the school you plan to attend is in.")])
    	plannedcollegetype = SelectField('currentcollegetype', choices=[('1', 'Community College'),('2', 'Four-year College') ('3', 'Graduate School'), ('4', 'Professional/Technical')])
    	plannedcommunitycollegelevel = SelectField('communitycollegelevel', choices=[('1', 'Freshman'),('2', 'Sophomore'),('3', '3rd year or more')])
    	plannedtraditionalcollegelevel = SelectField('traditionalcollegelevel', choices=[('1', 'Freshman'),('2', 'Sophomore'),('3', 'Junior'),('4','Senior'),('5','Graduating Senior')])
    	plannedmajor = TextField('plannedmajor'), validators = [Required(message="We'd like to know what you plan to study.")])
	pastrecipient = SelectField('pastrecipient', choices=[('1', 'No'),('2', 'Yes')], validators = [Required()])
	receivingyear = TextField('receivingyear')


class RecommendationsForm(Form):
	ref1name = TextField('ref1name', validators = [Required(message="your first recommender's first name")])
	ref1email = TextField('ref1email', validators = [Required(message="your first recommender's email address"), Email("Hmm, your first recommender's email address doesn't look like an email address.")])
	ref2name = TextField('ref2name', validators = [Required(message="your second recommender's first name")])
	ref2email = TextField('ref2email', validators = [Required(message="your second recommender's email address"), Email("Hmm, your second recommender's email address doesn't look like an email address.")])

class ConfidentialDemographics(Form):
	financialaid = SelectField('financialaid', choices=[('1', 'No'),('2', 'Yes')], validators = [Required()])
	financialaidreason = TextField('financialaidreason')
	financialaward  = SelectField('financialaward', choices=[('1', 'No'),('2', 'Yes')], validators = [Required()])
	financialawardlist = TextField('financialawardlist')
	economicallydisadvantaged = SelectField('economicallydisadvantaged', choices=[('1', 'No'),('2', 'Yes')], validators = [Required()])
	income = SelectField('income', choices=[('1', '$15,000 or under'),('2', '$15,001 - $25,000'), ('3', '$25,001 - $35,000'), ('4','35,001 - $55,000'), ('5', '$55,001 - $75,000'), ('6', '$75,001 - $95,000'), ('7', '$95,001 - $125,000'), ('8', '$125,001 - $160,000'), ('9', '$160,001 and above')], validators = [Required()])
	headofhousehold =  SelectField('headofhousehold', choices=[('1', 'No'),('2', 'Yes')], validators = [Required()])
	dependents = IntegerField('dependents')
	parent = SelectField('parent', choices=[('1', 'No'),('2', 'Yes')], validators = [Required()])
	children = IntegerField('dependents')
	immigrant = SelectField('immigrant', choices=[('1', 'No'),('2', 'Yes')], validators = [Required()])
	immigrationcountry = TextField('immigrationcountry')
	immigrationdate = TextField('immigrationdate')
	motherimmigrant =SelectField('motherimmigrant', choices=[('1', 'No'),('2', 'Yes')], validators = [Required()])
	motherimmigrationcountry = TextField('immigrationdate')
	motherimmigrationdate = TextField('immigrationdate')
	mothereducation = TextField('immigrationdate')
	fatherimmigrant = SelectField('fatherimmigrant', choices=[('1', 'No'),('2', 'Yes')], validators = [Required()])
	fatherimmigrationcountry = TextField('immigrationdate')
	fatherimmigrationdate = TextField('immigrationdate')
	fathereducation = TextField('immigrationdate')
	ab540 = SelectField('ab540', choices=[('1', 'No'),('2', 'Yes')], validators = [Required()])
	firstgencollege = SelectField('firstgencollege', choices=[('1', 'No'),('2', 'Yes')], validators = [Required()])
	primaryhomelanguage = TextField('immigrationdate')

class EssaysForm(Form):
	essaytext1 = db.Column(db.Text)
    	essaytext2 = db.Column(db.Text)


class RecLoginForm(Form):
	email = TextField('email', validators = [Required(message="We need to know your email address.")])
	password = PasswordField('password', validators = [Required(message="We need your password.")])

	def validate_email(self, field):
		recommender = self.get_recommender()
		if recommender is None:
			raise ValidationError('Invalid User')
		if recommender.password != self.password.data:
			raise ValidationError('Invalid Password')

	def get_recommender(self):
		return db.session.query(User).filter_by(email=self.email.data, role = 2).first()

class RecommenderForm(Form):
	recq1 = RadioField('recq1', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Required()])
	recq1ex = TextAreaField('recq1ex', validators = [Required(message="1")])
	recq2 = RadioField('recq2', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Required()])
	recq2ex = TextAreaField('recq2ex', validators = [Required(message="2")])
	recq3 = RadioField('recq3', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Required()])
	recq3ex = TextAreaField('recq3ex', validators = [Required(message="3")])
	recq4 = RadioField('recq4', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Required()])
	recq4ex = TextAreaField('recq4ex', validators = [Required(message="4")])
	recq5 = RadioField('recq5', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Required()])
	recq5ex = TextAreaField('recq5ex', validators = [Required(message="5")])
	recq6 = RadioField('recq6', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Required()])
	recq6ex = TextAreaField('recq6ex', validators = [Required(message="6")])
	recq7 = TextAreaField('recq7', validators = [Required(message="7")])
	recq8 = TextAreaField('recq8', validators = [Required(message="8")])

#new
class ChangeRecommenderContact(Form):
	email = TextField('email', validators = [Required(message="your recommender's email address"), Email("Hmm, this doesn't look like an email address.")])
#new

class ForgotPasswordForm(Form):

	email = TextField('email', validators = [Required(message="your email address"), Email("Hmm, this doesn't look like an email address.")])

	def validate_email(self, field):
		user = self.get_user()

		if not user:
			raise ValidationError("A user account does not exist for that email address.")

	def get_user(self):
		return User.query.filter_by(email=self.email.data).first()

class ResetPasswordForm(Form):
	password = PasswordField('password')
	password_confirmation = PasswordField('password_confirmation')
	token = TextField('token')

	def validate_password(self, field):
		if self.password.data == '':
			raise ValidationError("Please enter a password")

		if self.password.data != self.password_confirmation.data:
			raise ValidationError("Your passwords don't match - try retyping them.")

		if len(self.password.data) < 8:
			raise ValidationError("Your password is a little short - pick one that's at least 8 characters long.")

##### Begin code block for Selector process

class EvalLoginForm(Form):
	email = TextField('email', validators = [Required(message="We need to know your email address.")])
	password = PasswordField('password', validators = [Required(message="We need your password.")])

	def validate_email(self, field):
		evaluator = self.get_evaluator()
		if evaluator is None:
			raise ValidationError("Your email address doesn't appear to be in our system")
		if evaluator.password != self.password.data:
			raise ValidationError("We found your email address, but your password doesn't match")

	def get_evaluator(self):
		return db.session.query(User).filter_by(email=self.email.data, role = 4).first()

class EvaluatorForm(Form):
	critical = SelectField('critical', choices=[(None, ''),('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], validators = [Required()])
	mission = SelectField('mission', choices=[(None, ''),('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], validators = [Required()])
	community = SelectField('community', choices=[(None, ''),('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], validators = [Required()])
	inspire = SelectField('inspire', choices=[(None, ''),('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], validators = [Required()])
	yesno = SelectField('yesno', choices=[(None,''),('No','No'),('Yes','Yes')], validators=[Required()])
	interview = TextAreaField('interview', validators = [Required()])
	additional = TextAreaField('additional')

##### End code block for Selector process
