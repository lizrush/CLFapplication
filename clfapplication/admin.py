from django.contrib import admin
from clfapplication.models import Recommendation, Evaluation, Applicant, Evaluator, Recommender, Staff


# Register your models here.
admin.site.register(Applicant)
admin.site.register(Recommender)
admin.site.register(Evaluator)
admin.site.register(Staff)
admin.site.register(Evaluation)
admin.site.register(Recommendation)
