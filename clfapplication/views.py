# Import resources
import urlparse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from clfapplication.models import User, Evaluation, Recommendation

#Login page
def login(request):
        username =request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
                if user.is_active:
                        login(request, user)

#Logout page
def logout(request):
        logout(request)


def rec_login(request):
#    form = RecLoginForm()
#    if form.validate_on_submit():
#        recommender = form.get_recommender()
#        login_user(recommender)
#        return redirect('/rec_index')
	return render(request, 'rec_login.html')


def eval_login(request):
#    form = EvalLoginForm()
#    if form.validate_on_submit():
#        evaluator = form.get_evaluator()
#        login_user(evaluator)
#        return redirect('/evaluate_index')
 	return render(request, 'eval_login.html')


#@login_required
def index(request):
	recs = []
	return render(request, 'index.html')
'''	if current_user.role ==2:
		return redirect('/rec_index')
	if current_user.role ==3:
		return redirect('/eval_index')
	if current_user.role ==4:
		return redirect('/staffview')
	if current_user.application_complete ==1:
		recs.append(User.query.filter_by(email = current_user.rec1email).first())
		recs.append(User.query.filter_by(email = current_user.rec2email).first())
		recs.append(User.query.filter_by(email = current_user.rec3email).first())'''


def createprofile(request):
	user = None
	form = ProfileForm(obj=user)
	if not form.password or form.password == '':
		del form.password    
	if form.validate_on_submit():
		if user:
			flash('Successfully updated your profile.')
		else:
			user = User()
			user.role = 1
			flash('Congratulations, you just created an account!')
		form.populate_obj(user)
		user.save()
		login(request, user)
		return redirect('/')
	return render(request, 'profile.html')


def profile(request):
	return render(request, 'profile.html')
#	if current_user.is_authenticated():
#		user = current_user
#	else:
#		return redirect('/login')
#	form = ProfileForm(obj=current_user)
#	if not form.password or form.password == '':
#		del form.password
#	if form.validate_on_submit():
#		form.populate_obj(current_user)
#	current_user.save()



def background(request):
	form = BackgroundForm(obj=current_user)
	if form.validate_on_submit():
		form.populate_obj(current_user)
		db.session.add(current_user)
		db.session.commit()
	return render(request, 'background.html')
	
	
def demographic(request):
	return render(request,'demographic.html')
#	form = DemographicForm(obj=current_user)
#	if form.validate_on_submit():
#		form.populate_obj(current_user)
#		db.session.add(current_user)
#		db.session.commit()



def essayquestions(request):
	form = EssayForm(obj=current_user)
	if form.validate_on_submit():
		form.populate_obj(current_user)
		db.session.add(current_user)
		db.session.commit()
		return redirect('/')
	return render(request, 'essayquestions.html')


def documents(request):
    return render_template('documents.html')
#    form = TechskillsForm(obj=current_user)
 #   if form.validate_on_submit():
  #      form.populate_obj(current_user)
 #       db.session.add(current_user)
 #       db.session.commit()
 #       return redirect('/')



def recommenders(request):
    form = RecommendationsForm(obj=current_user)
    if form.validate_on_submit():
        form.populate_obj(current_user)
        db.session.add(current_user)
        db.session.commit()
        return redirect('/')
	return render(request, 'rec_login.html', {'form':form})

def finalsubmission(request):
	return render(request, 'finalsubmission.html')


def help(request):
	return render(request, 'help.html', {'form':form})


def staffview(request):
    if current_user.role ==1:
        return redirect('/index')
    if current_user.role ==2:
        return redirect('/rec_index')
    if current_user.role ==3:
        return redirect('/eval_index')
	finishedapplicants = User.query.filter_by(application_complete =1).all()
	sortedapplicants = []
	recommenders = User.query.all()
	finalistsRound1 = []
	displaymatrix = []
	trythismatrix = []
	for a in finishedapplicants:
		evals = Evaluation.query.filter_by(student_id = a.id).all()
		yeses = 0
		complete = 0
		totalscores =[]
		averagescore = 0
		for e in evals:
			if e.mission and e.critical and e.community and e.inspire:
				complete +=1
				totalscores.append((int(e.critical)+int(e.mission)+int(e.community)+int(e.inspire)))
			if e.yesno =='Yes':
				yeses +=1	
			if len(totalscores) >0:	
				averagescore = float(float((sum(totalscores))) /len(totalscores))
			else:
				averagescore = 0
		averagescore = int(averagescore * 100) / 100.0
		if complete <3:
			displaymatrix.append([a.id, a.firstname, a.lastname, a.city, a.state, averagescore, yeses])
		displaymatrix= sorted(displaymatrix, key=lambda applicant: applicant[5], reverse = True)
		for d in displaymatrix:
			entry = User.query.get(d[0])
			trythismatrix.append(entry)
		recommendations = Recommendation.query.all()
		return render_template("displayfinalists.html", finishedapplicants = finishedapplicants, recommendations = recommendations, recommenders = recommenders, finalistsRound1 = trythismatrix, displaymatrix = displaymatrix)
		

def received(request):
	if current_user.role ==2:
		return redirect('/rec_index')
	if current_user.application_complete ==1:
		return redirect('/index')
	current_user.application_complete =1
	db.session.add(current_user)
	db.session.commit()
	make_new_recommenders(current_user)
	make_blank_recommendations(current_user)
	completed_app_count = len(User.query.filter_by(application_complete =1).all())
	new_application_submitted(current_user, completed_app_count)
	notify_applicant(current_user)
	notify_recommenders(current_user)
	return render(request, 'received.html')


def make_new_recommenders(user):
	recommender1 = User.query.filter_by(email = user.rec1email, role = 2).first()
	recommender2 = User.query.filter_by(email = user.rec2email, role = 2).first()
	recommender3 = User.query.filter_by(email = user.rec3email, role = 2).first()
	if not recommender1:
		recommender1 = User(firstname = user.rec1firstname, lastname = user.rec1lastname, email = user.rec1email, phone = user.rec1phone, password = generate_recommender_password(user.rec1firstname, user.rec1lastname), role =2, all_recs_complete =0)
		db.session.add(recommender1)
	if not recommender2:
		recommender2 = User(firstname = user.rec2firstname, lastname = user.rec2lastname, email = user.rec2email, phone = user.rec2phone, password = generate_recommender_password(user.rec2firstname, user.rec2lastname), role = 2, all_recs_complete =0)
		db.session.add(recommender2)
	if not recommender3:
		recommender3 = User(firstname = user.rec3firstname, lastname = user.rec3lastname, email = user.rec3email, phone = user.rec3phone, password = generate_recommender_password(user.rec3firstname, user.rec3lastname), role = 2, all_recs_complete =0)
		db.session.add(recommender3)
		db.session.commit()

def make_blank_recommendations(user):
    firstrec = Recommendation(student_id = user.id, recommender_id = User.query.filter_by(email = user.rec1email, role =2).first().id)
    secondrec = Recommendation(student_id = user.id, recommender_id = User.query.filter_by(email = user.rec2email, role = 2).first().id)
    thirdrec = Recommendation(student_id = user.id, recommender_id = User.query.filter_by(email = user.rec3email, role = 2).first().id)
    db.session.add(firstrec)
    db.session.add(secondrec)
    db.session.add(thirdrec)
    db.session.commit()

def generate_recommender_password(firstname, lastname):
    import random    
    pieces = [random.choice([firstname,lastname]),str(random.randint(1000,9999))]
    i = random.choice(pieces)
    password = i
    pieces.remove(i)    
    password = i+pieces[0]
    password = password.replace(" ","")
    return password


def forgot(request):
    form = ForgotPasswordForm(request.form)
    if request.method == "POST" and form.validate():
        s = Signer(app.config['SECRET_KEY'])
        token = s.sign(request.form['email'])
        send_password_reset(form.get_user(), token)
        return redirect('/forgot_confirmation')
    return render_template("forgot.html", form=form)

def forgot_confirmation(request):
    return render(request, "forgot_confirmation.html")

def reset_password(request):
    form = ResetPasswordForm(request.form)
    if request.method == "POST" and form.validate():
        token = form.token.data
        s = Signer(app.config['SECRET_KEY'])
        try:
            email = s.unsign(token)
        except BadSignature:
            return render_template("reset_invalid_token.html")
        user = User.query.filter_by(email=email).first()
        if user:
            user.set_password(form.password.data)
            print user.password
            login_user(user)
            return redirect("/")
        else:
            return render_template("reset_invalid_token.html")
    token = request.args.get('token', None)
    if not token:
        return render_template("reset_invalid_token.html")
    return render(request, "reset_password.html", {'form':form, 'token':token})


def rec_index(request):
	if current_user.role ==1:
		return redirect('/index')
	if current_user.role ==4:
		return redirect('/staffview')
	students = []
	recs =[]    
	student1 = User.query.filter_by(ref1email = current_user.email).first()
#	student2 = (User.query.filter_by(rec2email = current_user.email, application_complete =1).all())
#	student3 = (User.query.filter_by(rec3email = current_user.email, application_complete =1).all())
	students.append(student1)
#	if student2:
#		for s2 in student2:
#			students.append(s2)
#	if student3:
#		for s3 in student3:
#			students.append(s3)
#	for s in students:
#		recommendation = Recommendation.query.filter_by(student_id = s.id, recommender_id = current_user.id).first()
#		if recommendation and recommendation.is_recommendation_complete():
#			recommendation.recommendation_complete =1
#		recs.append(recommendation)
	return render_template('rec_index.html',
		students=students, recs = recs)



@login_required
def eval_index(request):
	if current_user.role ==1:
		return redirect('/index')
	if current_user.role ==4:
		return redirect('/staffview')
	students = []
	recs =[]    
	student1 = User.query.filter_by(ref1email = current_user.email).first()
#	student2 = (User.query.filter_by(rec2email = current_user.email, application_complete =1).all())
#	student3 = (User.query.filter_by(rec3email = current_user.email, application_complete =1).all())
	students.append(student1)
#	if student2:
#		for s2 in student2:
#			students.append(s2)
#	if student3:
#		for s3 in student3:
#			students.append(s3)
#	for s in students:
#		recommendation = Recommendation.query.filter_by(student_id = s.id, recommender_id = current_user.id).first()
#		if recommendation and recommendation.is_recommendation_complete():
#			recommendation.recommendation_complete =1
#		recs.append(recommendation)
	return render_template('eval_index.html',
		students=students)





@login_required
def recommend(request, student_id):#pass in the student this is for
    if current_user.role ==1:
        return redirect('/index')
    student = User.query.get(student_id) #look up the recommendation that is for this student and this recommender
    recommendation = Recommendation.query.filter_by(student_id=student.id, recommender_id=current_user.id).first() #get the recommendation that matches this student and this recommender
    form = RecommenderForm(obj=recommendation) #pull up the form for this recommendation
    if form.validate_on_submit():
        form.populate_obj(recommendation)
        db.session.add(recommendation)
        db.session.commit()
        return redirect('/rec_index')
    return render(request, 'recommendation.html', form=form, student=student, recommendation=recommendation)#Tell it to pull up a form for this particular recommendation and its corresponding student


@login_required
def rec_finalsubmission(request):
    if current_user.role ==1:
        return redirect('/index')
    current_user.are_recs_complete()
    db.session.add(current_user)
    db.session.commit()
    return render(request, "rec_finalsubmission.html")


@login_required
def rec_help(request):
    if current_user.role ==1:
        return redirect('/index')
    return render(request, "rec_help.html")


@login_required
def rec_forgot(request):
    if current_user.role ==1:
        return redirect('/index')
    return render_template("rec_forgot.html")


@login_required
def rec_logout(request):
    logout_user()
    return redirect("http://www.codeforprogress.org")


@login_required
def rec_received(request):
    if current_user.role ==1:
        return redirect('/index')
    return render(request, "rec_received.html")


@login_required
def evaluate_index(request):
    if current_user.role ==1:
        return redirect('/index')
    if current_user.role ==2:
        return redirect('/rec_index')
    if current_user.role ==4:
        assignedapplicants =[]
        evals = Evaluation.query.filter_by(evaluator_id = current_user.id).all()
        for e in evals:
            a = User.query.filter_by(id = e.student_id).first()
            assignedapplicants.append(a)
        return render(request, "evaluate_index.html", assignedapplicants = assignedapplicants, evals=evals, user = current_user)


@login_required
def evaluate(request, student_id):
    if current_user.role ==1:
        return redirect('/index')
    if current_user.role ==2:
        return redirect('/rec_index')
    if current_user.role ==4:
        student = User.query.filter_by(role = 1, id = student_id).first()
        evaluation = Evaluation.query.filter_by(student_id = student.id, evaluator_id = current_user.id).first()
        recommender1 = User.query.filter_by(email = student.rec1email).first()
        recommender2 = User.query.filter_by(email = student.rec2email).first()
        recommender3 = User.query.filter_by(email = student.rec3email).first()
	if recommender1:
	        rec1 = Recommendation.query.filter_by(student_id = student.id, recommender_id = recommender1.id).first()
	else:
		rec1 = None
	if recommender2:
	        rec2 = Recommendation.query.filter_by(student_id = student.id, recommender_id = recommender2.id).first()
	else:
		rec2 = None
        if recommender3:
		rec3 = Recommendation.query.filter_by(student_id = student.id, recommender_id = recommender3.id).first()            
	else:
		rec3 = None
        form = EvaluatorForm(obj = evaluation)
        if form.validate_on_submit():
                form.populate_obj(evaluation)
                db.session.add(evaluation)
                db.session.commit()
                return redirect('/evaluate_index')
        return render(request, "evaluate.html", f = student, form = form, evaluation =evaluation, rec1 = rec1, rec2=rec2, rec3=rec3)


@login_required
def eval_finalsubmission(request):
    evals_complete = current_user.are_evals_complete()
    db.session.add(current_user)
    db.session.commit()
    if current_user.role ==1:
        return redirect('/index')
    if current_user.role ==2:
        return redirect('/rec_index')
    if evals_complete == True:
        #return redirect('/evaluate_index')
        return render_template("eval_received.html")
    return render(request, "eval_finalsubmission.html")


@login_required
def eval_help(request):
    return render(request, "eval_help.html")


@login_required
def eval_forgot(request):
    return render(request, "eval_forgot.html")


@login_required
def eval_logout(request):
    logout_user()
    return redirect("/eval_login")


@login_required
def eval_received(request):
    if current_user.role ==1:
        return redirect('/index')
    if current_user.role ==2:
        return redirect('/rec_index')
    if current_user.are_evals_complete() ==False:
        return redirect('/eval_finalsubmission')
    if current_user.are_evals_complete() ==True:
        return redirect('/eval_index')
    return render(request, "eval_received.html")


@login_required
def myrecommender(request, recommender_id):
    if current_user.role ==2:
        return redirect('/rec_index')
    if current_user.role ==0:
        return redirect('/staffview')
    #get the recommender sent from the click on index and put it into the form
    recommender = User.query.filter_by(id = recommender_id).first()
    form = ChangeRecommenderContact(obj=recommender)
    if recommender.email == current_user.rec1email:
        whichRec = 1
    if recommender.email == current_user.rec2email:
        whichRec = 2
    if recommender.email == current_user.rec3email:
        whichRec = 3
    if form.validate_on_submit():
        form.populate_obj(recommender)
        #commits new recommender info to the database - and this is working
        db.session.add(recommender)
        db.session.commit()
        
        #reload the recommender and put its email into the appropriate place for the current_user
        newrec = User.query.get(recommender.id)
        if whichRec==1:
            current_user.rec1email = newrec.email
        if whichRec==2:
            current_user.rec2email = newrec.email
        if whichRec==3:
            current_user.rec3email = newrec.email
        db.session.add(current_user)            
        db.session.commit()
        #send email to the recommender
        remind_recommender(current_user, recommender)

        return redirect('/index')
    return render(request, "myrecommender.html", recommender = recommender, form = form)


@login_required
def view_recommendations(request, student_id):
	recs = Recommendation.query.filter_by(student_id = student_id).all()
	return render(request, "view_recommendations.html", recs = recs)
	
@login_required
def view_evaluations(request, student_id):
	applicant = User.query.get(student_id)
	evals = Evaluation.query.filter_by(student_id = student_id).all()
	evaluators=[]
	for e in evals:
		evaluator = User.query.filter_by(id = e.evaluator_id).first()
		evaluators.append(evaluator)			
	complete = 0
	totalscores =[]
	averagescore = 0
	for e in evals:
		if e.evaluation_complete == 1:
			complete +=1
			totalscores.append((int(e.critical)+int(e.mission)+int(e.community)+int(e.inspire)))
		if e.yesno =='Yes':
			yeses +=1	
			averagescore = (sum(totalscores) / float(len(totalscores)))
	return render(request, "view_evaluations.html", applicant = applicant, evals = evals, evaluators = evaluators, averagescore = averagescore, complete = complete)
