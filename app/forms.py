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

class CreateProfileForm(Form):
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
	permanentaddress = TextField('address', validators = [Required(message="We need your address!")])
	permanentcity = TextField('city', validators = [Required(message="We'd like to know what city you live in.")])
	permanentstate = TextField('state', validators = [Required(message="We'd like to know what state you live in.")])
	permanentzipcode = IntegerField('zipcode', validators = [Required(message="We need your zipcode!")])


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

class ShortanswerForm(Form):
	Q01 = TextAreaField('Q01', validators = [Required(message="1")])
	Q02 = TextAreaField('Q02', validators = [Required(message="2")])
	Q03 = TextAreaField('Q03', validators = [Required(message="3")])
	Q04 = TextAreaField('Q04', validators = [Required(message="4")])
	Q05 = TextAreaField('Q05', validators = [Required(message="5")])
	Q06 = TextAreaField('Q06', validators = [Required(message="6")])
	Q07 = TextAreaField('Q07', validators = [Required(message="7")])
	Q08 = TextAreaField('Q08', validators = [Required(message="8")])
	Q09 = TextAreaField('Q09', validators = [Required(message="9")])
	Q10 = TextAreaField('Q10', validators = [Required(message="10")])
	Q11 = TextAreaField('Q11', validators = [Required(message="11")])
	Q12 = TextAreaField('Q12', validators = [Required(message="12")])

class TechskillsForm(Form):
	basicq1 = RadioField('basicq1', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Required()])
	basicq2 = RadioField('basicq2', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Required()])
	basicq3 = RadioField('basicq3', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Required()])
	basicq4 = RadioField('basicq4', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Required()])
	basicq5 = RadioField('basicq5', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Required()])
	basicq6 = RadioField('basicq6', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Required()])
	basicq7 = RadioField('basicq7', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Required()])
	basicq8 = RadioField('basicq8', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Required()])
	basicq9 = RadioField('basicq9', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Required()])
	systemsq1 = RadioField('systemsq1', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Optional()])
	systemsq2 = RadioField('systemsq2', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Optional()])
	systemsq3 = RadioField('systemsq3', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Optional()])
	codingq1 = RadioField('codingq1', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Optional()])
	codingq2 = RadioField('codingq2', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Optional()])
	codingq3 = RadioField('codingq3', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Optional()])
	codingq4 = RadioField('codingq4', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Optional()])
	codingq5 = RadioField('codingq5', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Optional()])
	codingq6 = RadioField('codingq6', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Optional()])

class RecommendationsForm(Form):
	rec1firstname = TextField('rec1firstname', validators = [Required(message="your first recommender's first name")])
	rec1lastname = TextField('rec1lastname', validators = [Required(message="your first recommender's last name")])
	rec1email = TextField('rec1email', validators = [Required(message="your first recommender's email address"), Email("Hmm, your first recommender's email address doesn't look like an email address.")])
	rec1phone = TextField('rec1phone', validators = [Required(message="your first recommender's phone number")])
	rec1how = TextAreaField('rec1how', validators = [Required(message="how you know your first recommender")])
	rec2firstname = TextField('rec2firstname', validators = [Required(message="your second recommender's first name")])
	rec2lastname = TextField('rec2lastname', validators = [Required(message="your second recommender's last name")])
	rec2email = TextField('rec2email', validators = [Required(message="your second recommender's email address"), Email("Hmm, your second recommender's email address doesn't look like an email address.")])
	rec2phone = TextField('rec2phone', validators = [Required(message="your second recommender's phone number")])
	rec2how = TextAreaField('rec2how', validators = [Required(message="how you know your second recommender")])
	rec3firstname = TextField('rec3firstname', validators = [Required(message="your third recommender's first name")])
	rec3lastname = TextField('rec3lastname', validators = [Required(message="your third recommender's last name")])
	rec3email = TextField('rec3email', validators = [Required(message="your third recommender's phone number")])
	rec3phone = TextField('rec3phone', validators = [Required(message="your third recommender's phone number")])
	rec3how = TextAreaField('rec3how', validators = [Required(message="how you know your third recommender")])

class ChecklistForm(Form):
	check1 =  BooleanField('I understand.', validators=[Required()])
	check2 =  BooleanField('I understand.', validators=[Required()])
	check3 =  BooleanField('I understand.', validators=[Required()])
	check4 =  BooleanField('I understand.', validators=[Required()])
	check5 =  BooleanField('I understand', validators=[Required()])

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
