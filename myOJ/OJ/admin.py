from django.contrib import admin

# Register your models here.
from .models import Problem,Test_cases,Submission,User_score 
admin.site.register(Problem)
admin.site.register(Test_cases)
admin.site.register(Submission)
admin.site.register(User_score)