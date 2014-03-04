from django import forms
from django.forms import CharField, Form, PasswordInput, IntegerField, ChoiceField, BooleanField, FileField, Textarea, RadioSelect, EmailField
from django.contrib.auth.models import User
from clfapplication.models import User, Recommendation, Evaluation


def unique_user(form, field):
     users = User.query.filter_by(email=field.data)
     if users and users.count() > 0:
         raise ValidationError('The email address you provided is already in use.')


class ProfileForm(Form):
	firstname = CharField(required=True)
	firstname2 = CharField()
	middlename = CharField()
	lastname = CharField(required=True)
	lastname2 = CharField()
	email = CharField(required=True)
	password = CharField(widget=PasswordInput(), required=True)
	retypepassword = CharField(widget=PasswordInput(), required=True)
	phone = CharField(required=True)
	phonetype = ChoiceField(choices = (('Home','Home'),('Mobile','Mobile')),required=True)
	address = CharField(required=True)
	city = CharField(required=True)
	state = CharField(required=True)
	zipcode = IntegerField(required=True)
	permanentaddress = CharField(required=True)
	permanentcity = CharField(required=True)
	permanentstate = CharField(required=True)
	permanentzipcode = IntegerField(required=True)


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

class BackgroundForm(Form):
	ged = ChoiceField(choices=(('1', 'No'),('2', 'Yes')), required=True)
	highschoolname = CharField(required=True)
	highschoolcity = CharField(required=True)
	highschoolstate =CharField(required=True)
	highschoolyear =CharField(required=True)
	currentcollegename =CharField()
	currentcollegecity = CharField()
	currentcollegestate = CharField()
	currentcollegetype = ChoiceField(choices=(('1', 'Community College'),('2', 'Four-year College'), ('3', 'Graduate School'), ('4', 'Professional/Technical')))
	communitycollegelevel = ChoiceField(choices=(('1', 'Freshman'),('2', 'Sophomore'),('3', '3rd year or more')))
	traditionalcollegelevel = ChoiceField(choices=(('1', 'Freshman'),('2', 'Sophomore'),('3', 'Junior'),('4','Senior'),('5','Graduating Senior')))
	gradlevel = ChoiceField(choices=(('1', 'Coursework'),('2', 'Internship'),('3', 'Thesis'),('4','Dissertation')))
	techproflevel = ChoiceField(choices=(('1', 'Coursework/Thesis/Internship'),('2', 'Dissertation'),('3', 'Other')))
	major = CharField()
	gpa = CharField()
	studentid = CharField()


class DemographicForm(Form):
	financialaid = ChoiceField(choices=(('1', 'No'),('2', 'Yes')), required=True)
	financialaidreason = CharField()
	financialaward  = ChoiceField(choices=(('1', 'No'),('2', 'Yes')), required=True)
	financialawardlist = CharField()
	economicallydisadvantaged = ChoiceField(choices=(('1', 'No'),('2', 'Yes')), required=True)
	income = ChoiceField(choices=(('1', '$15,000 or under'),('2', '$15,001 - $25,000'), ('3', '$25,001 - $35,000'), ('4','35,001 - $55,000'), ('5', '$55,001 - $75,000'), ('6', '$75,001 - $95,000'), ('7', '$95,001 - $125,000'), ('8', '$125,001 - $160,000'), ('9', '$160,001 and above')), required=True)
	headofhousehold =  ChoiceField(choices=(('1', 'No'),('2', 'Yes')), required=True)
	dependents = IntegerField()
	parent = ChoiceField(choices=(('1', 'No'),('2', 'Yes')), required=True)
	children = IntegerField()
	immigrant = ChoiceField(choices=(('1', 'No'),('2', 'Yes')), required=True)
	immigrationcountry = CharField()
	immigrationdate = CharField()
	motherimmigrant =ChoiceField(choices=(('1', 'No'),('2', 'Yes')), required=True)
	motherimmigrationcountry = CharField()
	motherimmigrationdate = CharField()
	mothereducation = CharField()
	fatherimmigrant = ChoiceField(choices=(('1', 'No'),('2', 'Yes')), required=True)
	fatherimmigrationcountry = CharField()
	fatherimmigrationdate = CharField()
	fathereducation = CharField()
	ab540 = ChoiceField(choices=(('1', 'No'),('2', 'Yes')), required=True)
	firstgencollege = ChoiceField(choices=(('1', 'No'),('2', 'Yes')), required=True)
	primaryhomelanguage = CharField()


class ScholarshipForm(Form):
	awardcycle = CharField(required=True)
	referral = CharField()
   	plannedcollegename =CharField(required=True)
   	plannedcollegecity = CharField(required=True)
   	plannedcollegestate = CharField(required=True)
   	plannedcollegetype = ChoiceField(choices=(('1', 'Community College'),('2', 'Four-year College'),('3', 'Graduate School'), ('4', 'Professional/Technical')))
	plannedcommunitycollegelevel = ChoiceField(choices=(('1', 'Freshman'),('2', 'Sophomore'),('3', '3rd year or more')))
	plannedtraditionalcollegelevel = ChoiceField(choices=(('1', 'Freshman'),('2', 'Sophomore'),('3', 'Junior'),('4','Senior'),('5','Graduating Senior')))
	plannedmajor = CharField(required=True)
	pastrecipient = ChoiceField(choices=(('1', 'No'),('2', 'Yes')), required=True)
	receivingyear = CharField()


class DocumentsForm(Form):
	student_mailing = BooleanField()
	student_emailing = BooleanField()
	college_sending = BooleanField()
	cv_or_resume = FileField()


class EssayForm(Form):
	essay1 = CharField()
	essay2 = CharField()


class RecommendationsForm(Form):
	ref1firstname = CharField(required=True)
	ref1lastname = CharField(required=True)
	ref1email = CharField(required=True)
	ref2firstname = CharField(required=True)
	ref2lastname = CharField(required=True)
	ref2email = CharField(required=True)


class RecommenderForm(Form):
	KnownApplicant = CharField(required=True)
	Capacity = CharField(required=True)
	OtherCapacity = CharField(required=True)
	Recommendation = CharField(widget=Textarea(), required=True)
	refCertify =  BooleanField(required=True)
	Criteria1Rating = ChoiceField(widget=RadioSelect, choices=(('1','1'),('2','2'),('3','3'),('4','4'),('5','5')), required=True)
	Criteria1Comment = CharField(widget=Textarea(), required=True)
	Criteria2Rating = ChoiceField(widget=RadioSelect, choices=(('1','1'),('2','2'),('3','3'),('4','4'),('5','5')), required=True)
	Criteria2Comment = CharField(widget=Textarea(), required=True)
	Criteria3Rating = ChoiceField(widget=RadioSelect, choices=(('1','1'),('2','2'),('3','3'),('4','4'),('5','5')), required=True)
	Criteria3Comment = CharField(widget=Textarea(), required=True)
	Criteria4Rating = ChoiceField(widget=RadioSelect, choices=(('1','1'),('2','2'),('3','3'),('4','4'),('5','5')), required=True)
	Criteria4Comment = CharField(widget=Textarea(), required=True)
	Criteria5Rating = ChoiceField(widget=RadioSelect, choices=(('1','1'),('2','2'),('3','3'),('4','4'),('5','5')), required=True)
	Criteria5Comment = CharField(widget=Textarea(), required=True)
	Criteria6Rating = ChoiceField(widget=RadioSelect, choices=(('1','1'),('2','2'),('3','3'),('4','4'),('5','5')), required=True)
	Criteria6Comment = CharField(widget=Textarea(), required=True)
	Criteria7Rating = ChoiceField(widget=RadioSelect, choices=(('1','1'),('2','2'),('3','3'),('4','4'),('5','5')), required=True)
	Criteria7Comment = CharField(widget=Textarea(), required=True)
	OverallRating = ChoiceField(widget=RadioSelect, choices=(('1','1'),('2','2'),('3','3'),('4','4'),('5','5')), required=True)
	OverallComment = CharField(widget=Textarea(), required=True)


class EvaluatorForm(Form):
	rating = ChoiceField(choices=((None, ''),('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')), required = True)
	notes = CharField(widget=Textarea())


class ChangeRecommenderContact(Form):
	email = EmailField(required=True)


class ForgotPasswordForm(Form):
	email = EmailField(required=True)
	def validate_email(self, field):
		user = self.get_user()
		if not user:
			raise ValidationError("A user account does not exist for that email address.")
	def get_user(self):
		return User.query.filter_by(email=self.email.data).first()


class ResetPasswordForm(Form):
	password = CharField(widget=PasswordInput(), required=True)
	password_confirmation = CharField(widget=PasswordInput(), required=True)
	token = CharField()
	def validate_password(self, field):
		if self.password.data == '':
			raise ValidationError("Please enter a password")
		if self.password.data != self.password_confirmation.data:
			raise ValidationError("Your passwords don't match - try retyping them.")
		if len(self.password.data) < 8:
			raise ValidationError("Your password is a little short - pick one that's at least 8 characters long.")
