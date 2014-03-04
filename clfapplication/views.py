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
from clfapplication.forms import ProfileForm, BackgroundForm, DemographicForm, ScholarshipForm, DocumentsForm, EssayForm, RecommendationsForm, RecommenderForm, EvaluatorForm, ChangeRecommenderContact, ForgotPasswordForm, ResetPasswordForm


#Login page
def login(request):
        username =request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
                if user.is_active:
                        login(request, user)

def logout(request):
	logout(request)


@login_required
def index(request):
	recs = []
	return render(request, 'index.html')
'''	if user.role ==2:
		return redirect('/rec_index')
	if user.role ==3:
		return redirect('/eval_index')
	if user.role ==4:
		return redirect('/staffview')
	if user.application_complete ==1:
		recs.append(User.objects.filter_by(email = user.rec1email).first())
		recs.append(User.objects.filter_by(email = user.rec2email).first())
		recs.append(User.objects.filter_by(email = user.rec3email).first())'''


def createprofile(request):
	user = None
	if request.method == 'POST':
		form = ProfileForm(request.POST)
		if not form.password or form.password == '':
			del form.password
		if form.is_valid():
			login(request, user)
			return HttpResponseRedirect('index')
	else:
		form = ProfileForm()
	return render(request, 'profile.html', {'form':form})

@login_required
def profile(request):
	if request.method == 'POST':
		form = ProfileForm(request.POST)
		if not form.password or form.password == '':
			del form.password
		if form.is_valid():
			login(request, user)
			return HttpResponseRedirect('index')
	else:
		form = ProfileForm()
	return render(request, 'profile.html', {'form':form})


@login_required
def background(request):
	if request.method == 'POST':
		form = BackgroundForm(request.POST)
		if form.is_valid():
			login(request, user)
			return HttpResponseRedirect('index')
	else:
		form = BackgroundForm()
	return render(request, 'background.html', {'form':form})


@login_required
def demographic(request):
	if request.method == 'POST':
		form = DemographicForm(request.POST)
		if form.is_valid():
			login(request, user)
			return HttpResponseRedirect('index')
	else:
		form = DemographicForm()
	return render(request,'demographic.html', {'form':form})


@login_required
def essayquestions(request):
	if request.method == 'POST':
		form = EssayForm(request.POST)
		if form.is_valid():
			login(request, user)
			return HttpResponseRedirect('index')
	else:	
		form = EssayForm()
	return render(request, 'essayquestions.html', {'form':form})


@login_required
def documents(request):
	if request.method == 'POST':
		form = DocumentsForm(request.POST)
		if form.is_valid():
			login(request, user)
			return HttpResponseRedirect('index')
	else:
		form = DocumentsForm()
	return render(request, 'documents.html', {'form':form})



@login_required
def recommenders(request):
	if request.method == 'POST':
		form = RecommendationsForm(request.POST)
		if form.is_valid():
			login(request, user)
			return HttpResponseRedirect('index')
	else:
		form = RecommendationsForm()
	return render(request, 'recommenders.html', {'form':form})



@login_required
def finalsubmission(request):
	return render(request, 'finalsubmission.html')


def help(request):
	return render(request, 'help.html', {'form':form})

@login_required
def staffview(request):
		return render_template("reports.html")

@login_required
def received(request):
	make_new_recommenders(user)
	make_blank_recommendations(user)
	completed_app_count = len(User.objects.filter_by(application_complete =1).all())
	new_application_submitted(user, completed_app_count)
	notify_applicant(user)
	notify_recommenders(user)
	return render(request, 'received.html')
'''	if user.role ==2:
		return redirect('/rec_index')
	if user.application_complete ==1:
		return redirect('/index')'''


def make_new_recommenders(user):
	recommender1 = User.objects.filter_by(email = user.rec1email, role = 2).first()
	recommender2 = User.objects.filter_by(email = user.rec2email, role = 2).first()
	recommender3 = User.objects.filter_by(email = user.rec3email, role = 2).first()
	if not recommender1:
		recommender1 = User(firstname = user.rec1firstname, lastname = user.rec1lastname, email = user.rec1email, phone = user.rec1phone, password = generate_recommender_password(user.rec1firstname, user.rec1lastname), role =2, all_recs_complete =0)
		recommender1.save()
	if not recommender2:
		recommender2 = User(firstname = user.rec2firstname, lastname = user.rec2lastname, email = user.rec2email, phone = user.rec2phone, password = generate_recommender_password(user.rec2firstname, user.rec2lastname), role = 2, all_recs_complete =0)
		recommender2.save()
	if not recommender3:
		recommender3 = User(firstname = user.rec3firstname, lastname = user.rec3lastname, email = user.rec3email, phone = user.rec3phone, password = generate_recommender_password(user.rec3firstname, user.rec3lastname), role = 2, all_recs_complete =0)
		recommender1.save()

def make_blank_recommendations(user):
	firstrec = Recommendation(student_id = user.id, recommender_id = User.objects.filter_by(email = user.rec1email, role =2).first().id)
	secondrec = Recommendation(student_id = user.id, recommender_id = User.objects.filter_by(email = user.rec2email, role = 2).first().id)
	thirdrec = Recommendation(student_id = user.id, recommender_id = User.objects.filter_by(email = user.rec3email, role = 2).first().id)
	firstrec.save()
	secondrec.save()
	thirdrec.save()

def generate_recommender_password(firstname, lastname):
    import random
    pieces = [random.choice([firstname,lastname]),str(random.randint(1000,9999))]
    i = random.choice(pieces)
    password = i
    pieces.remove(i)
    password = i+pieces[0]
    password = password.replace(" ","")
    return password

@login_required
def forgot(request):
    form = ForgotPasswordForm(request.form)
    if request.method == "POST" and form.validate():
        s = Signer(app.config['SECRET_KEY'])
        token = s.sign(request.form['email'])
        send_password_reset(form.get_user(), token)
        return redirect('/forgot_confirmation')
    return render_template("forgot.html", form=form)

@login_required
def forgot_confirmation(request):
    return render(request, "forgot_confirmation.html")

@login_required
def reset_password(request):
    form = ResetPasswordForm(request.form)
    if request.method == "POST" and form.validate():
        token = form.token.data
        s = Signer(app.config['SECRET_KEY'])
        try:
            email = s.unsign(token)
        except BadSignature:
            return render_template("reset_invalid_token.html")
        user = User.objects.filter_by(email=email).first()
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

@login_required
def rec_index(request):
	students = User.objects.all() # placeholder
	return render(request, 'rec_index.html', {'students':students})

def guidelines(request):
	return render(request, 'guidelines.html')

@login_required
def eval_index(request):
	students = User.objects.all() # placeholder
	return render(request, 'eval_index.html', {'students':students})

@login_required
def recommend(request, student_id):#pass in the student this is for
	student = User.objects.get(id = student_id) #look up the recommendation that is for 
	if request.method == 'POST':
		form = RecommenderForm(request.POST)
		if form.is_valid():
			login(request, user)
			return HttpResponseRedirect('index')
	else:
		form = RecommenderForm()
	return render(request, 'recommendation.html', {'student': student, 'form':form})


@login_required
def rec_finalsubmission(request):
# Do stuff here
	return render(request, "rec_finalsubmission.html")


@login_required
def rec_received(request):
    return render(request, "rec_received.html")


@login_required
def evaluate(request, student_id):#pass in the student this is for
	student = User.objects.get(id = student_id)
	if request.method == 'POST':
		form = EvaluatorForm(request.POST)
		if form.is_valid():
			login(request, user)
			return HttpResponseRedirect('eval_index')
	else:
		form = EvaluatorForm(request.POST)
	return render(request, 'evaluate.html', {'student': student, 'form':form})


@login_required
def eval_finalsubmission(request):
	if user.evals_complete == True:
		return HttpResponseRedirect('/eval_index')
		return render_template("eval_received.html")
	return render(request, "eval_finalsubmission.html")


@login_required
def eval_received(request):
    if user.are_evals_complete() ==False:
        return redirect('/eval_finalsubmission')
    if user.are_evals_complete() ==True:
        return redirect('/eval_index')
    return render(request, "eval_received.html")


@login_required
def myrecommender(request, recommender_id):
    if user.role ==2:
        return redirect('/rec_index')
    if user.role ==0:
        return redirect('/staffview')
    #get the recommender sent from the click on index and put it into the form
    recommender = User.objects.filter_by(id = recommender_id).first()
    form = ChangeRecommenderContact(obj=recommender)
    if recommender.email == user.rec1email:
        whichRec = 1
    if recommender.email == user.rec2email:
        whichRec = 2
    if recommender.email == user.rec3email:
        whichRec = 3
	if form.validate_on_submit():
		form.populate_obj(recommender)
		recommender.save()
		newrec = User.objects.get(recommender.id)
		if whichRec==1:
			user.rec1email = newrec.email
		if whichRec==2:
			user.rec2email = newrec.email
		if whichRec==3:
			user.rec3email = newrec.email
		user.save()
		#send email to the recommender
		remind_recommender(user, recommender)

		return redirect('/index')
	return render(request, "myrecommender.html", recommender = recommender, form = form)


@login_required
def view_recommendations(request, student_id):
	recs = Recommendation.objects.filter_by(student_id = student_id).all()
	return render(request, "view_recommendations.html", recs = recs)

@login_required
def view_evaluations(request, student_id):
	applicant = User.objects.get(student_id)
	evals = Evaluation.objects.filter_by(student_id = student_id).all()
	evaluators=[]
	for e in evals:
		evaluator = User.objects.filter_by(id = e.evaluator_id).first()
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
