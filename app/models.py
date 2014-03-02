from app import db
import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.Integer)
    title = db.Column(db.String(45))
    organization = db.Column(db.String(45))
    email = db.Column(db.String(45), unique=True)
    password = db.Column(db.String(45))
    firstname = db.Column(db.String(45))
    firstname2 = db.Column(db.String(45))
    lastname = db.Column(db.String(45))
    lastname2 = db.Column(db.String(45))
    phonetype = db.Column(db.Integer)
    address = db.Column(db.String(90))
    city = db.Column(db.String(45))
    state = db.Column(db.String(45))
    zipcode = db.Column(db.String(10))

    # permanent address
    permanentaddress =db.Column(db.String(90))
    permanentcity = db.Column(db.String(45))
    permanentstate = db.Column(db.String(45))
    permanentzipcode = db.Column(db.String(10))

    #  school information
    ged = db. Column(db.Integer)
    highschoolname = db.Column(db.String(45))
    highschoolcity = db.Column(db.String(45))
    highschoolstate = db.Column(db.String(45))
    highschoolyear = db.Column(db.String(10))
    currentcollegename = db.Column(db.String(45))
    currentcollegecity = db.Column(db.String(45))
    currentcollegestate = db.Column(db.String(45))
    currentcollegetype = db.Column(db.Integer)
    communitycollegelevel = db.Column(db.Integer)
    traditionalcollegelevel = db.Column(db.Integer)
    gradlevel = db.Column(db.Integer)
    techproflevel = db.Column(db.Integer)
    major = db.Column(db.String(45))
    gpa = db.Column(db.String(45))
    studentid = db.Column(db.String(45))

    # future school info
    plannedcollegename = db.Column(db.String(45))
    plannedcollegecity = db.Column(db.String(45))
    plannedcollegestate = db.Column(db.String(45))
    plannedcollegetype = db.Column(db.Integer)
    plannedcommunitycollegelevel = db.Column(db.Integer)
    plannedtraditionalcollegelevel = db.Column(db.Integer)
    plannedgradlevel = db.Column(db.Integer)
    plannedtechproflevel = db.Column(db.Integer)
    plannedmajor = db.Column(db.String(45))

    pastrecipient = db.Column(db.Integer)
    receivingyear = db.Column(db.String(10))
    referral = db.Column(db.Text)
    awardcycle = db.Column(db.String(10))
    essaytext1 = db.Column(db.Text)
    essaytext2 = db.Column(db.Text)

    # confidential demographics
    financialaid = db. Column(db.Integer)
    financialaidreason = db.Column(db.String(45))
    financialaward = db. Column(db.Integer)
    financialawardlist = db.Column(db.String(45))
    economicallydisadvantaged = db. Column(db.Integer)
    income = db. Column(db.Integer)
    headofhousehold = db. Column(db.Integer)
    dependents = db.Column(db.String(45))
    parent = db. Column(db.Integer)
    children = db. Column(db.Integer)
    immigrant = db. Column(db.Integer)
    immigrationcountry = db.Column(db.String(45))
    immigrationdate = db.Column(db.String(45))
    motherimmigrant = db. Column(db.Integer)
    motherimmigrationcountry = db.Column(db.String(45))
    motherimmigrationdate = db.Column(db.String(45))
    mothereducation = db.Column(db.String(45))
    fatherimmigrant = db. Column(db.Integer)
    fatherimmigrationcountry = db.Column(db.String(45))
    fatherimmigrationdate = db.Column(db.String(45))
    fathereducation = db.Column(db.String(45))
    ab540 = db. Column(db.Integer)
    firstgencollege = db. Column(db.Integer)
    primaryhomelanguage = db.Column(db.String(45))

    # reference info
    ref1firstname = db.Column(db.String(45))
    ref1lastname = db.Column(db.String(45))
    ref1email = db.Column(db.String(45))
    ref2firstname = db.Column(db.String(45))
    ref2lastname = db.Column(db.String(45))
    ref2email = db.Column(db.String(45))


    timestamp = db.Column(db.DateTime)
    application_complete = db.Column(db.Integer, default = 0)
    all_recs_complete = db.Column(db.Integer)

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


class Recommendation(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	student_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	recommender_id = db.Column(db.Integer)
	KnownApplicant = db.Column(db.Text)
	Capacity = db.Column(db.Text)
	OtherCapacity = db.Column(db.Text)
	Recommendation = db.Column(db.Text)
	refCertify = db.Column(db.Integer)
	Criteria1Rating = db.Column(db.Integer)
	Criteria1Comment = db.Column(db.Text)
	Criteria2Rating = db.Column(db.Integer)
	Criteria2Comment = db.Column(db.Text)
	Criteria3Rating = db.Column(db.Integer)
	Criteria3Comment = db.Column(db.Text)
	Criteria4Rating = db.Column(db.Integer)
	Criteria4Comment = db.Column(db.Text)
	Criteria5Rating = db.Column(db.Integer)
	Criteria5Comment = db.Column(db.Text)
	Criteria6Rating = db.Column(db.Integer)
	Criteria6Comment = db.Column(db.Text)	
	Criteria7Rating = db.Column(db.Integer)
	Criteria7Comment = db.Column(db.Text)
	OverallRating = db.Column(db.Integer)
	OverallComment = db.Column(db.Text)
	timestamp = db.Column(db.DateTime)

	def __repr__(self):
		return '<Recommendation %r>' % (self.id)

	def is_recommendation_complete(self):
		if self.Criteria1Rating and self.Criteria1Comment and self.Criteria2Rating and self.Criteria2Comment and self.Criteria3Rating and self.Criteria3Comment and self.Criteria4Rating and self.Criteria4Comment and self.Criteria5Rating and self.Criteria5Comment and self.Criteria6Rating and self.Criteria6Comment and self.Criteria7Rating and self.Criteria7Comment and self.OverallRating and self.OverallComment:
			return True
		return False


class Evaluation(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	evaluator_id = db.Column(db.Integer)
	student_id = db.Column(db.Integer)
	rating = db.Column(db.Integer)
	notes = db.Column(db.Text)

	def is_evaluation_complete(self):
		if rating:
			return True
		return False
