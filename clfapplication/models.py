from django.db import models
from django.contrib.auth.models import User

# Django has a built-in User model that works well with the out-of-the-box authentication functions, so we are using it/them.
# That model is created via User.objects.create(username, email, password), and can then also hold first_name and last_name.

#Instead of redefining the entire User class to acommodate our variables and then writing security funtions for it (and on and on), we are "extending" the user model with Staff, Evaluator, Recommender, and Applicant models that reference their User base model via a OneToOneField.

#To reference via the extended class, do something like: 
	#olga = User.objects.get(first_name ="Olga")
	#olgastitle = olga.staff.title

class Staff(models.Model):
    user = models.OneToOneField(User)
    role = models.IntegerField()
    first_name2 = models.CharField(max_length=45)
    last_name2 = models.CharField(max_length=45)
    title = models.CharField(max_length=45)

class Evaluator(models.Model):
    user = models.OneToOneField(User)
    role = models.IntegerField()
    firstname2 = models.CharField(max_length=45)
    lastname2 = models.CharField(max_length=45)


class Recommender(models.Model):
    user = models.OneToOneField(User)
    role = models.IntegerField()
    firstname2 = models.CharField(max_length=45)
    lastname2 = models.CharField(max_length=45)
    title = models.CharField(max_length=45)
    organization = models.CharField(max_length=45)


class Applicant(models.Model):
    user = models.OneToOneField(User)
    role = models.IntegerField()
    firstname2 = models.CharField(max_length=45)
    lastname2 = models.CharField(max_length=45)
    phonetype = models.IntegerField(default = 0)
    address = models.CharField(max_length=90)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    zipcode = models.CharField(max_length=10)

    # permanent address
    permanentaddress =models.CharField(max_length=90)
    permanentcity = models.CharField(max_length=45)
    permanentstate = models.CharField(max_length=45)
    permanentzipcode = models.CharField(max_length=10)

    #  school information
    ged = models.IntegerField(default = 0)
    highschoolname = models.CharField(max_length=45)
    highschoolcity = models.CharField(max_length=45)
    highschoolstate = models.CharField(max_length=45)
    highschoolyear = models.CharField(max_length=10)
    currentcollegename = models.CharField(max_length=45)
    currentcollegecity = models.CharField(max_length=45)
    currentcollegestate = models.CharField(max_length=45)
    currentcollegetype = models.IntegerField(default = 0)
    communitycollegelevel = models.IntegerField(default = 0)
    traditionalcollegelevel = models.IntegerField(default = 0)
    gradlevel = models.IntegerField(default = 0)
    techproflevel = models.IntegerField(default = 0)
    major = models.CharField(max_length=45)
    gpa = models.CharField(max_length=45)
    studentid = models.CharField(max_length=45)

    # future school info
    plannedcollegename = models.CharField(max_length=45)
    plannedcollegecity = models.CharField(max_length=45)
    plannedcollegestate = models.CharField(max_length=45)
    plannedcollegetype = models.IntegerField(default = 0)
    plannedcommunitycollegelevel = models.IntegerField(default = 0)
    plannedtraditionalcollegelevel = models.IntegerField(default = 0)
    plannedgradlevel = models.IntegerField(default = 0)
    plannedtechproflevel = models.IntegerField(default = 0)
    plannedmajor = models.CharField(max_length=45)

    pastrecipient = models.IntegerField(default = 0)
    receivingyear = models.CharField(max_length=10)
    referral = models.TextField()
    awardcycle = models.CharField(max_length=10)
    essaytext1 = models.TextField()
    essaytext2 = models.TextField()

    # confidential demographics
    financialaid = models.IntegerField(default = 0)
    financialaidreason = models.CharField(max_length=45)
    financialaward = models.IntegerField(default = 0)
    financialawardlist = models.CharField(max_length=45)
    economicallydisadvantaged = models.IntegerField(default = 0)
    income = models.IntegerField(default = 0)
    headofhousehold = models.IntegerField(default = 0)
    dependents = models.CharField(max_length=45)
    parent = models.IntegerField(default = 0)
    children = models.IntegerField(default = 0)
    immigrant = models.IntegerField(default = 0)
    immigrationcountry = models.CharField(max_length=45)
    immigrationdate = models.CharField(max_length=45)
    motherimmigrant = models.IntegerField(default = 0)
    motherimmigrationcountry = models.CharField(max_length=45)
    motherimmigrationdate = models.CharField(max_length=45)
    mothereducation = models.CharField(max_length=45)
    fatherimmigrant = models.IntegerField(default = 0)
    fatherimmigrationcountry = models.CharField(max_length=45)
    fatherimmigrationdate = models.CharField(max_length=45)
    fathereducation = models.CharField(max_length=45)
    ab540 = models.IntegerField(default = 0)
    firstgencollege = models.IntegerField(default = 0)
    primaryhomelanguage = models.CharField(max_length=45)

    # reference info
    ref1firstname = models.CharField(max_length=45)
    ref1lastname = models.CharField(max_length=45)
    ref1email = models.CharField(max_length=45)
    ref2firstname = models.CharField(max_length=45)
    ref2lastname = models.CharField(max_length=45)
    ref2email = models.CharField(max_length=45)
    timestamp = models.IntegerField(default = 0)

    def __repr__(self):
        return '<User %r>' % (self.email)

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def __unicode__(self):
        return self.email

    def get_id(self):
        return self.id


class Recommendation(models.Model):
	student_id = models.ForeignKey(Applicant)
	recommender_id = models.ForeignKey(User)
	KnownApplicant = models.TextField()
	Capacity = models.TextField()
	OtherCapacity = models.TextField()
	Recommendation = models.TextField()
	refCertify = models.IntegerField()
	Criteria1Rating = models.IntegerField()
	Criteria1Comment = models.TextField()
	Criteria2Rating = models.IntegerField()
	Criteria2Comment = models.TextField()
	Criteria3Rating = models.IntegerField()
	Criteria3Comment = models.TextField()
	Criteria4Rating = models.IntegerField()
	Criteria4Comment = models.TextField()
	Criteria5Rating = models.IntegerField()
	Criteria5Comment = models.TextField()
	Criteria6Rating = models.IntegerField()
	Criteria6Comment = models.TextField()	
	Criteria7Rating = models.IntegerField()
	Criteria7Comment = models.TextField()
	OverallRating = models.IntegerField()
	OverallComment = models.TextField()

	def __unicode__(self):
		return self.id

	def is_recommendation_complete(self):
		if self.Criteria1Rating and self.Criteria1Comment and self.Criteria2Rating and self.Criteria2Comment and self.Criteria3Rating and self.Criteria3Comment and self.Criteria4Rating and self.Criteria4Comment and self.Criteria5Rating and self.Criteria5Comment and self.Criteria6Rating and self.Criteria6Comment and self.Criteria7Rating and self.Criteria7Comment and self.OverallRating and self.OverallComment:
			return True
		return False


class Evaluation(models.Model):
	student_id = models.ForeignKey(Applicant)
	evaluator_id = models.ForeignKey(User)
	rating = models.IntegerField()
	notes = models.TextField()

	def is_evaluation_complete(self):
		if rating:
			return True
		return False

        def __unicode__(self):
                return self.id
