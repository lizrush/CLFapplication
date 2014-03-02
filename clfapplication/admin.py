from django.contrib import admin
from clfapplication.models import User, Recommendation, Evaluation


# Register your models here.
admin.site.register(User)
admin.site.register(Evaluation)
admin.site.register(Recommendation)
