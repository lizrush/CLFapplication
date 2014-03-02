
from app import db
import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.Integer)
    email = db.Column(db.String(45), unique=True)
    password = db.Column(db.String(45))
    firstname = db.Column(db.String(45))
    lastname = db.Column(db.String(45))
    phone = db.Column(db.String(45))
    address = db.Column(db.String(90))
    city = db.Column(db.String(45))
    state = db.Column(db.String(45))
    zipcode = db.Column(db.String(10))
    languages = db.Column(db.Text)
    culturalgroups = db.Column(db.Text)
    working = db.Column(db.Text)
    rec1firstname = db.Column(db.String(45))
    rec1lastname = db.Column(db.String(45))
    rec1email = db.Column(db.String(45))
    rec1phone = db.Column(db.String(45))
    rec1how = db.Column(db.Text)
    rec2firstname = db.Column(db.String(45))
    rec2lastname = db.Column(db.String(45))
    rec2email = db.Column(db.String(45))
    rec2phone = db.Column(db.String(45))
    rec2how = db.Column(db.Text)
    rec3firstname = db.Column(db.String(45))
    rec3lastname = db.Column(db.String(45))
    rec3email = db.Column(db.String(45))
    rec3phone = db.Column(db.String(45))
    rec3how = db.Column(db.Text)
    eval1_id = db.Column(db.Integer)
    eval2_id = db.Column(db.Integer)
    eval3_id = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)
    application_complete = db.Column(db.Integer, default = 0)
    recommendations = db.relationship('Recommendation', backref = 'requester', lazy = 'dynamic')    
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

'''
    def profile_complete(self):
#        if self.email and self.password and self.culturalgroups and self.working:
           return True
        return False

    def essay_questions_complete(self):
#        if self.basicq1 and self.basicq2 and self.basicq3 and self.basicq4 and \
#           self.basicq5 and self.basicq6 and self.basicq7 and self.basicq8 and self.basicq9:
           return True
        return False

    def documents_complete(self):
#        if self.Q01 and self.Q02 and self.Q03 and self.Q04 and self.Q05 and self.Q06 and \
#           self.Q07 and self.Q08 and self.Q09 and self.Q10 and self.Q11 and self.Q12:
           return True
        return False
\
    def recommendations_complete(self):
#        if self.rec1firstname and self.rec1lastname and self.rec1email and self.rec1phone and \
#           self.rec1how and self.rec2firstname and self.rec2lastname and self.rec2email and \
#           self.rec2phone and self.rec2how and self.rec3firstname and self.rec3lastname and \
#           self.rec3email and self.rec3phone and self.rec3how:
           return True
        return False
'''


class Recommendation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recommender_id = db.Column(db.Integer)
    recq1 = db.Column(db.Integer)
    recq1text = db.Column(db.Text)
    recq2 = db.Column(db.Integer)
    recq2text = db.Column(db.Text)
    recq3 = db.Column(db.Integer)
    recq3text = db.Column(db.Text)
    recq4 = db.Column(db.Integer)
    recq4text = db.Column(db.Text)
    recq5 = db.Column(db.Integer)
    recq5text = db.Column(db.Text)
    recq6 = db.Column(db.Integer)
    recq6text = db.Column(db.Text)
    recq7 = db.Column(db.Text)
    recq8 = db.Column(db.Text)
    recommendation_complete = db.Column(db.Integer, default = 0)
    timestamp = db.Column(db.DateTime)
    
    def __repr__(self):
        return '<Recommendation %r>' % (self.id)
        
    def is_recommendation_complete(self):
        if self.recq1 and self.recq1ex and self.recq2 and self.recq2ex and self.recq3 and self.recq3ex and \
            self.recq4 and self.recq4ex and self.recq5 and self.recq5ex and self.recq6 and self.recq6ex and \
            self.recq7 and self.recq8:
            self.recommendation_complete = 1
            db.session.add(self)
            db.session.commit()
            return True
        return False

##### Begin code block for selector process

class Evaluation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    evaluator_id = db.Column(db.Integer)
    student_id = db.Column(db.Integer)
    critical = db.Column(db.Integer)
    mission = db.Column(db.Integer)
    community = db.Column(db.Integer)
    inspire = db.Column(db.Integer)
    yesno = db.Column(db.Text)
    interview = db.Column(db.Text)
    additional = db.Column(db.Text)
    evaluation_complete = db.Column(db.Integer, default = 0)

    def is_evaluation_complete(self):
        if self.critical and self.mission and self.community and self.inspire and self.yesno and self.interview:
            self.evaluation_complete = 1
            db.session.add(self)
            db.session.commit()
            return True

        return False

##### End code block for selector process
