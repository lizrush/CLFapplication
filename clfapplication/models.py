from django.db import models

class User(models.Model):
    role = models.IntegerField()
    title = models.CharField(max_length=45)
    organization = models.CharField(max_length=45)
    email = models.CharField(max_length=45, unique=True)
    password = models.CharField(max_length=45)
    firstname = models.CharField(max_length=45)
    firstname2 = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    lastname2 = models.CharField(max_length=45)
    phonetype = models.IntegerField()
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
    ged = models.IntegerField()
    highschoolname = models.CharField(max_length=45)
    highschoolcity = models.CharField(max_length=45)
    highschoolstate = models.CharField(max_length=45)
    highschoolyear = models.CharField(max_length=10)
    currentcollegename = models.CharField(max_length=45)
    currentcollegecity = models.CharField(max_length=45)
    currentcollegestate = models.CharField(max_length=45)
    currentcollegetype = models.IntegerField()
    communitycollegelevel = models.IntegerField()
    traditionalcollegelevel = models.IntegerField()
    gradlevel = models.IntegerField()
    techproflevel = models.IntegerField()
    major = models.CharField(max_length=45)
    gpa = models.CharField(max_length=45)
    studentid = models.CharField(max_length=45)

    # future school info
    plannedcollegename = models.CharField(max_length=45)
    plannedcollegecity = models.CharField(max_length=45)
    plannedcollegestate = models.CharField(max_length=45)
    plannedcollegetype = models.IntegerField()
    plannedcommunitycollegelevel = models.IntegerField()
    plannedtraditionalcollegelevel = models.IntegerField()
    plannedgradlevel = models.IntegerField()
    plannedtechproflevel = models.IntegerField()
    plannedmajor = models.CharField(max_length=45)

    pastrecipient = models.IntegerField()
    receivingyear = models.CharField(max_length=10)
    referral = models.TextField()
    awardcycle = models.CharField(max_length=10)
    essaytext1 = models.TextField()
    essaytext2 = models.TextField()

    # confidential demographics
    financialaid = models.IntegerField()
    financialaidreason = models.CharField(max_length=45)
    financialaward = models.IntegerField()
    financialawardlist = models.CharField(max_length=45)
    economicallydisadvantaged = models.IntegerField()
    income = models.IntegerField()
    headofhousehold = models.IntegerField()
    dependents = models.CharField(max_length=45)
    parent = models.IntegerField()
    children = models.IntegerField()
    immigrant = models.IntegerField()
    immigrationcountry = models.CharField(max_length=45)
    immigrationdate = models.CharField(max_length=45)
    motherimmigrant = models.IntegerField()
    motherimmigrationcountry = models.CharField(max_length=45)
    motherimmigrationdate = models.CharField(max_length=45)
    mothereducation = models.CharField(max_length=45)
    fatherimmigrant = models.IntegerField()
    fatherimmigrationcountry = models.CharField(max_length=45)
    fatherimmigrationdate = models.CharField(max_length=45)
    fathereducation = models.CharField(max_length=45)
    ab540 = models.IntegerField()
    firstgencollege = models.IntegerField()
    primaryhomelanguage = models.CharField(max_length=45)

    # reference info
    ref1firstname = models.CharField(max_length=45)
    ref1lastname = models.CharField(max_length=45)
    ref1email = models.CharField(max_length=45)
    ref2firstname = models.CharField(max_length=45)
    ref2lastname = models.CharField(max_length=45)
    ref2email = models.CharField(max_length=45)
    timestamp = models.IntegerField()
    application_complete = models.IntegerField(default = 0)
    all_recs_complete = models.IntegerField()

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



class Evaluator(models.Model):
    role = models.IntegerField()
    title = models.CharField(max_length=45)
    organization = models.CharField(max_length=45)
    email = models.CharField(max_length=45, unique=True)
    password = models.CharField(max_length=45)
    firstname = models.CharField(max_length=45)
    firstname2 = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    lastname2 = models.CharField(max_length=45)
    phonetype = models.IntegerField()
    address = models.CharField(max_length=90)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    zipcode = models.CharField(max_length=10)
  
    
class Recommender(models.Model):
    role = models.IntegerField()
    title = models.CharField(max_length=45)
    organization = models.CharField(max_length=45)
    email = models.CharField(max_length=45, unique=True)
    password = models.CharField(max_length=45)
    firstname = models.CharField(max_length=45)
    firstname2 = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    lastname2 = models.CharField(max_length=45)
    phonetype = models.IntegerField()
    address = models.CharField(max_length=90)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    zipcode = models.CharField(max_length=10)


class Recommendation(models.Model):
	student_id = models.ForeignKey(User)
	recommender_id = models.ForeignKey(Recommender)
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
	student_id = models.ForeignKey(User)
	evaluator_id = models.ForeignKey(Evaluator)
	rating = models.IntegerField()
	notes = models.TextField()

	def is_evaluation_complete(self):
		if rating:
			return True
		return False

        def __unicode__(self):
                return self.id
